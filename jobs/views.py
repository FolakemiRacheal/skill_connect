from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Job
from .serializers import JobSerializer

@api_view(['GET','POST'])
def jobs_view(request):
    if request.method == 'GET':
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = JobSerializer(data =request.data)
        if serializer.is_valid():
            serializer.save(client=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.data, status=404)
    
    @api_view(['GET'])
    @permission_classes([IsAuthenticated])
    def get_job(request, id):
        try:
            job = Job.objects.get(pk=id)
        except Job.DoesNotExist:
            return Response({'error':'Job not found'}, status=404)
        
        serializer = JobSerializer(job)
        return Response(serializer.data)