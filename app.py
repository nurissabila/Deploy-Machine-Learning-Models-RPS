from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import time

app = Flask(__name__)

dic = {0 : 'Paper', 1 : 'Rock', 2 : 'Scissors'}

model = load_model('D:\SMT 7\Pembelajaran Mesin\Modul\Modul 6 - AI Web Model Deployment-20230919T140103Z-001\Modul 6 - AI Web Model Deployment\PraktikumModul6\modeldataimage.h5')


@app.route("/", methods=['GET'])
def main():
	return render_template("index.html")

@app.route("/submit", methods = ['POST'])
def get_output():
	start_time = time.time()
	img = request.files['my_image']
	img_path = "static/" + img.filename	
	img.save(img_path)
	img_array = image.img_to_array(image.load_img(img_path, target_size=(128, 128))) / 255.0
	img_array = img_array.reshape(1,128, 128,3)
	p = model.predict(img_array)
	predicted_class = np.argmax(p)
	prediction = dic[predicted_class]
	confidence = np.round(float(p[0][predicted_class])*100,2)
	end_time = time.time()
	runtime = round(end_time - start_time, 4)
	return render_template("result.html", prediction = prediction,  img_path = img_path, runtime=runtime, confidence=confidence)

	
if __name__ =='__main__':
	app.run(debug = True)
