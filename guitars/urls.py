from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ibanez/', include('ibanez.urls')),
    path('gibson/', include('gibson.urls')),
    path('fender/', include('fender.urls'))
]
