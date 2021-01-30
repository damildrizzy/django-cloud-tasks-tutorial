import time
from django.shortcuts import render
from django.http import JsonResponse
from .cloud_tasks import send_task


# Create your views here.

def task_view(request):
    payload = request.body.decode('utf-8')
    time.sleep(60)
    print(f"{payload} is completed")

    #perform some task with payload


def create_task(request):
    task = "Test Task"
    send_task(url="_/task/", payload=task)
    return JsonResponse({'message': "task started"})
