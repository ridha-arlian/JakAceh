from gc import get_objects
from django.shortcuts import redirect, render
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Profile
from jak.forms import EditUserProfileForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
from django.contrib.auth.models import User, auth
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    return render(request, 'jak/index.html')

@login_required(login_url="login")
def home(request):
    return render(request, 'jak/home.html')

@login_required(login_url="login")
def angkutan(request):
    return render(request, 'jak/angkutan.html')

@login_required(login_url="login")
def bengkel(request):
    return render(request, 'jak/bengkel.html')

@login_required(login_url="login")
def kuliner(request):
    return render(request, 'jak/kuliner.html')

@login_required(login_url="login")
def minimarket(request):
    return render(request, 'jak/minimarket.html')

@login_required(login_url="login")
def penginapan(request):
    return render(request, 'jak/penginapan.html')

@login_required(login_url="login")
def polisi(request):
    return render(request, 'jak/polisi.html')


@login_required(login_url="login")
def profil(request):
    user_profile = Profile.objects.get(user=request.user)
    
    context = {
        'user_profile': user_profile
    }


    if request.method == 'POST':

        if request.FILES.get('image') == None:
            image = user_profile.profileimg        
            user_profile.profileimg = image
            user_profile.save()
        if request.FILES.get('image') != None:
            image = request.FILES.get('image')

            user_profile.profileimg = image
            user_profile.save()
        
        return redirect('profil')
    return render(request, 'jak/profil.html', context)


def registrasi(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('registrasi')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('registrasi')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
                user.save()

                #log user in and redirect to settings page
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                #create a Profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('login')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('registrasi')
        
    else:
        return render(request, 'jak/registrasi.html')

@login_required(login_url="login")
def rumahsakit(request):
    return render(request, 'jak/rumahsakit.html')

@login_required(login_url="login")
def souvenir(request):
    return render(request, 'jak/souvenir.html')

@login_required(login_url="login")
def spbu(request):
    return render(request, 'jak/spbu.html')

@login_required(login_url="login")
def wisata(request):
    return render(request, 'jak/wisata.html')

def login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            request.session['login']=True
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')

    else:
        return render(request, 'jak/login.html')

@login_required(login_url='login')
def logout(request):
    del request.session['login']
    auth.logout(request)
    return redirect('login')

class UpdateUserView(generic.UpdateView):
    form_class = EditUserProfileForm
    template_name = "jak/update.html"
    success_url = reverse_lazy('profil')
    
    def get_object(self):
        return self.request.user
