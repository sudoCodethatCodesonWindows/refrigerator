import numpy as np
from ultralytics import YOLO
import cv2
import requests
from PIL import Image
from io import BytesIO

# Load YOLOv8 pretrained model
model = YOLO("yolov8n.pt")  # nano = fast, accurate enough

def load_image(source):
    if source.startswith("http"):
        response = requests.get(source)
        img = Image.open(BytesIO(response.content))
        return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    else:
        return cv2.imread(source)

def detect_objects(image_source):
    image = load_image(image_source)

    results = model(image)

    for result in results:
        for box in result.boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            label = f"{model.names[cls]} {conf*100:.2f}%"

            # Draw box
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(image, label, (x1, y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imwrite("output.jpg", image)
print("Saved result as output.jpg")

# 🔹 Example usage:
detect_objects("https://ultralytics.com/images/bus.jpg")
# OR
# detect_objects("myimage.jpg")
