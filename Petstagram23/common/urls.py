from django.urls import path

from Petstagram23.common.views import index

urlpatterns = (
    path('',index, name='index'),
)