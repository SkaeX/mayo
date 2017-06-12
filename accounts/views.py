from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import UpdateView
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from .models import User
from .forms import UserEditForm


@login_required()
def profile_home(request):
    return render(request, 'profile/home.html', {})


class UserMixin(LoginRequiredMixin, SuccessMessageMixin):
    model = User


class UserListView(PermissionRequiredMixin, UserMixin, ListView):
    permission_required = 'auth.change_user'
    template_name = 'management/user/list.html'
    paginate_by = 10



class UserUpdateView(PermissionRequiredMixin, UserMixin, UpdateView):
    permission_required = 'auth.change_user'
    template_name = 'management/user/form.html'
    success_url = reverse_lazy('profile:users_list')
    success_message = "%(email)s was updated successfully"
    form_class = UserEditForm
