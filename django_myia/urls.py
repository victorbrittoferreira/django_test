from django.contrib import admin
from django.urls import path

from myia.views import error

urlpatterns = [
    path('admin/', admin.site.urls),

        # Error Handling
    path('error/', error, name='error'),
]
