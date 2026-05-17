import os
import time
import requests
import pandas as pd
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

if not GITHUB_TOKEN:
    raise ValueError(
        "No se encontró GITHUB_TOKEN en el archivo .env"
    )


HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

BASE_URL = "https://api.github.com/search/repositories"

QUERIES = [
    "data-science",
    "machine-learning",
    "deep-learning",
    "artificial-intelligence",
    "computer-vision",
    "nlp",
    "data-analysis"
]

PER_PAGE = 100
PAGES = 3


def fetch_repositories(query, page):

    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": PER_PAGE,
        "page": page
    }

    response = requests.get(
        BASE_URL,
        headers=HEADERS,
        params=params
    )

    if response.status_code != 200:
        print(f"\nError {response.status_code}")
        print(response.text)
        return []

    data = response.json()

    return data.get("items", [])


def process_repository(repo):

    topics = repo.get("topics", [])

    description = repo.get("description") or ""

    license_info = repo.get("license")

    license_name = (
        license_info["name"]
        if license_info
        else None
    )

    return {

        # Identificación
        "repo_name": repo.get("name"),
        "full_name": repo.get("full_name"),
        "owner": repo.get("owner", {}).get("login"),

        # Popularidad
        "stars": repo.get("stargazers_count"),
        "forks": repo.get("forks_count"),
        "watchers": repo.get("watchers_count"),

        # Actividad
        "open_issues": repo.get("open_issues_count"),

        # Tamaño
        "size": repo.get("size"),

        # Metadata
        "language": repo.get("language"),
        "license": license_name,

        # Variables booleanas
        "has_issues": repo.get("has_issues"),
        "has_projects": repo.get("has_projects"),
        "has_wiki": repo.get("has_wiki"),
        "has_pages": repo.get("has_pages"),
        "archived": repo.get("archived"),

        # Topics
        "topics_count": len(topics),

        # Texto
        "description_length": len(description),

        # Fechas
        "created_at": repo.get("created_at"),
        "updated_at": repo.get("updated_at"),
        "pushed_at": repo.get("pushed_at"),

        # URL
        "html_url": repo.get("html_url")
    }



all_repositories = []

for query in QUERIES:

    print(f"\nBuscando: {query}")

    for page in range(1, PAGES + 1):

        print(f"Página {page}")

        repositories = fetch_repositories(query, page)

        for repo in repositories:

            processed_repo = process_repository(repo)

            all_repositories.append(processed_repo)

        time.sleep(1)


df = pd.DataFrame(all_repositories)

# Eliminar duplicados
df.drop_duplicates(
    subset="full_name",
    inplace=True
)


today = pd.Timestamp.now(tz="UTC")

df["created_at"] = pd.to_datetime(df["created_at"])
df["updated_at"] = pd.to_datetime(df["updated_at"])
df["pushed_at"] = pd.to_datetime(df["pushed_at"])

# Edad del repositorio
df["repo_age_days"] = (
    today - df["created_at"]
).dt.days

# Días desde última actualización
df["days_since_update"] = (
    today - df["updated_at"]
).dt.days

# Stars por día
df["stars_per_day"] = (
    df["stars"] / (df["repo_age_days"] + 1)
)

# Ratio forks/stars
df["forks_to_stars_ratio"] = (
    df["forks"] / (df["stars"] + 1)
)


output_dir = "data/raw"

os.makedirs(output_dir, exist_ok=True)

output_path = f"{output_dir}/github_repositories.csv"

df.to_csv(
    output_path,
    index=False
)

print("\nDataset guardado correctamente.")
print(f"Repositorios totales: {len(df)}")
print(f"Ruta: {output_path}")