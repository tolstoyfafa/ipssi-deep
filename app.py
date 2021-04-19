import os
import string
import random
import json
import requests
import numpy as np
import tensorflow as tf

from flask import Flask, request, render_template

app = Flask(__name__)

"""
Utility functions
"""


def generate_filename():
    return ''.join(random.choices(string.ascii_lowercase, k=20)) + '.jpg'


def get_prediction(image_path):
    image = tf.keras.preprocessing.image.load_img(
        image_path, target_size=(SIZE, SIZE))
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = tf.keras.applications.mobilenet_v2.preprocess_input(image)
    image = np.expand_dims(image, axis=0)

    data = json.dumps({'instances': image.tolist()})
    response = requests.post(MODEL_URI, data=data.encode())
    result = json.loads(response.text)
    print(result)
    prediction = result['predictions'][0]
    class_name = CLASSES[int(prediction[0] > 0.5)]
    return class_name


"""
Constants
"""
MODEL_URI = 'http://localhost:8502/v1/models/horse-vs-human:predict'
OUTPUT_DIR = 'static/uploaded_images'
CLASSES = ['Horse', 'Human']
SIZE = 300


"""
Routes
"""


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # If the request method is POST we know an image file is uploaded
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            # If the file name is not blank we do the prediction
            # It it's blank it means the button was pressed but no image was uploaded
            # Check if the extension of the file is correct (png, jpg)
            # Save the image in the static folder before passing it to the model
            # Copying the images in the folder will allow us to show the image along with the prediction

            if uploaded_file.filename[-3:] in ['jpg', 'png']:
                image_path = os.path.join(OUTPUT_DIR, generate_filename())
                print(
                    "#################################################################################")
                print(image_path)
                uploaded_file.save(image_path)
                class_name = get_prediction(image_path)
                result = {
                    'class_name': class_name,
                    'image_path': image_path,
                    'size': SIZE
                }
                return render_template('show.html', result=result)
            else:
                erreur = "Veuillez deposer une image au format PNG ou JPG"
                return render_template('index.html', erreur=erreur)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
