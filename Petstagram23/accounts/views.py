from django.http import HttpResponse
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, login, get_user_model

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
        # Variant 1 Send mail only when registered from website
        # not from admin
        # send_mail ....
        # same as
        # user = self.object
        # login(self,request,user)
        return result

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['next'] = self.request.GET.get('next', '')

        return context

    def get_success_url(self):
        return self.request.POST.get('next', self.success_url)


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

    profile_image = static('images/person.png')

    def get_profile_image(self):
        if self.object.profile_picture is not None:
            return self.object.profile_picture
        return self.profile_image

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['profile_image'] = self.get_profile_image()
        context['pets'] = self.request.user.pet_set.all()

        return context

    # `UserModel.objects.all()` returns `queryset`
    # To work provide either `model`, `queryset` or `get_queryset`


# def profile_details(request, pk):
#     pets = Pet.objects.all()
#
#     context = {
#         "pets": pets,
#     }
#
#     return render(request, 'accounts/profile-details-page.html', context=context)


class ProfileEditView(views.UpdateView):
    template_name = 'accounts/profile-edit-page.html'


class ProfileDeleteView(views.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
