from django.urls import path, include
from .views import *

urlpatterns = [
    path('company/', Company_Create.as_view(), name='company-create'),
    path('model/', Model_Create.as_view(), name='model-create'),

]
