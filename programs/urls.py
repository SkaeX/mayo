from django.conf.urls import url
from . import views

urlpatterns = [


    # Management
    url(r'^fields/$',
        views.FieldListView.as_view(),
        name='fields_list'),
    url(r'^fields/new/$',
        views.FieldAddView.as_view(),
        name='new_field'),
    url(r'^fields/(?P<pk>\d+)/edit/$',
        views.FieldUpdateView.as_view(),
        name='field_edit'),

    url(r'^requests/$',
        views.RequestListView.as_view(),
        name='requests_list'),
    url(r'^requests/new/$',
        views.RequestAddView.as_view(),
        name='new_request'),
    url(r'^requests/(?P<pk>\d+)/edit/$',
        views.RequestUpdateView.as_view(),
        name='request_edit'),

    url(r'^programs/$',
        views.ProgramListView.as_view(),
        name='programs_list'),
    url(r'^programs/new/$',
        views.ProgramAddView.as_view(),
        name='new_program'),
    url(r'^programs/(?P<pk>\d+)/edit/$',
        views.ProgramUpdateView.as_view(),
        name='program_edit'),
]