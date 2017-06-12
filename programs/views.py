from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from .models import Field, Request, Program
from .forms import FieldForm, RequestForm, ProgramForm


class FieldMixin(LoginRequiredMixin, SuccessMessageMixin):
    model = Field


class FieldEditMixin(FieldMixin, SuccessMessageMixin):
    template_name = 'management/field/form.html'
    form_class = FieldForm
    success_url = reverse_lazy('programs:fields_list')


class FieldListView(PermissionRequiredMixin, FieldMixin, ListView):
    permission_required = 'programs.change_field'
    template_name = 'management/field/list.html'
    paginate_by = 10


class FieldAddView(PermissionRequiredMixin, FieldEditMixin, CreateView):
    permission_required = 'programs.add_field'
    success_message = "%(title)s field was added successfully"


class FieldUpdateView(PermissionRequiredMixin, FieldEditMixin, UpdateView):
    permission_required = 'programs.change_field'
    success_message = "%(title)s field was updated successfully"


class RequestMixin(LoginRequiredMixin, SuccessMessageMixin):
    model = Request


class RequestEditMixin(FieldMixin, SuccessMessageMixin):
    template_name = 'management/request/form.html'
    form_class = RequestForm
    success_url = reverse_lazy('programs:requests_list')


class RequestListView(PermissionRequiredMixin, RequestMixin, ListView):
    permission_required = 'programs.change_request'
    template_name = 'management/request/list.html'
    paginate_by = 10


class RequestAddView(PermissionRequiredMixin, RequestEditMixin, CreateView):
    permission_required = 'programs.add_request'
    success_message = "Your request was added successfully"


class RequestUpdateView(PermissionRequiredMixin, RequestEditMixin, UpdateView):
    permission_required = 'programs.change_request'
    success_message = "The request was updated successfully"


class ProgramMixin(LoginRequiredMixin, SuccessMessageMixin):
    model = Program


class ProgramEditMixin(ProgramMixin, SuccessMessageMixin):
    template_name = 'management/program/form.html'
    form_class = ProgramForm
    success_url = reverse_lazy('programs:programs_list')


class ProgramListView(PermissionRequiredMixin, ProgramMixin, ListView):
    permission_required = 'programs.change_program'
    template_name = 'management/program/list.html'
    paginate_by = 10


class ProgramAddView(PermissionRequiredMixin, ProgramEditMixin, CreateView):
    permission_required = 'programs.add_program'
    success_message = "%(title)s program was added successfully"


class ProgramUpdateView(PermissionRequiredMixin, ProgramEditMixin, UpdateView):
    permission_required = 'programs.change_program'
    success_message = "%(title)s program was updated successfully"
