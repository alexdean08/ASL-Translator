from tensorflow import keras
from time import sleep
import cv2
import numpy as np

model = keras.models.load_model('model.h5')
webcam = cv2.VideoCapture(0)

while(True):

    if cv2.waitKey(1) >= 0:
        break

    img = webcam.read()[1]/255.0
    cv2.imshow('video', img)

    sleep(0.5)
    img_size = 100

    if img.shape[0] > img.shape[1]:
      sq_size = img.shape[0] - img.shape[1]
      img = img[int(sq_size/2):img.shape[0]-int(sq_size/2), 0:img.shape[1]]
    else:
      sq_size = img.shape[1] - img.shape[0]
      img = img[0:int(img.shape[0]), int(sq_size/2):int(img.shape[1])-int(sq_size/2)]

    img_resized = cv2.resize(img, (img_size, img_size))

    img_resized = np.asarray(img_resized.reshape(-1, img_size, img_size, 1))
    prediction = model.predict([img_resized])[0]

    i = -1
    max_val = 0
    max_index = 0
    for num in prediction:
      i+=1
      if num > max_val:
        max_val = num
        max_index = i

    if max_index != 26:
        print(chr(65+max_index))
    else:
        print('Blank')
