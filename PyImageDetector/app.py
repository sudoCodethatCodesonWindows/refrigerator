import cv2
from ultralytics import YOLO

def run_headless_detection(input_path, output_path, model_version="yolo11l.pt"):
    # 1. Load the model (yolov11m is the 'medium' version for ~80%+ accuracy)
    # It will automatically download the weights on the first run
    model = YOLO(model_version)

    # 2. Run Inference
    # imgsz=640 is standard; conf=0.80 ensures we only keep high-confidence detections
    results = model.predict(source=input_path, conf=0.80, imgsz=640, verbose=False)

    # 3. Process Results
    result = results[0]  # We are processing a single image
    
    # Logic: Print what we found to the console
    if len(result.boxes) == 0:
        print(f"No objects detected with >80% confidence in {input_path}")
    else:
        print(f"Detected {len(result.boxes)} objects:")
        for box in result.boxes:
            class_id = int(box.cls[0])
            label = result.names[class_id]
            conf = float(box.conf[0])
            print(f" - {label}: {conf:.2%}")

    # 4. Save the Output Image (Headless saving)
    # result.plot() creates an image with boxes and labels already "burned" in
    annotated_image = result.plot()
    cv2.imwrite(output_path, annotated_image)
    print(f"Output saved to: {output_path}")

if __name__ == "__main__":
    run_headless_detection("download.jpeg", "detected_output.jpg")
