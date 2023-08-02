from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project, Pledge
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer, PledgeDetailSerializer
from django.http import Http404
from rest_framework import status, permissions
from .permissions import IsOwnerOrReadOnly, IsSupporterOrReadOnly, IsSupporterNotOwnerOrReadOnly
from django.db.models import Sum

# Create your views here.

class ProjectList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

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
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly # for put method
    ]

    def get_object(self, pk):
        # return Project.objects.get(pk=pk) 
        try: 
            # return Project.objects.get(pk=pk)
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(self.request, project)
            return project
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        project = self.get_object(pk) 
        # serializer = ProjectSerializer(project)
        serializer = ProjectDetailSerializer(project)        
        return Response(serializer.data)
    
    def put(self, request, pk):
        project = self.get_object(pk)

        serializer = ProjectDetailSerializer(
            instance=project,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class PledgeList(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsSupporterNotOwnerOrReadOnly
    ]

    def get(self, request):
        pledges = Pledge.objects.all()
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)


    def post(self, request):
        
        pledge = request.data
        # pledge is not saved yet, is in json format
        # print("pledge=", pledge, pledge['project'])
        # self.check_object_permissions(self.request, pledge)
        project = Project.objects.get(pk=pledge['project'])
        # print("compare proj owner to request user",project.owner, request.user)
        # project owner must not be the requesting user when creating a pledge        
        self.check_object_permissions(self.request, project)

        serializer = PledgeSerializer(data=request.data)
        print(serializer)

        if serializer.is_valid():
            serializer.save(supporter=request.user)            
            # serializer.save()
            # return Response(serializer.data)
            return Response(
                serializer.data, 
                status=status.HTTP_201_CREATED,
            )
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class PledgeDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsSupporterOrReadOnly # for put method
    ]

    def get_object(self, pk):
 
        try: 
            pledge = Pledge.objects.get(pk=pk)
            return pledge
        except Pledge.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        pledge = self.get_object(pk) 
        serializer = PledgeDetailSerializer(pledge)        
        return Response(serializer.data)
    
    def put(self, request, pk):
        pledge = self.get_object(pk)
        self.check_object_permissions(self.request, pledge)

        serializer = PledgeDetailSerializer(
            instance=pledge,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

# Inherit from class ProjectLIst to return a count of total project, total pledges, $ amount of pledges, unique supporters
class ProjectStatistics(ProjectList):

    def statistics(self,request):
        # projects = self.get_queryset()

        projects = Project.objects.all()
        pledges = Pledge.objects.all() 
        pledges_amt = pledges.aggregate(Sum('amount'))
        unique_supporters = pledges.values_list('supporter',flat=True).distinct().count()
     
        statistics = {  'project_count': projects.count(),
                        'pledge_count': pledges.count(),
                        'pledge_amount': pledges_amt['amount__sum'],
                        'unique_supporters': unique_supporters
                     }
        return Response(statistics)

    def get(self, request):
        return self.statistics(request)

    # def get(self, request):
    #     projects = Project.objects.all()
    #     # serializer = ProjectSerializer(projects, many=True)
    #     return Response("hello")