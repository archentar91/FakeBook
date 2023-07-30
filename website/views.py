from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from .forms import SignUpForm, AddRecordForm
from .models import Record


# Create your views here.

def home(request):
    records = Record.objects.all()  
    # Check if the user is logged in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})

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
