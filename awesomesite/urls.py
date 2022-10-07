from django.contrib import admin
from django.urls import include, path

#somethings not right here either. What are you waiting for? go ahead and fix it!
urlpatterns = [
    path('admin', admin.site.urls), #Check this
]
