from django.shortcuts import redirect, render  
from ImageAnalyser.forms import UserImageForm  
from .models import UploadImage  
from . import backend
import os
  
def image_request(request):  
    if request.method == 'POST':  
        form = UserImageForm(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()  
  
            # Getting the current instance object to display in the template  
            img_object = form.instance  
            img_url = os. getcwd()+img_object.image.url
            frame = open(os. getcwd()+img_object.image.url,"r+b")
            sentiment = backend.getsentiment(frame)
            print("Reply from Backend",sentiment)
            return render(request, 'image_form.html', {'form': form, 'img_obj': img_object, 'Sentiment':sentiment})  
    else:  
        form = UserImageForm()  
  
    return render(request, 'image_form.html', {'form': form})  