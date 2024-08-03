from django.urls import path
from .views import *
urlpatterns = [
    path('first/',firstapi ,name='first'),
    path('register/',registations , name='register'),
    path('search/', Search.as_view() , name='search'),
    path('apiview/',contactAPIVIEW.as_view() , name='contact-api'),
    path('serializer/', contactserializerAPIVIEW.as_view(), name='serializer'),
    path('serializers/', contactserializersAPIVIEW.as_view(), name='serializers'),
    path('post/', genericAPIVIEW.as_view(), name='post'),
    path('postlist/', postlistAPIVIEW.as_view(), name='postlist'),
    path('retrive/<int:id>/', postretriveAPIVIEW.as_view(), name='retrive'),
    path('api/books/', BookListCreateView.as_view(), name='book-list-create'),
]

