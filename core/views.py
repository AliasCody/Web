from django.http import JsonResponse
from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')


def comments_api(request):
    data = {
        "comments":[
            {"author": "Alice","content":"First Messege"},
            {"author": "Bob","content":"Hello Django+Dom"},
        ]
    }

    return JsonResponse(data)