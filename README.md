🤖 VisionDetect — AI-Powered Computer Vision Web Application
<p align="center"> <img src="https://github.com/suriyaelumalai08/VisionDetect/blob/main/screenshorts/Home.png" width="100%"> </p> <p align="center">










</p>
# 📌 Overview

VisionDetect is a Flask-based AI web application that combines multiple Computer Vision and Deep Learning systems into a single platform.

The project provides:

* 🚗 Vehicle Image Classification
* 😀 Face Recognition System
* 🐶 Animal Image Classification
* 📦 YOLOv8 Object Detection

Users can upload images, detect objects, classify animals and vehicles, and perform AI-powered face recognition using Deep Learning models.

---

# 🚀 Main Features

## ✅ Multi AI Modules

| Module                 | Description                     |
| ---------------------- | ------------------------------- |
| Home                   | Landing page with AI navigation |
| Vehicle Classification | Vehicle prediction using CNN    |
| Face Recognition       | Real-time face detection        |
| Animal Classification  | Animal prediction system        |
| Object Detection       | YOLOv8 object detector          |

---

# 🛠️ Technologies Used

## Frontend

* HTML5
* CSS3
* JavaScript

## Backend

* Flask
* Python

## AI / Deep Learning

* TensorFlow
* Keras
* OpenCV
* YOLOv8
* CNN Models

---

# 📂 Project Structure

```bash
VisionDetect/
│
├── app.py
├── requirements.txt
│
├── models/
│   ├── animal_model.h5
│   ├── vehicle_model.h5
│   └── yolov8.pt
│
├── static/
│   ├── css/
│   ├── uploads/
│   └── images/
│
├── templates/
│   ├── home.html
│   ├── vehicle.html
│   ├── face.html
│   ├── animal.html
│   └── object.html
│
└── screenshorts/
    ├── Home.png
    ├── vehicle.png
    ├── face.png
    ├── animal.png
    └── object.png
```

---

# 🖼️ Application Outputs

# 🏠 Home Page

The landing page of the platform that connects all AI modules.

<p align="center">
  <img src="https://github.com/suriyaelumalai08/VisionDetect/blob/main/screenshorts/Home.png" width="100%">
</p>

🚗 Vehicle Image Classification

Deep Learning-based vehicle classification system.

Features
Upload vehicle image
CNN-based prediction
Multiple vehicle categories
<p align="center"> <img src="https://github.com/suriyaelumalai08/VisionDetect/blob/main/screenshorts/vehicle.png" width="100%"> </p>
😀 Face Recognition System

AI-powered real-time face recognition module.

Features
Webcam integration
Real-time face detection
Start / Stop controls
<p align="center"> <img src="https://github.com/suriyaelumalai08/VisionDetect/blob/main/screenshorts/face.png" width="100%"> </p>
🐶 Animal Image Classification

Animal classification using Deep Learning models.

Supported Animals
Dog
Horse
Elephant
Butterfly
Chicken
Cat
Cow
Sheep
Spider
Squirrel
<p align="center"> <img src="https://github.com/suriyaelumalai08/VisionDetect/blob/main/screenshorts/animal.png" width="100%"> </p>
📦 Object Detection System

YOLOv8-powered object detection module.

Features
Bounding box detection
Object labeling
Confidence score display
Multi-object detection
<p align="center"> <img src="https://github.com/suriyaelumalai08/VisionDetect/blob/main/screenshorts/object.png" width="100%"> </p>
⚙️ Installation
1️⃣ Clone Repository
git clone https://github.com/suriyaelumalai08/VisionDetect.git
2️⃣ Move into Project Folder
cd VisionDetect
3️⃣ Install Dependencies
pip install -r requirements.txt

Or manually install:

pip install flask tensorflow opencv-python ultralytics numpy pillow
▶️ Run the Application
python app.py

Open browser:

http://127.0.0.1:5000
🧠 AI Models Used
Model	Purpose
CNN	Vehicle Classification
CNN	Animal Classification
OpenCV	Face Detection
YOLOv8	Object Detection
🎨 UI Design

The application includes:

Minimal modern design
Large typography
Custom CSS styling
Clean navigation system
Responsive layout
📈 Future Improvements

The project looks visually impressive for a portfolio project, but technically it can still be improved.

Recommended Improvements
Add database support
Add authentication system
Improve model optimization
Add API-based architecture
Add Docker deployment
Improve mobile responsiveness
Add real-time tracking
Deploy on cloud platform

Right now it is a strong portfolio/demo project, not a production-ready SaaS application.

📚 Learning Outcomes

This project demonstrates practical implementation of:

Deep Learning
CNN Models
YOLOv8
OpenCV
Flask Development
Computer Vision
Frontend + Backend Integration
AI Web Applications
👨‍💻 Author
Suriya Elumalai

BCA Graduate | AI & Machine Learning Enthusiast

Skills
Python
Machine Learning
Deep Learning
Computer Vision
Flask
FastAPI
NLP Basics

🔗 GitHub
https://github.com/suriyaelumalai08

📄 License

This project is created for educational and portfolio purposes.
