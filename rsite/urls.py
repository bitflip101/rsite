from django.contrib import admin
from django.urls import path, include
from abode.views import handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('abode.urls', namespace='abode')),
]

handler404 = 'abode.views.handler404'
handler500 = handler500 # Link to the custom 500 view 
