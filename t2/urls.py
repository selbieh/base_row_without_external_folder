from django.urls import path

from .views import  CrunchBaseOrganization


app_name = "baserow.t2"

urlpatterns =[
    path('crunch_base_organization/<int:table_id>/<int:row_id>/',CrunchBaseOrganization.as_view())
]