from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project, Pledge
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer
from django.http import Http404
from rest_framework import status

# Create your views here.

class ProjectList(APIView):

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    # def get_queryset(self):
    #     projects = Project.objects.all()
    #     return projects

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.save()
            serializer.save(owner=request.user)
            # return Response(serializer.data)
            return Response(
                serializer.data, 
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class ProjectDetail(APIView):

    def get_object(self, pk):
        # return Project.objects.get(pk=pk) 
        try: 
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        project = self.get_object(pk) 
        # serializer = ProjectSerializer(project)
        serializer = ProjectDetailSerializer(project)        
        return Response(serializer.data)
    
    
class PledgeList(APIView):

    def get(self, request):
        pledges = Pledge.objects.all()
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = PledgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # return Response(serializer.data)
            return Response(
                serializer.data, 
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

# Inherit from class ProjectLIst to return a count of total project, total pledges and $ amount of pledges
class ProjectStatistics(ProjectList):

    def statistics(self,request):
        # projects = self.get_queryset()

        projects = Project.objects.all()
        pledges = Pledge.objects.all() 
        # for i in pledges:            
        # pledges_amount =        
        statistics = {  'project_count': projects.count(),
                        'pledges_count': pledges.count(),
                        'pledges_amount': 0 ,
                        'number_pledgers': 0
                     }
        return Response(statistics)

    def get(self, request):
        return self.statistics(request)

    # def get(self, request):
    #     projects = Project.objects.all()
    #     # serializer = ProjectSerializer(projects, many=True)
    #     return Response("hello")