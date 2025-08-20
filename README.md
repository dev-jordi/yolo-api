# 🚀 YOLO Object Detection API (com Docker)

Uma API simples de **detecção de objetos** usando **YOLOv5 + FastAPI**, empacotada em **Docker**.  
Você envia uma imagem → a API retorna as detecções (bounding boxes, classes e confiabilidade).

---

## ✨ Tecnologias usadas
- [Python 3.11](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [PyTorch](https://pytorch.org/)
- [YOLOv5](https://github.com/ultralytics/yolov5)
- [Docker](https://www.docker.com/)

---

## 📂 Estrutura do projeto

yolo-api/
│── app/
│ ├── main.py # Código da API
│ ├── requirements.txt # Dependências Python
│── Dockerfile # Imagem Docker
│── README.md # Este arquivo

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

#print

## 👨‍💻 Autor

Feito por Jordi