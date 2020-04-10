from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact

def register(request):  
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
             # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('register')
                else:
                    # Looks good
                    user = User.objects.create_user(username=username, password=password,email=email, first_name=first_name, last_name=last_name)
                    # Login after register and will save the instance in the STATE cookie 'sessionid',
                    # therefore, you can use user.is_authenticated to check if the user is logged in.
                    # 'user' will be available Globally after doing auth.login(request, user), 
                    # in html templates using 'user'||'user.is_authenticated' or 
                    # django .py files using 'request.user'||'request.user.is_authenticated'.
                    # because you created the object here using create_user you don't need -> user = auth.authenticate(username=username, password=password)
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in')
                    # return redirect('index')
                    #user.save()# NOT NEEDED AS create_user WILL CALL THE .save() method on the user object
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else: 
        return render(request, 'login.html')

def logout(request):
    #LOGOUT HAS TO BE A POST REQUEST
    if request.method == 'POST':
        auth.logout(request) #destroy the session
        messages.success(request, 'You are now logged out')
        return redirect('index')

def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context = {
    'contacts': user_contacts
    }
    return render(request, 'dashboard.html', context)
