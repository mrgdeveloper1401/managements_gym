from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .forms import SignUpForm, LoginForm, ProfileEditForm


class SignupView(View):
    form_class = SignUpForm
    template_name = 'accounts/login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"signup": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'successfully create account')
            # return redirect()
        return render(request, self.template_name, {'form': form})


class LoginViews(LoginView):
    form_class = LoginForm
    success_url = '/'
    template_name = 'accounts/login.html'

