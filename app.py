from flask import Flask, request, render_template, redirect, url_for, send_file
from ultralytics import YOLO
import os
from PIL import Image
import numpy as np
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
model = YOLO(r'D:\DEVANSH COLLEGE\Btech 7th Sem\New folder\Defect Detection.v6i.yolov8\runs\detect\train\weights\best.pt')
@app.route('/')
def index():
    return render_template('upload.html')
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']    
    if file.filename == '':
        return redirect(request.url)
    if file:
        uploaded_path = os.path.join(app.config['UPLOAD_FOLDER'], 'uploaded_image.jpg')
        file.save(uploaded_path)
        results = model.predict(uploaded_path)
        result_path = os.path.join(app.config['UPLOAD_FOLDER'], 'result_image.jpg')
        for result in results:
            img_with_annotations = result.plot() 
            if isinstance(img_with_annotations, np.ndarray):
                img_with_annotations = Image.fromarray(img_with_annotations)
            img_with_annotations.save(result_path)
        return render_template('result.html', uploaded_image='uploaded_image.jpg', result_image='result_image.jpg')
@app.route('/display/<filename>')
def display_image(filename):
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), mimetype='image/jpeg')
if __name__ == '__main__':
    app.run(debug=True)
