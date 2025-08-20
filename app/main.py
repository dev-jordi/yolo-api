from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import torch
import shutil
import os
from PIL import Image

app = FastAPI(title="YOLO Object Detection API")

# Carregar modelo YOLO (pré-treinado no COCO)
MODEL_PATH = "yolov5s.pt"
model = torch.hub.load("ultralytics/yolov5", "custom", path=MODEL_PATH)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Salvar imagem temporária
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Rodar detecção
    results = model(temp_path)

    # Converter resultados
    detections = results.pandas().xyxy[0].to_dict(orient="records")

    # Apagar arquivo temporário
    os.remove(temp_path)

    return JSONResponse(content={"detections": detections})
