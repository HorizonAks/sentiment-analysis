#!/usr/bin/env python
# coding: utf-8

# In[4]:


import asyncio
import io
import glob
import os
import sys
import time
import uuid
import requests
#import cv2
from urllib.parse import urlparse
from io import BytesIO
# To install this module, run:
# python -m pip install Pillow
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, QualityForRecognition, FaceAttributeType


# In[5]:


# This key will serve all examples in this document.
KEY = "ef60ee33acab4852a6b8ad758f2cc04a"

# This endpoint will be used in all examples in this quickstart.
ENDPOINT = "https://sentiment-analyser-01.cognitiveservices.azure.com/"


# In[6]:


# Create an authenticated FaceClient.
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))


# In[ ]:


#define face attribute
e1 = [FaceAttributeType("emotion")]


# In[30]:


def getsentiment(frame):
    detected_faces = face_client.face.detect_with_stream(frame, detection_model='detection_01',return_face_attributes=e1)
    #face_client.face.detect_with_stream()
    if not detected_faces:
        return None
    for face in detected_faces: 
        #return 1 face sentiments
        #TODO - fix
        sentiments = face.face_attributes.emotion.as_dict()
        return max(sentiments, key= lambda x: sentiments[x])

