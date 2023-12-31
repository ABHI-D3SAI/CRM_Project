from django.contrib import admin
from django.urls import path, include
from leads.views import MainPageView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPageView.as_view(), name= 'main-page'),
    path('leads/', include('leads.urls', namespace="leads"))
]
