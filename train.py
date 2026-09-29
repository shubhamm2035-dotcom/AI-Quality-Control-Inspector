from ultralytics import YOLO

# 1. Load a pre-trained YOLOv8 model (using the 'nano' version which is fast and lightweight)
model = YOLO("yolov8n.pt")

# 2. Train the model on your custom dataset
print("Starting AI Training...")
results = model.train(
    data="data.yaml",           # Path to your dataset configuration file
    epochs=50,                  # How many times the AI will study the entire dataset
    imgsz=640,                  # Image resolution for training (standard is 640x640)
    batch=16,                   # Number of images the AI processes at the same time
    device="cpu",               # Use "0" instead of "cpu" if you have an NVIDIA GPU
    project="AI_Inspector",     # Main folder where results will be saved
    name="defect_detection_v1"  # Sub-folder for this specific training run
)

print("Training Complete! Check the 'AI_Inspector/defect_detection_v1/weights' folder for best.pt")
