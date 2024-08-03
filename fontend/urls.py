from django.urls import path
from .views import *

urlpatterns = [
    path('contact/', Contact_form, name='contact'),
    path('details/',contact_view,name='details'),
    path('login/',Login_view,name='login'),
    path('form/',book_post,name='form'),
]
