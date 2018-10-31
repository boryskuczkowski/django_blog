
from django.urls import path, include
from envelope.views import MyContactView


urlpatterns = [
    path('', MyContactView.as_view(), name='envelope-contact'),

]
