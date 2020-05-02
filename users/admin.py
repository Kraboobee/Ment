from django.contrib import admin
from users.models import Profile, AccompaniMent, TreatMent, FulfilMent

admin.site.register(Profile)
admin.site.register(AccompaniMent)
admin.site.register(TreatMent)
admin.site.register(FulfilMent)