from django.urls import path, include

from Petstagram23.accounts.views import LoginUserView, \
    RegisterUserView, LogoutUserView, ProfileDetailView, ProfileEditView, ProfileDeleteView

urlpatterns = (
    path('register/',RegisterUserView.as_view(), name='register user'),
    path('login/', LoginUserView.as_view(), name='login user'),
    path('logout/', LogoutUserView.as_view(), name='logout user'),
    path('profile/<int:pk>/',include(
        [
            path('',ProfileDetailView.as_view(), name='details user'),
            path('edit/',ProfileEditView.as_view(),name='edit user'),
            path('delete/',ProfileDeleteView.as_view(),name='delete user'),
        ]
    ))
)