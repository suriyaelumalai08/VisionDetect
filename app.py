
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from flask import Flask, render_template, url_for, request, jsonify
from tensorflow.keras.models import load_model
from werkzeug.utils import secure_filename
import numpy as np
import base64
import cv2
import os

try:
    from ultralytics import YOLO
except ImportError:
    YOLO = None




app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

VEHICLE_MODEL_PATH = "vehicle_model.h5"
ANIMAL_MODEL_PATH = "Animal.h5"
OBJECT_MODEL_PATH = "yolov8n.pt"
IMAGE_SIZE = (150, 150)

VEHICLE_CLASS_NAMES = [
    'airplane', 'ambulance', 'bicycle', 'bike', 'boat',
    'bus', 'car', 'fire_truck', 'helicopter', 'hovercraft',
    'jet_ski', 'kayak', 'rickshaw', 'scooter', 'segway',
    'skateboard', 'tractor', 'truck', 'unicycle', 'van'
]

ANIMAL_CLASS_NAMES = [
    'Dog', 'Horse', 'Elephant', 'Butterfly', 'Chicken',
    'Cat', 'Cow', 'Sheep', 'Spider', 'Squirrel'
]

vehicle_model = load_model(VEHICLE_MODEL_PATH)
animal_model = load_model(ANIMAL_MODEL_PATH)
object_model = None


def prepare_image(image_path):
    img = load_img(image_path, target_size=IMAGE_SIZE)
    img_array = img_to_array(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


def predict_uploaded_image(uploaded_file, model, class_names, prefix):
    if not uploaded_file or uploaded_file.filename == '':
        return None, None, None

    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    filename = secure_filename(uploaded_file.filename)
    filename = f"{prefix}_{filename}"
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    uploaded_file.save(image_path)

    image_array = prepare_image(image_path)
    result = model.predict(image_array)
    predicted_index = int(np.argmax(result[0]))

    prediction = class_names[predicted_index]
    confidence = round(float(np.max(result[0])) * 100, 2)
    uploaded_image = url_for('static', filename=f'uploads/{filename}')

    return prediction, confidence, uploaded_image


def get_object_model():
    global object_model

    if YOLO is None:
        return None

    if object_model is None:
        object_model = YOLO(OBJECT_MODEL_PATH)

    return object_model


def detect_uploaded_objects(uploaded_file):
    if YOLO is None:
        return None, None, [], "Please install ultralytics to use YOLO object detection."

    if not uploaded_file or uploaded_file.filename == '':
        return None, None, [], None

    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    filename = secure_filename(uploaded_file.filename)
    filename = f"object_{filename}"
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    uploaded_file.save(image_path)

    model = get_object_model()
    if model is None:
        return None, None, [], "YOLO model could not be loaded."

    results = model(image_path)
    result = results[0]
    annotated_image = result.plot()

    detected_filename = f"detected_{filename}"
    detected_path = os.path.join(app.config['UPLOAD_FOLDER'], detected_filename)
    cv2.imwrite(detected_path, annotated_image)

    detections = []
    names = result.names

    for box in result.boxes:
        class_id = int(box.cls[0])
        detections.append({
            "name": names[class_id],
            "confidence": round(float(box.conf[0]) * 100, 2)
        })

    uploaded_image = url_for('static', filename=f'uploads/{filename}')
    detected_image = url_for('static', filename=f'uploads/{detected_filename}')

    return uploaded_image, detected_image, detections, None


@app.route('/')
@app.route('/home')
def home():
    return render_template('Home.html')


@app.route('/vehical', methods=['GET', 'POST'])
def vehical():
    prediction = None
    confidence = None
    uploaded_image = None

    if request.method == "POST":

        uploaded_file = request.files.get("image")

        prediction, confidence, uploaded_image = predict_uploaded_image(
            uploaded_file,
            vehicle_model,
            VEHICLE_CLASS_NAMES,
            'vehicle'
        )
        print(f'predicted:{prediction},confidence score:{confidence}')

    return render_template(
        'vehical.html',
        prediction=prediction,
        confidence=confidence,
        uploaded_image=uploaded_image
    )








def detect_faces(frame):
    #face detection d face detector only one time
    face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=4,
        minSize=(40, 40)
    )

    boxes = []

    for (x, y, w, h) in faces:
        boxes.append({
            "x": int(x),
            "y": int(y),
            "w": int(w),
            "h": int(h),
            "name": "Face"
        })

    print("Detected boxes:", boxes)

    return boxes


@app.route("/face")
def face():
    return render_template("face.html")


@app.route("/detect", methods=["POST"])
def detect():
    data = request.get_json()

    if not data or "image" not in data:
        return jsonify({
            "boxes": [],
            "error": "No image received"
        })

    image_data = data["image"]

    if "," in image_data:
        image_data = image_data.split(",")[1]

    image_bytes = base64.b64decode(image_data)
    np_arr = np.frombuffer(image_bytes, np.uint8)

    frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    if frame is None:
        return jsonify({
            "boxes": [],
            "error": "Frame decode failed"
        })

    boxes = detect_faces(frame)

    return jsonify({
        "boxes": boxes
    })


# Animal  classifier

@app.route("/animal", methods=['GET', 'POST'])
def animal():
    prediction = None
    confidence = None
    uploaded_image = None

    if request.method == "POST":
        uploaded_file = request.files.get("image")

        prediction, confidence, uploaded_image = predict_uploaded_image(
            uploaded_file,
            animal_model,
            ANIMAL_CLASS_NAMES,
            'animal'
        )
        print(f'animal predicted:{prediction},confidence score:{confidence}')

    return render_template(
        'animal.html',
        prediction=prediction,
        confidence=confidence,
        uploaded_image=uploaded_image
    )


@app.route("/object", methods=['GET', 'POST'])
def object_detection():
    uploaded_image = None
    detected_image = None
    detections = []
    error = None

    if request.method == "POST":
        uploaded_file = request.files.get("image")
        uploaded_image, detected_image, detections, error = detect_uploaded_objects(uploaded_file)

    return render_template(
        'object.html',
        uploaded_image=uploaded_image,
        detected_image=detected_image,
        detections=detections,
        error=error
    )





if __name__=="__main__":
    app.run(debug=True)
