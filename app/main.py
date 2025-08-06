from flask import Flask , request, jsonify

from torch_utils import transform_image , get_prediction 

app = Flask(__name__)

allowed_extenstions = {'png', 'jpg', 'jpeg'}
def allowed_file(filename):
    
    return '.'in filename and filename.rsplit('.',1)[1].lower() in allowed_extenstions

@app.route('/predict', methods = ['POST'])
def predict():
    if request.method == 'POST':
        file = request.files.get('file')
        if file is None or file.filename == "":
            return jsonify({'error':'No file'})
        if not allowed_file(file.filename):
            return jsonify({'error':'format not supported'})
        
        try:
            img_bytes = file.read()
            tensor = transform_image(img_bytes)
            predict = get_prediction(tensor)
            data = {'prediction':predict, 'class_name': str(predict)}
            return jsonify(data)
                    
        except:
            return jsonify({'error':'error during prediction'})