from django.urls import path

from . import views
#something seems not right. please fix it
urlpatterns = [
    path('', views.index, name='index'),
	path('taglines/', views.detail, name='detail'),
]
