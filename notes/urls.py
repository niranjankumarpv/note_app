
from django.contrib import admin
from django.urls import path, include
from note_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('note_app.urls'))
]
