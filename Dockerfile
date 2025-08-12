# Usa una imagen base de Python oficial
FROM python:3.10-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los requerimientos e instálalos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de tu aplicación al contenedor
COPY main.py .

# Expone el puerto en el que se ejecutará la API
EXPOSE 8000

# Comando para iniciar el servidor Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
