from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
import os
import numpy as np  # pip install numpy
import cv2  # pip install opencv-python
from keras.models import load_model  # pip install tensorflow
#######################################################################
# Create your views here.


def predictTomatoDisease(request):
    if request.method == 'POST' and request.FILES['img']:
        img = request.FILES['img']
        img_path = os.path.join(os.getcwd(), 'app_predict', 'images',
                                img.name)    # image name path
        fss = FileSystemStorage()
        file = fss.save(img_path, img)

        # constant
        IMG_SIZE = 250

        img_arr = cv2.imread(img_path)
        img_arr = cv2.resize(img_arr, (IMG_SIZE, IMG_SIZE))

        test_data = [img_arr]
        test_data = np.array(test_data)
        test_data = test_data/255

        os.remove(img_path)

        plantName = request.POST.get('plantName')

        if(plantName == "tomato"):
            finalResult = tomato(test_data)
        elif(plantName == "rice"):
            finalResult = rice(test_data)
        else:
            return HttpResponse("Invalid Request")

        return JsonResponse(finalResult)
    else:
        return HttpResponse("Invalid Request")


def tomato(test_data):
    #print("########### Tomato ###########")
    model_path = os.path.join(
        os.getcwd(), 'app_predict', 'models', 'tomato.h5')  # model name path

    model = load_model(model_path)

    result = model.predict(test_data)
    result = result[0].tolist()

    max_value = max(result)
    max_index = result.index(max_value)

    # print("result => ", result)
    # print("Max value => ", max_value)
    # print("Max Index", max_index)

    dic = {
        0: {
            "plant": "Tomato",
            "accuracy": max_value,
            "Status": "Bacterial Spot",
            "details": "will be added"},
        1:  {
            "plant": "Tomato",
            "accuracy": max_value,
            "Status": "Early Blight",
            "details": "will be added"},
        2:  {
            "plant": "Tomato",
            "accuracy": max_value,
            "Status": "Healthy",
            "details": "will be added"},
        3:  {
            "plant": "Tomato",
            "accuracy": max_value,
            "Status": "Late Blight",
            "details": "will be added"},
        4:  {
            "plant": "Tomato",
            "accuracy": max_value,
            "Status": "Leaf Mold",
            "details": "will be added"},
        5:  {
            "plant": "Tomato",
            "accuracy": max_value,
            "Status": "Septoria Leaf Spot",
            "details": "will be added"},
        6:  {
            "plant": "Tomato",
            "accuracy": max_value,
            "Status": "Spider Mites Two-Spotted Spider Mite",
            "details": "will be added"},
        7:  {
            "plant": "Tomato",
            "accuracy": max_value,
            "Status": "Target Spot",
            "details": "will be added"},
        8:  {
            "plant": "Tomato",
            "accuracy": max_value,
            "Status": "Tomato Mosaic Virus",
            "details": "will be added"},
        9:  {
            "plant": "Tomato",
            "accuracy": max_value,
            "Status": "Tomato Yellow Leaf Cyrl Virus",
            "details": "will be added"},
    }

    return (dic[max_index])


def rice(test_data):
    #print("########### Rice ###########")
    model_path = os.path.join(
        os.getcwd(), 'app_predict', 'models', 'rice.h5')  # model name path

    model = load_model(model_path)

    result = model.predict(test_data)
    result = result[0].tolist()

    max_value = max(result)
    max_index = result.index(max_value)

    # print("result => ", result)
    # print("Max value => ", max_value)
    # print("Max Index", max_index)

    dic = {
        0: {
            "plant": "Rice",
            "accuracy": max_value,
            "Status": "Brown Spot",
            "details": "will be added"},
        1:  {
            "plant": "Rice",
            "accuracy": max_value,
            "Status": "Healthy",
            "details": "will be added"},
        2:  {
            "plant": "Rice",
            "accuracy": max_value,
            "Status": "Hispa",
            "details": "will be added"},
        3:  {
            "plant": "Rice",
            "accuracy": max_value,
            "Status": "Leaf Blast",
            "details": "will be added"},
    }

    return (dic[max_index])
