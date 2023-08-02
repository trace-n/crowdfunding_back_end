from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
            if request.method in permissions.SAFE_METHODS:
                return True
            return obj.owner == request.user
    
class IsSupporterOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
            if request.method in permissions.SAFE_METHODS:
                return True
            return obj.supporter == request.user    
    
class IsSupporterNotOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
            if request.method in permissions.SAFE_METHODS:
                return True
            # supporter cannot be the owner of project
# for shell troubleshooting
# from projects.models import Project, Pledge
# x = Pledge.objects.get(pk=1)
# x.project.id
# 1
# x.project.title
# 'Another project'
# x.project.owner
# <CustomUser: trace_n>
# print(x.project.owner == x.supporter)
# True

            # return obj.project.owner != request.user    

            return obj.owner != request.user