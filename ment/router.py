from tracker.api.viewsets   import EntryViewSet #, TaskViewSet
from rest_framework         import routers

router = routers.DefaultRouter()
router.register('entries', EntryViewSet)