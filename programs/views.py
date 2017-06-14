from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.messages.views import SuccessMessageMixin
from braces.views import LoginRequiredMixin, PermissionRequiredMixin
from .models import Field, Prequest, Program
from .forms import FieldForm, PrequestForm, ProgramForm, IndividualPrequestForm


class FieldMixin(LoginRequiredMixin, SuccessMessageMixin):
    model = Field


class FieldEditMixin(FieldMixin):
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


class PrequestMixin(LoginRequiredMixin, SuccessMessageMixin):
    model = Prequest


class PrequestEditMixin(PrequestMixin):
    template_name = 'management/prequest/form.html'
    form_class = PrequestForm
    success_url = reverse_lazy('programs:prequests_list')


class PrequestListView(PermissionRequiredMixin, PrequestMixin, ListView):
    permission_required = 'programs.change_prequest'
    template_name = 'management/prequest/list.html'
    paginate_by = 10


class PrequestAddView(PermissionRequiredMixin, PrequestEditMixin, CreateView):
    permission_required = 'programs.add_prequest'
    success_message = "Your prequest was added successfully"


class PrequestUpdateView(PermissionRequiredMixin, PrequestEditMixin, UpdateView):
    permission_required = 'programs.change_prequest'
    success_message = "The prequest was updated successfully"


class PrequestDeleteView(PermissionRequiredMixin, PrequestMixin, DeleteView):
    permission_required = 'programs.delete_prequest'
    success_url = reverse_lazy('programs:prequests_list')
    template_name = 'management/prequest/delete.html'
    success_message = "The prequest was deleted successfully"


class IndividualPrequestAddView(PermissionRequiredMixin, PrequestEditMixin, CreateView):
    success_message = "Your prequest was created successfully"
    success_url = reverse_lazy('programs:myprograms_list')
    permission_required = 'programs.add_prequest'
    form_class = IndividualPrequestForm

    def form_valid(self, form):
        req = form.instance
        req.requester = self.request.user
        return super(IndividualPrequestAddView, self).form_valid(form)


class ProgramMixin(LoginRequiredMixin, SuccessMessageMixin):
    model = Program


class ProgramEditMixin(ProgramMixin):
    template_name = 'management/program/form.html'
    form_class = ProgramForm
    success_url = reverse_lazy('programs:programs_list')


class ProgramListView(PermissionRequiredMixin, ProgramMixin, ListView):
    permission_required = 'programs.change_program'
    template_name = 'management/program/list.html'
    paginate_by = 10


class IndividualProgramListView(ProgramMixin, ListView):
    template_name = 'program/list.html'
    paginate_by = 10

    def get_queryset(self):
        groups = self.request.user.groups.values_list("name", flat=True)
        qs = super(IndividualProgramListView, self).get_queryset()
        if 'Mentor' in groups:
            return qs.filter(mentors=self.request.user)
        elif 'Mentee' in groups:
            return qs.filter(mentees=self.request.user)
        else:
            return qs


class IndividualProgramDetailView(ProgramMixin, DetailView):
    template_name = 'program/detail.html'

    def get_queryset(self):
        groups = self.request.user.groups.values_list("name", flat=True)
        qs = super(IndividualProgramDetailView, self).get_queryset()
        if 'Mentor' in groups:
            return qs.filter(mentors=self.request.user)
        elif 'Mentee' in groups:
            return qs.filter(mentees=self.request.user)
        else:
            return qs


class ProgramAddView(PermissionRequiredMixin, ProgramEditMixin, CreateView):
    permission_required = 'programs.add_program'
    success_message = "%(title)s program was added successfully"


class ProgramUpdateView(PermissionRequiredMixin, ProgramEditMixin, UpdateView):
    permission_required = 'programs.change_program'
    success_message = "%(title)s program was updated successfully"
