from django.urls import path

from .views import CrunchBaseOrganization, CrunchBaseFounder

app_name = "baserow.t2"

urlpatterns =[
    path('crunch_base_organization/<int:table_id>/<int:row_id>/',CrunchBaseOrganization.as_view()),
    path('crunch_base_founder/<int:table_id>/<int:row_id>/',CrunchBaseFounder.as_view()),
]