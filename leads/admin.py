from django.contrib import admin

from .models import *

admin.site.register(User)
admin.site.register(Leads)
admin.site.register(Agent)