# 🚀 YOLO Object Detection API (com Docker)

Uma API simples de **detecção de objetos** usando **YOLOv5 + FastAPI**, empacotada em **Docker**.  
Você envia uma imagem → a API retorna as detecções (bounding boxes, classes e confiabilidade).

## ✨ Tecnologias usadas
[![Python 3.11](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-✨-green?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![PyTorch](https://img.shields.io/badge/PyTorch-🔥-red?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![YOLOv5](https://img.shields.io/badge/YOLOv5-🚀-orange?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ultralytics/yolov5)
[![Docker](https://img.shields.io/badge/Docker-🐳-blue?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)

## ⚡ Como rodar o projeto

### 1. Clonar repositório
```bash
git clone https://github.com/seu-usuario/yolo-api.git
cd yolo-api
```

## 2 Construir a imagem Docker

```bash
docker build -t yolo-api .
```

## 3. Rodar o container

```bash
docker run -p 8000:8000 yolo-api
```

A API ficará disponível em:
👉 http://localhost:8000/docs

Resposta:

```bash
{
  "detections": [
    {
      "xmin": 50.3,
      "ymin": 100.1,
      "xmax": 200.4,
      "ymax": 300.2,
      "confidence": 0.87,
      "class": 0,
      "name": "person"
    }
  ]
}
```

## 📸 Exemplo de detecção

#print1

#print2
