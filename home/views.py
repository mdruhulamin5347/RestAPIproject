from django.shortcuts import render
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from rest_framework.views import APIView
from .serializers import *

# Create your views here.

@api_view(['GET','POST'])
def firstapi(request):
    if request.method == 'POST':
        name = request.data['name']
        age = request.data['age']
        print(name,age)
        return Response({"name":name,"age":age})
    context={
        'name':'Md.Ruhul amin',
        'versity':'Jashore University'
    }
    return Response(context)

from django.contrib.auth.models import User
@api_view(['GET','POST'])
def registations(request):
    if request.method == 'POST':
        username = request.data['username']
        email = request.data['email']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        password1 = request.data['password1']
        password2 = request.data['password2']

        if User.objects.filter(username=username).exists():
            return Response({'error':'username allready exists'})
        if User.objects.filter(email=email).exists():
            return Response({'error':'email name already exists'})
        
        if User.objects.filter(first_name=first_name).exists():
            return Response({'error':'first name already exists'})
        if password1 != password2:
            return Response({'error':'two password did not match'})
        
        user = User()
        user.username = username
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.is_active = True
        
        user.set_password(raw_password=password1)
        user.save()
        return Response({"success":"successfully user login"})
    context1={
        'name':'ruhul amin',
        'age':21
    }
    return Response(context1)





class contactAPIVIEW(APIView):
    permission_classes=[AllowAny]
    def post(self, request, format = None):
        data = request.data
        name = data['name']
        email = data['email']
        phone = data['phone']
        details = data['details']

        contact=Contact(name=name,email=email,phone=phone,details=details)
        contact.save()
        return Response({'success':'successfully saved!'})
    def get(self, request, format = None):
        return Response({'unsuccess':'successfully not save!'})
    


class contactserializerAPIVIEW(APIView):
    permission_classes=[AllowAny]
    def post(self, request , format = None):
        serializer = contactserializerform(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    def get(self, request, format = None):
        queryset = contactserializer.objects.all()
        serializer = contactserializerform(queryset, many = True)
        return Response(serializer.data)
    

class contactserializersAPIVIEW(APIView):
    def post(self, request , format = None):
        serializer = contactserializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    def put(self, request , format = None):
        contactt = serializerss.objects.get(id = 2)
        serializer = contactserializers(data = request.data, instance=contactt)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    def get(self, request, format = None):
        queryset = serializerss.objects.all()
        serializer = contactserializers(queryset, many = True)
        return Response(serializer.data)
    


from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView,ListCreateAPIView

class genericAPIVIEW(CreateAPIView):
    permission_classes=[IsAuthenticated]
    queryset = blogpost.objects.all()
    serializer_class = postserializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class postlistAPIVIEW(ListAPIView):
    queryset = blogpost.objects.all()
    serializer_class = postserializer


class postretriveAPIVIEW(RetrieveUpdateDestroyAPIView):
    queryset = blogpost.objects.all()
    serializer_class = postserializer
    lookup_field = 'id'



from django.db.models import Q
class Search(APIView):
    permission_classes=[AllowAny]
    def post(self, request, format = None):
        queryset = blogpost.objects.all()
        try:
            str = self.request.data['str']
            q = (Q(title__icontains=str))
            queryset= queryset.filter(q)
        except:
            pass
    
        try:
            subject = self.request.data['subject']       
            queryset= queryset.filter(subject__iexact = subject)
        except:
            pass
        serializer = postserializer(queryset, many = True)
        return Response(serializer.data)
    def get(self,request,foramt=None):
        queryset = blogpost.objects.all()
        serializer = postserializer(queryset, many = True)
        return Response(serializer.data)


class BookListCreateView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer