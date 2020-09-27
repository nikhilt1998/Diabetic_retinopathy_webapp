from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from keras.preprocessing import image
import cv2
import os
import numpy as np
import tensorflow as tf
from keras.models import load_model
from tensorflow import keras
global graph, model
import warnings
warnings.filterwarnings("ignore")

from django.core.files.storage import FileSystemStorage

print("Keras model loading.......")
model = load_model('dr_classification/models/model.h5')
print("Model loaded!!")

#creating a dictionary of classes
class_dict = {'No DR': 0,
            'Mild': 1,
            'Moderate': 2,
            'Severe': 3,
            'Proliferative DR': 4,
            }

class_names = list(class_dict.keys())

def prediction(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        SIZE = 300
        path = os.path.join('media',filename) 
        image = cv2.imread(path)
        image = cv2.resize(image, (SIZE, SIZE))
        X = np.array((image[np.newaxis])/255)
        score_predict=((model.predict(X).ravel()*model.predict(X[:, ::-1, :, :]).ravel()*model.predict(X[:, ::-1, ::-1, :]).ravel()*model.predict(X[:, :, ::-1, :]).ravel())**0.25).tolist()
        label_predict = np.argmax(score_predict)
        result = class_names[label_predict]
        return render(request, "dr_classification/prediction_result.html", {'result': result})
    else:
        return render(request, "dr_classification/prediction.html")
