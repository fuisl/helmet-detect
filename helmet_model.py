"""
Model for helmet detection fine-tuned from YOLOv10
"""
import sys
from pathlib import Path

# Assuming your current script is in the same directory as the yolov10 directory
yolov10_dir = Path(__file__).resolve().parent / 'yolov10'
sys.path.append(str(yolov10_dir))

from ultralytics import YOLOv10

class HelmetModel:
    def __init__(self, weights_path):
        self.model = YOLOv10(weights_path)

    def predict(self, image):
        return self.model(image)
    

if __name__ == '__main__':
    model = HelmetModel('best.pt')
    results = model.predict()
    results.show()