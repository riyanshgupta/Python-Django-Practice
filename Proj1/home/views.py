
from email.mime import image
from tkinter import image_names
from django.shortcuts import render, HttpResponse
import qrcode, cv2
from .models import Destination 
# Create your views here.
def index(request):
    cond = 'False'
    msg = False
    #return HttpResponse("This is my homepage.")
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.id = 21312
    dest1.desc = "Mumbai nevers sleeps."
    dest1.price = 700
    dest1.img = 'Mumbai.jpg'
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Hyderabad'
    dest2.id = 21313
    dest2.desc = "Biryani comes before Shervani"
    dest2.price = 650
    dest2.img = 'Hyderabad.jpg'
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'Bangalore'
    dest3.id = 21314
    dest3.desc = "Silicon valley of Asia"
    dest3.price = 750
    dest3.img = 'bangalore.jpg'
    dest3.offer = False
    
    dests = [dest1, dest2, dest3]
    return render(request, 'T1 .html',{'dests' : dests, 'name':name, 'surname':"Gupta", 'cond': cond, 'msg':msg})

def about(request):
    return HttpResponse("This is my about page.")

def sum(request):
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    res = val1+val2
    return render(request, 'result.html', {'result': res})

def qrgen(request):
    data = request.GET['data']
    img = qrcode.make(data)
    img.save("static/qrcode.jpg")
    img1 = cv2.imread("static/qrcode.jpg")
    return render(request, 'qr.html', {'image': img1})

# python programming
name = "Riyansh"
dic = {'name':name, 'surname':"Gupta"}