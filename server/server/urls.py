from django.contrib import admin
from django.urls import path,include

from user.views import UserView
from rest_framework import routers

route = routers.DefaultRouter()
route.register("",UserView)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))

]
