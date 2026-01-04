# 📊 Data - Análisis y ETL

Módulo de procesamiento, análisis y transformación de datos.

## 🏗️ Estructura

```
data/
├── notebooks/           # Jupyter notebooks para análisis exploratorio
│   ├── 01_exploratory_analysis.ipynb
│   ├── 02_data_quality.ipynb
│   └── 03_feature_engineering.ipynb
├── scripts/
│   ├── etl/             # Extract, Transform, Load
│   │   ├── extract_sql.py
│   │   ├── extract_csv.py
│   │   ├── extract_api.py
│   │   ├── transform.py
│   │   └── load.py
│   ├── analysis/        # Scripts de análisis
│   │   ├── sales_analysis.py
│   │   ├── customer_segmentation.py
│   │   └── trend_detection.py
│   └── ml/              # Machine Learning
│       ├── train_model.py
│       ├── predict.py
│       └── evaluate.py
├── raw/                 # Datos crudos (no versionados)
├── processed/           # Datos procesados
├── models/              # Modelos entrenados
├── tests/               # Pruebas
└── requirements.txt
```

## 🚀 Instalación

```bash
cd data
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 📓 Jupyter Notebooks

### Iniciar Jupyter Lab

```bash
jupyter lab
```

### Notebooks Principales

1. **01_exploratory_analysis.ipynb**: Análisis exploratorio de datos (EDA)
2. **02_data_quality.ipynb**: Validación de calidad de datos
3. **03_feature_engineering.ipynb**: Creación de features

## 🔄 ETL Pipeline

### Extract (Extracción)

```python
# scripts/etl/extract_sql.py
from sqlalchemy import create_engine
import pandas as pd

def extract_from_sql(query: str, connection_string: str) -> pd.DataFrame:
    """Extrae datos desde base de datos SQL."""
    engine = create_engine(connection_string)
    df = pd.read_sql(query, engine)
    return df

