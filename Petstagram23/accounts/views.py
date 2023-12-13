from django.http import request, HttpResponse
from django.shortcuts import render
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, login, get_user_model
from django.contrib.auth import mixins as auth_mixins

from Petstagram23.accounts.forms import RegisterUserForm, LoginUserForm

UserModel = get_user_model()


# prevents logged in users from entering registration
class OnlyAnonymousMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponse(self.get_success_url())
        return super().dispatch(request, *args, **kwargs)


class RegisterUserView(OnlyAnonymousMixin, views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        # same as
        # user = self.object
        # login(self,request,user)
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['next'] = self.request.GET.get('next', '')
        return context

    def get_success_url(self):
        return self.request.POST.get('next', self.success_url)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'
    form_class = LoginUserForm

    # success_url = ''
    # def get_success_url(self):


class LogoutUserView(auth_views.LogoutView):
    template_name = 'common/home-page.html'


class ProfileDetailView(views.DetailView):
    template_name = 'accounts/profile-details-page.html'
    # To work provide either model ,query or get_queryset
    model = UserModel

    def get_context_data(self, **kwargs):
        profile_image = static('images/person.png')
        if self.object.profile_picture is not None:
            profile_image = self.object.profile_picture

        context = super().get_context_data(**kwargs)

        context['profile_image'] = profile_image

        return context
    # queryset =
    # def get_queryset(self):
    #     ...


class ProfileEditView(views.UpdateView):
    template_name = 'accounts/profile-edit-page.html'


class ProfileDeleteView(views.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
