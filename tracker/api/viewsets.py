from tracker.models import Entry, CommitMent
from .serializers   import EntrySerializer #, TaskViewSet
from rest_framework import viewsets

class EntryViewSet(viewsets.ModelViewSet):
    queryset            = Entry.objects.all()
    serializer_class    = EntrySerializer
    
# class TaskViewSet(viewsets.ModelViewSet):
#     queryset            = CommitMent.objects.all()
#     serializer_class    = TaskSerializer
    
