import os
from ultralytics import YOLO
import cv2

MODEL = None

def init_model(model_name='yolov8n.pt'):
    global MODEL
    if MODEL is None:
        MODEL = YOLO(model_name)
    return MODEL

def detect_dogs(image_path, output_path=None, conf=0.25):
    model = init_model()
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Image not found: {image_path}")

    results = model(img, conf=conf)
    dog_count = 0

    for r in results:
        boxes = r.boxes
        for box in boxes:
            cls = int(box.cls[0])
            label = model.names[cls]
            if label == 'dog':
                dog_count += 1
                x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(img, 'Dog', (x1, y1-8), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

    if output_path:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        cv2.imwrite(output_path, img)

    return dog_count
