from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required   
from .utils import download_audio, transcribe_audio, generate_blog
from .models import BlogPost

# Create your views here.
#login view
def user_login(request):
    
    if request.method == 'POST':             
        username = request.POST.get('username')  
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        

        if user is not None:                 
            login(request, user)             
            messages.success(request, 'Login successful!')
            return redirect('index')         
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')     

#signup view
def user_signup(request):
    
    if request.method == 'POST':             
        username = request.POST.get('username')
        email = request.POST.get('email')
        passw = request.POST.get('password')
        confirm_pass = request.POST.get('password_confirm')

        
        if not username or not email or not passw or not confirm_pass:
            messages.error(request, 'Please fill out all fields.')
        elif passw != confirm_pass:
            messages.error(request, 'Passwords do not match.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
        else:
            
            user = User.objects.create_user(username=username, email=email, password=passw)
            user.save()

            messages.success(request, 'Account created! You are now logged in.')
            login(request, user)  
            return redirect('index')

    return render(request, 'signup.html')    

#logout view
def user_logout(request):
    
    logout(request)                          
    messages.info(request, 'You have been logged out.')
    return redirect('login')                

#home view
@login_required
def index(request):
    if request.method == "POST":
        link = request.POST.get("youtube_link")
        path=download_audio(link)
        transcript=transcribe_audio(path)
        text_blog=generate_blog(transcript)

        BlogPost.objects.create(
            user=request.user,
            youtube_title="(Title)",  
            youtube_url=link,
            transcript=transcript,
            gen_blog=text_blog
        )
        return render(request, 'result.html', {'blog': text_blog})
    
    return render(request, 'index.html')