FROM python:3.11-slim

# Instalar dependências de sistema necessárias para o OpenCV e PyTorch
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# instalar YOLOv5 via pip
RUN pip install yolov5

COPY app/ .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
