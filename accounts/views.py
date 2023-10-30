from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import UserSignupForm, UserLoginForm
from .models import User


class UserSignupView(View):
    templated_name = 'accounts/signup.html'
    form_class = UserSignupForm
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.templated_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(
                email = cd['email'],
                mobile_phone = cd['mobile_phone'],
                full_name = cd['full_name'],
                password = cd['password']
            )
            messages.success(request, 'User created successfully', 'success')
            return redirect('home:home')
        messages.error(request, 'invalid', 'warning')
        return render(request, self.templated_name, {'form': form})
    
    
class UserLoginView(View):
    templated_name = 'accounts/login.html'
    form_class = UserLoginForm
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.templated_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                email = cd['email'],
                password = cd['password']
            )
            if user is not None:
                login(request, user)
                messages.success(request, 'login successful', 'success')
                return redirect('home:home')
            messages.error(request, 'Invalid username or password', 'warning')
        return render(request, self.templated_name, {'form': form})
    
    
class UserLogoutView(View):
    def get(self, request):
            logout(request)
            messages.success(request, 'User logged out', 'success')
            return redirect('accounts:login')
        
        
class UserProfileView(View):
    
    def dispatch(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs['user_id'])
        if request.user.id != user.id:
            messages.error(request, 'invalid', 'danger')
            return redirect('accounts:profile', request.user.id)
        return super().dispatch(request, *args, **kwargs)
        
        
    templated_name = 'accounts/profile.html'
    def get(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        return render(request, self.templated_name, {'user': user})
    
    def post(self, request):
        pass
    
    