# HELMET DETECTION

This project is a simple implementation of a helmet detection system using OpenCV and YOLOv3.

## Usage

To use this project, you need to have all dependencies installed. Conda is recommended for this purpose. You can install all dependencies using the following command:

```bash
cd yolov10
pip install -r requirements.txt
pip install -e .
```

After installing the dependencies, you can run streamlit app in the root directory of the project using the following command:

```bash
streamlit run app.py
```

Currently the app only support images. You can upload an image and the app will detect helmets in the image.
