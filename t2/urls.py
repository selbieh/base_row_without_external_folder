from django.urls import path

from .views.crunch_base import CrunchBaseOrganization, CrunchBaseFounder
from rest_framework.routers import DefaultRouter
from django.urls import include
from .views.staff_users import StaffUserControlViewSet

router=DefaultRouter()
router.register('staff-control',StaffUserControlViewSet,basename='staff_control')


app_name = "baserow.t2"

urlpatterns =[
    path('crunch_base_organization/<int:table_id>/<int:row_id>/',CrunchBaseOrganization.as_view()),
    path('crunch_base_founder/<int:table_id>/<int:row_id>/',CrunchBaseFounder.as_view()),
    path('',include(router.urls))
]