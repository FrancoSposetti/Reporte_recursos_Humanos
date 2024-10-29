import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargo archivo excel

ruta = r"C:\Users\kbm19\Desktop\Franco Cursos\Proyectos\Proyecto Recursos Humanos\Datos+Empleados.xlsx"
data = pd.ExcelFile(ruta)

# Creo 3 DataFrames con cada hoja dentro del archivo excel

empleados_df = data.parse('Tabla Empleados')
evaluacion_df = data.parse('Tabla Evaluacion')
sueldo_df = data.parse('Tabla Sueldo')

# Función para generar el resumen de cada DataFrame
def resumen_dataset(data, nombre_tabla):
    print(f"--- {nombre_tabla} ---")
    print("Primeras filas del dataset:")
    print(data.head(), "\n")
    
    print("Información del Dataset:")
    data.info()
    print("\n")
    
    print("Tamaño del dataset (filas, columnas):", data.shape)
    print("\n")
    
    print("Valores nulos en el dataset:")
    print(data.isnull().sum(), "\n")
    
    print("Resumen Estadístico de las variables numéricas:")
    print(data.describe(), "\n")

# Generar los resúmenes para las tres tablas
resumen_dataset(empleados_df, 'Tabla Empleados')
resumen_dataset(evaluacion_df, 'Tabla Evaluacion')
resumen_dataset(sueldo_df, 'Tabla Sueldo')

# --- Análisis y visualización ---

# 1. Conteo de empleados por departamento
conteo_departamento = empleados_df['Departamento'].value_counts()
print("Conteo de empleados por departamento:")
print(conteo_departamento)
print("\n")

plt.figure(figsize=(12, 6))
sns.countplot(data=empleados_df, x='Departamento', palette='viridis', order=empleados_df['Departamento'].value_counts().index)
plt.title('Distribución de Empleados por Departamento')
plt.xlabel('Departamento')
plt.ylabel('Cantidad de Empleados')
plt.xticks(rotation=45)
plt.show()

# 2. Resumen estadístico de sueldos por departamento
sueldo_departamento = sueldo_df.join(empleados_df.set_index('ID Empleado'), on='ID Empleado')
resumen_sueldo_departamento = sueldo_departamento.groupby('Departamento')['Sueldo'].describe()
print("Resumen estadístico de sueldos por departamento:")
print(resumen_sueldo_departamento)
print("\n")

# Gráfico de caja para sueldos por departamento
plt.figure(figsize=(12, 6))
sns.boxplot(data=sueldo_departamento, x='Departamento', y='Sueldo', palette='Set2')
plt.title('Distribución de Sueldos por Departamento')
plt.xlabel('Departamento')
plt.ylabel('Sueldo')
plt.xticks(rotation=45)
plt.show()

# 3. Promedio de sueldos por género
promedio_sueldo_genero = empleados_df.join(sueldo_df.set_index('ID Empleado'), on='ID Empleado').groupby('Género')['Sueldo'].mean()
print("Promedio de sueldos por género:")
print(promedio_sueldo_genero)
print("\n")

# Gráfico de barras para el promedio de sueldos por género
plt.figure(figsize=(10, 6))
sns.barplot(x=promedio_sueldo_genero.index, y=promedio_sueldo_genero.values, palette='Set1')
plt.title('Promedio de Sueldos por Género')
plt.xlabel('Género')
plt.ylabel('Promedio de Sueldo')
plt.show()

#  Promedio de evaluaciones de desempeño por departamento
evaluacion_departamento = evaluacion_df.join(empleados_df.set_index('ID Empleado'), on='ID Empleado')
promedio_evaluacion_departamento = evaluacion_departamento.groupby('Departamento')['Evaluación'].mean()
print("Promedio de evaluaciones de desempeño por departamento:")
print(promedio_evaluacion_departamento)
print("\n")

# Gráfico de barras para el promedio de evaluaciones por departamento
plt.figure(figsize=(12, 6))
sns.barplot(x=promedio_evaluacion_departamento.index, y=promedio_evaluacion_departamento.values, palette='Set2')
plt.title('Promedio de Evaluaciones de Desempeño por Departamento')
plt.xlabel('Departamento')
plt.ylabel('Promedio de Evaluación')
plt.xticks(rotation=45)
plt.show()


# Uno los DataFrames de evaluación y sueldo para este análisis
evaluacion_sueldo_df = pd.merge(evaluacion_df, sueldo_df, on='ID Empleado')

plt.figure(figsize=(10, 6))
sns.scatterplot(data=evaluacion_sueldo_df, x='Evaluación', y='Sueldo', alpha=0.7)
plt.title('Relación entre Evaluación de Desempeño y Sueldo')
plt.xlabel('Evaluación de Desempeño')
plt.ylabel('Sueldo')
plt.show()