# Uso
df = extract_from_sql(
    query="SELECT * FROM sales WHERE date >= '2024-01-01'",
    connection_string="postgresql://user:pass@localhost/db"
)
```

### Transform (Transformación)

```python
# scripts/etl/transform.py
import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Limpia y transforma datos."""
    # Eliminar duplicados
    df = df.drop_duplicates()
    
    # Manejar valores nulos
    df = df.fillna(method='ffill')
    
    # Normalizar columnas
    df['amount'] = df['amount'].astype(float)
    
    return df

def aggregate_data(df: pd.DataFrame) -> pd.DataFrame:
    """Agrega datos por categoría."""
    return df.groupby(['category', 'date']).agg({
        'amount': 'sum',
        'quantity': 'sum'
    }).reset_index()
```

### Load (Carga)

```python
# scripts/etl/load.py
import pandas as pd

def load_to_database(df: pd.DataFrame, table_name: str, connection_string: str):
    """Carga datos a base de datos."""
    from sqlalchemy import create_engine
    engine = create_engine(connection_string)
    df.to_sql(table_name, engine, if_exists='replace', index=False)

def load_to_parquet(df: pd.DataFrame, file_path: str):
    """Guarda datos en formato Parquet."""
    df.to_parquet(file_path, compression='snappy')
```

## 📈 Análisis de Datos

### Sales Analysis

```python
# scripts/analysis/sales_analysis.py
import pandas as pd
import matplotlib.pyplot as plt

def analyze_sales_trends(df: pd.DataFrame):
    """Analiza tendencias de ventas."""
    # Ventas por mes
    monthly_sales = df.groupby(df['date'].dt.to_period('M'))['amount'].sum()
    
    # Visualización
    plt.figure(figsize=(12, 6))
    monthly_sales.plot(kind='line')
    plt.title('Tendencia de Ventas Mensuales')
    plt.xlabel('Mes')
    plt.ylabel('Ventas ($)')
    plt.savefig('sales_trend.png')
    
    return monthly_sales
```

### Customer Segmentation

```python
# scripts/analysis/customer_segmentation.py
from sklearn.cluster import KMeans
import pandas as pd

def segment_customers(df: pd.DataFrame, n_clusters: int = 4):
    """Segmenta clientes usando K-Means."""
    features = df[['total_purchases', 'avg_order_value', 'recency']]
    
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['segment'] = kmeans.fit_predict(features)
    
    return df
```

## 🤖 Machine Learning

### Entrenamiento de Modelo

```python
# scripts/ml/train_model.py
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib

def train_sales_predictor(df: pd.DataFrame):
    """Entrena modelo de predicción de ventas."""
    X = df[['month', 'category', 'promotion']]
    y = df['sales']
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Guardar modelo
    joblib.dump(model, '../models/sales_predictor.pkl')
    
    return model
```

### Predicción

```python
# scripts/ml/predict.py
import joblib
import pandas as pd

def predict_sales(features: pd.DataFrame):
    """Realiza predicciones de ventas."""
    model = joblib.load('../models/sales_predictor.pkl')
    predictions = model.predict(features)
    return predictions
```

## 📊 Visualizaciones

### Matplotlib

```python
import matplotlib.pyplot as plt

# Gráfico de líneas
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['sales'])
plt.title('Ventas en el Tiempo')
plt.xlabel('Fecha')
plt.ylabel('Ventas')
plt.savefig('sales_plot.png')
```

### Seaborn

```python
import seaborn as sns

# Heatmap de correlación
plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Matriz de Correlación')
plt.savefig('correlation_heatmap.png')
```

### Plotly (Interactivo)

```python
import plotly.express as px

# Gráfico interactivo
fig = px.line(df, x='date', y='sales', title='Ventas Interactivas')
fig.write_html('sales_interactive.html')
```

## 🔍 Calidad de Datos

### Great Expectations

```python
import great_expectations as ge

# Crear expectativas
df_ge = ge.from_pandas(df)

# Validaciones
df_ge.expect_column_values_to_not_be_null('customer_id')
df_ge.expect_column_values_to_be_between('amount', min_value=0, max_value=10000)
df_ge.expect_column_values_to_be_in_set('status', ['pending', 'completed', 'cancelled'])

# Generar reporte
results = df_ge.validate()
```

## 🔄 Apache Airflow (ETL Scheduling)

### DAG Example

```python
# dags/daily_etl.py
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'data-team',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'daily_sales_etl',
    default_args=default_args,
    schedule_interval='0 2 * * *',  # 2 AM diario
)

extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_from_sql,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=clean_data,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load_data',
    python_callable=load_to_database,
    dag=dag,
)

extract_task >> transform_task >> load_task
```

## 📁 Gestión de Datos

### Estructura de Archivos

```
data/
├── raw/                    # Datos originales (no modificar)
│   ├── sales_2024.csv
│   └── customers.xlsx
├── processed/              # Datos procesados
│   ├── sales_clean.parquet
│   └── customers_clean.parquet
└── models/                 # Modelos ML
    ├── sales_predictor.pkl
    └── customer_segmentation.pkl
```

### Convenciones de Nombres

```
{source}_{entity}_{date}.{format}

Ejemplos:
- erp_sales_20240101.csv
- crm_customers_20240101.xlsx
- processed_sales_monthly_20240101.parquet
```

## 🧪 Testing

```bash
# Ejecutar tests
pytest tests/

# Con cobertura
pytest tests/ --cov=scripts --cov-report=html
```

## 📊 Métricas de Calidad

- **Completitud**: % de valores no nulos
- **Unicidad**: % de valores únicos
- **Validez**: % de valores dentro de rangos esperados
- **Consistencia**: Coherencia entre datasets

## 🛠️ Stack Tecnológico

- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn, Plotly
- **ETL**: Apache Airflow, Prefect
- **ML**: Scikit-learn, Statsmodels
- **Notebooks**: Jupyter Lab
- **Data Quality**: Great Expectations
- **File Formats**: Parquet, CSV, Excel

## 🤝 Contribución

1. Crear rama desde `data`
2. Desarrollar análisis o pipeline
3. Documentar en notebook o README
4. Ejecutar tests
5. Crear Pull Request hacia `data`
