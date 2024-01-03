from django.contrib import admin
from django.urls import path, include
from leads.views import MainPageView, SignUpView
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPageView.as_view(), name= 'main-page'),
    path('leads/', include('leads.urls', namespace="leads")),
    path('signup/',SignUpView.as_view(), name='Signup'),
    path('login/',LoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(), name='logout')
    

]

if settings.DEBUG:
    urlpatterns +=  static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
