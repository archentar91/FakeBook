from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .forms import SignUpForm, AddRecordForm, UserChangeForm, ChangePasswordForm, LoginForm, UpdateProfileForm
from .models import Record


def home(request):
    records = Record.objects.all()
    
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            # Authenticate
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have been logged in!")
            else:
                messages.error(request, "Invalid username or password. Please try again.")
        
        # Redirect to the home page (to avoid form resubmission)
        return redirect('home')
    
    else:
        login_form = LoginForm()

    return render(request, 'home.html', {'records': records, 'login_form': login_form})

@login_required
def my_account_user(request):
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('my_account')
    else:
        form = UpdateProfileForm(instance=request.user)

    return render(request, 'my_account.html', {'form': form})

@login_required
def change_password_user(request):
    if request.method == 'POST':
        form = ChangePasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            logout(request)
            messages.success(request, 'Password changed successfully!')
            return redirect('home')
    else:
        form = ChangePasswordForm(user=request.user)
        messages.error(request, 'Please fill in all the fields.')
    return render(request, 'change_password.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form})

def register_check_password(request):
    if request.method == "POST":
        data = request.POST
        password = data.get("password", "")
        is_valid_password = True  # Replace this with your password authentication logic
        return JsonResponse({"valid": is_valid_password})
    return JsonResponse({"valid": False})  # Return False if the request method is not POST

def customer_record(request, pk):
    if request.user.is_authenticated:
        # Check if the user is logged in
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.error(request, 'You are not logged in')
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record deleted successfully")
        return redirect('home')
    else:
        messages.error(request, 'You are not logged in')
        return redirect('home')
    
def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Record Added.")
				return redirect('home')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In.")
		return redirect('home')

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "Record Updated.")
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, "You must be logged in.")
        return redirect('home')
