# DEPLOY MACHINE LEARNING MODELS
Project ini digunakan untuk mendeteksi RPS (Rock, Paper, Scissors) untuk mengklasifikasi citra gestur tangan individu pada permaian batu, kertas, gunting.

Link Dataset yang digunakan : https://drive.google.com/file/d/1T4BGxhHm7JXYm4XHaUPP-zZkbTwgC8LK/view?usp=drive_link

Menggunakan Tranfer Learning pada klasifikasi citra gestur tangan dengan model VGG19

# Overview Dataset
Link dataset yang digunakan : https://drive.google.com/file/d/1T4BGxhHm7JXYm4XHaUPP-zZkbTwgC8LK/view?usp=drive_link
Gambar yang digunakan dalah citra gestur tangan pada permaian batu, kertas, gunting dengan total gambar 2520 Terdiri dari 840 gambar gestur tangan batu, 840 gambar gestur tangan kertas, dan 840 gambar gestur tangan gunting

Splitting Dataset : Training : 70% , Validation = 25% , Testing = 5%

# Preprocessing dan Modelling
Preprocessing Model :  rescale=1./255, rotation_range=30, zoom_range=0.2, Horizontal_flip=True, fill_mode='nearest'

Modelling model VGG19
summary model VGG19

<img width="400" alt="2" src="https://github.com/nurissabila/Deploy-Machine-Learning-Models/assets/71714312/ec42919c-60f7-4742-8eb4-7e988ce33cbb">


Graph Loss dan Accuracy 

![11](https://github.com/nurissabila/Deploy-Machine-Learning-Models/assets/71714312/a75762be-1598-4a6f-85f5-8509044d3e7e)

![12](https://github.com/nurissabila/Deploy-Machine-Learning-Models/assets/71714312/9a0b3ec9-59bd-4f0d-a6ea-d8c3394b53ff)

Evaluation Matrix

<img width="500" alt="3" src="https://github.com/nurissabila/Deploy-Machine-Learning-Models/assets/71714312/ce62fdcd-1dee-42b0-9c67-0a253650ecbe">


# Predict Data
Predict Data dengan Model VGG19
![download](https://github.com/nurissabila/Deploy-Machine-Learning-Models/assets/71714312/598f9a69-37e5-4a92-8b16-21b72629351d)


# Local Development
<img width="904" alt="image" src="https://github.com/nurissabila/Deploy-Machine-Learning-Models-RPS/assets/71714312/fa59741c-0f77-4cb1-be57-82be02ab90e8">



<img width="904" alt="image" src="https://github.com/nurissabila/Deploy-Machine-Learning-Models-RPS/assets/71714312/09e22fe5-c385-4bb0-846d-7bb93ea55c7a">




