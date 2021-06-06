from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Tasks
from .serializers import TaskSerializer
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
# Create your views here.

def home(request):

    return render(request,'tasks\home.html')

@api_view(['GET','POST'])
def tasks(request):
    if request.method == 'GET':
        dt = Tasks.objects.all()
        serializ = TaskSerializer(dt,many=True)
        return JsonResponse(serializ.data,safe=False,status=200)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)

   
@api_view(['GET','PUT','DELETE'])
def task_details(request,pk):
    dt= get_object_or_404(Tasks, pk=pk)
    if request.method == 'GET':
        serializ = TaskSerializer(dt)
        return JsonResponse(serializ.data)

    elif request.method == 'PUT':
        data= JSONParser().parse(request)
        serializ = TaskSerializer(dt, data=data)
        if serializ.is_valid():
            serializ.save()
            return JsonResponse(serializ.data,status=200)
        return JsonResponse(serializ.errors,status=400)

    elif request.method == 'DELETE':
        dt.delete()
        return JsonResponse({'response':'Deleted successfully'},status=status.HTTP_204_NO_CONTENT)
    

        
    