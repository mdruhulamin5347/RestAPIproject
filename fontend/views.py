from django.shortcuts import render
from .forms import contactForm
import requests, json

# Create your views here.

def Login_view(request):
    # if request.method == 'POST':        
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     credentials = {
    #         'username': username,
    #         'password': password,
    #     }
    #     django_backend_url = 'http://127.0.0.1:8000/api/jwt-access/'
    #     response = requests.post(url=django_backend_url, data=credentials)
    #     try:
    #         resp0=json.loads(response.text)
    #     except:
    #         resp0 = None

    #     print(resp0)   
        return render(request, 'login.html')

def Contact_form(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        data = form.data
        d={'username':'ruhularafat', 'password':'ruhularafat'}
        url0 = 'http://127.0.0.1:8000/api/jwt-access/'
        api0 = requests.post(url=url0, json=d)
        try:
            resp0=json.loads(api0.text)
        except:
            resp0 = None
        token = resp0['access']
        url = 'http://127.0.0.1:8000/api/rest/serializer/'
        api = requests.get(url= url, data=data, headers={'Authorization': f'Bearer {token}'})
        try:
            resp=json.loads(api.text)
        except:
            resp = None
        print(resp)
      
    else:
        form = contactForm()
    return render(request, 'contact.html', {'form':form})


def contact_view(request):
    d={'username':'ruhularafat', 'password':'ruhularafat'}
    url0 = 'http://127.0.0.1:8000/api/jwt-access/'
    api0 = requests.post(url=url0, json=d)
    try:
        resp0=json.loads(api0.text)
    except:
        resp0 = None
    token = resp0['access']
    url = 'http://127.0.0.1:8000/api/rest/serializer/'
    api = requests.get(url= url, headers={'Authorization': f'Bearer {token}'})
    try:
        resp=json.loads(api.text)
    except:
        resp = None    
    return render(request, 'contact_view.html', {'resp':resp})



def book_post(request):
     return render(request, 'index.html')
