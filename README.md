# GitHub Data Science Repository Analysis

## Descripción

Proyecto final del curso **Modelos Cuantitativos de Información** enfocado en el análisis y modelado de repositorios de Ciencia de Datos en GitHub utilizando datos reales obtenidos mediante la GitHub REST API.

El objetivo principal es identificar factores asociados a la popularidad de proyectos open source relacionados con:

* Data Science
* Machine Learning
* Artificial Intelligence
* Deep Learning
* NLP
* Computer Vision

La popularidad de los repositorios se analiza principalmente mediante la cantidad de estrellas (`stars`).

---

# Dataset

El dataset fue construido utilizando la GitHub API y contiene aproximadamente:

* 1573 repositorios
* Variables numéricas, categóricas y temporales

Variables principales:

* stars
* forks
* watchers
* open_issues
* size
* language
* topics_count
* created_at
* updated_at
* stars_per_day
* forks_to_stars_ratio

---

# Objetivos

* Analizar patrones estructurales en repositorios de Ciencia de Datos.
* Identificar factores asociados a la popularidad de proyectos open source.
* Explorar relaciones entre actividad comunitaria y éxito de repositorios.
* Construir modelos predictivos utilizando Machine Learning.

---

# Tecnologías Utilizadas

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* GitHub REST API
* Jupyter Notebook

---

# Estructura del Proyecto

```text id="7tq6nr"
PROYECTO_FINAL_ML-/
│
├── data/
│   ├── processed/
│   └── raw/
│       └── github_repositories.csv
│
├── images/
│
├── notebooks/
│   ├── 01_eda_raw.ipynb
│   └── 02_modeling.ipynb
│
├── report/
│
├── scripts/
│
├── .env
├── .gitignore
├── environment.yml
└── README.md
```

---

# Notebooks

## 01_eda_raw.ipynb

Contiene:

* análisis exploratorio de datos,
* distribuciones,
* correlaciones,
* detección de outliers,
* análisis temporal,
* visualizaciones e interpretación inicial.

## 02_modeling.ipynb

Contiene:

* preprocessing,
* feature engineering básico,
* entrenamiento de modelos,
* evaluación de métricas,
* comparación entre algoritmos.

---

# Estado Actual

## Completado

* Extracción automática de datos desde GitHub API
* Construcción del dataset
* Limpieza inicial
* Análisis exploratorio de datos (EDA)

## En Desarrollo

* Modelado predictivo
* Evaluación de modelos

## Pendiente

* Interpretación final
* Informe PDF

---

# Configuración del Entorno

## Crear entorno Conda

```bash id="ewrnl8"
conda env create -f environment.yml
```

---

## Activar entorno

```bash id="69i1e6"
conda activate proyecto_final_ML
```

---

# Configuración de GitHub API

Crear un archivo `.env` en la raíz del proyecto:

```env id="qrf5ha"
GITHUB_TOKEN=your_github_token
```

---

# Ejecución

## Extracción de datos

```bash id="68idvx"
python scripts/fetch_github_data.py
```

---

# Integrantes

* Carlos Aldana
* Carlos Angel
* Diego Monroy
