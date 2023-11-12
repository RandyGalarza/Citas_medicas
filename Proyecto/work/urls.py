
from django.contrib import admin
from django.urls import path,include
from cita_medica import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('cita_medica.urls')),
    path('',views.inicio,name="home"),
    path('accounts/',include('django.contrib.auth.urls'))
]
