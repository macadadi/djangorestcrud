from django.shortcuts import  render,get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .models import Tasks
from .serializers import TaskSerializer



def home(request):
    
    return render(request,'tasks\home.html')


@api_view(['GET','POST'])
def tasks(request):
    if request.method == 'GET':
        dt = Tasks.objects.all()
        serializer = TaskSerializer(dt,many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method == 'POST':
        dt = JSONParser().parse(request)
        serializer = TaskSerializer(data=dt)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)


@api_view(['GET','PUT','DELETE'])
def task_details(request,pk):
    obj= get_object_or_404(Tasks,pk=pk)
    if request.method == 'GET':
        serializer = TaskSerializer(obj)
        return JsonResponse(serializer.data,status=400)

    elif request.method == 'PUT':
        dt = JSONParser().parse(request)
        serializer = TaskSerializer(obj,data=dt)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=200)
        return JsonResponse(serializer.errors,status=400)

    elif request.method == 'DELETE':
        obj.delete()
        return JsonResponse({'response':'object was successfully deleted'})
        
        
        