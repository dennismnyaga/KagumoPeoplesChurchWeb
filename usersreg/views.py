from django.shortcuts import render, redirect
from .models import *
from .forms import CreateUserForm, CustomerForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout





def register(request):
	form = CreateUserForm()
	customer = request.user
	print(customer)
	if request.method =='POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Account was created for ' + user)
			return redirect('usersreg:login')
	context = {'form':form}
	return render(request, 'registration/register.html', context)
	
def loginPage(request):

	if request.method == 'POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		
		user = authenticate(request, username=username, password=password)
		
		if user is not None:
			login(request,user)
			return redirect('shopping:store')
		else:
			messages.info(request, 'username or password is incorrect')
			return render(request,'registration/login.html', context)
	context = {}
	return render(request,'registration/login.html', context)





def logoutUser(request):
	logout(request)
	return redirect('login')



# def register(request):
#     """Register a new user."""
#     if request.method != 'POST':
#         # Display blank registration form. 
#         form = UserCreationForm()
#     else:
#         # Process completed form.
#         form = UserCreationForm(data=request.POST)
#         if form.is_valid():
#             new_user = form.save()
#             login(request, new_user)
#             return redirect('webapp:home')
#     context = {'form': form}
#     return render(request, 'registration/register.html', context)