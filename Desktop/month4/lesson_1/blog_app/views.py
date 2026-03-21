from django.shortcuts import render
#Класс HttResponse - для одиночного запроса 
from django.http import HttpResponse

def hello_view(req):
    if req.method == "GET":
        return HttpResponse('Hello World')
    
def emodji(req):
    if req.method == "GET":
        return HttpResponse("😅🤪😏🫢🤠")

def pic(req):
    if req.method == "GET":
        return HttpResponse('<img src="https://theportablewife.com/wp-content/uploads/best-places-to-take-pictures-in-paris-newfeatured.jpg" alt="альтернативный текст">')
    
    

