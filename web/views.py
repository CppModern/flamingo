from django.http import HttpRequest
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from . import sender


@csrf_exempt
def send_mail(request: HttpRequest):
    if not request.method == "POST":
        return JsonResponse({"error": "method not allowed"})
    msg = "User Rervation Details:\n\n"
    data = request.POST
    items = ["email", "phone"]
    for item in items:
        info = data.get(item, "")
        msg += item + info + "\n"
    print("Sending email")
    sender.send_message(sender.service, settings.RECIPIENT, body=msg, obj="InFo")
    return JsonResponse({"msg": "OK"})


def index(request: HttpRequest):
    return render(request, "web/index.html")
