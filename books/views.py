from django.shortcuts import render, redirect
from django.views import View
from .forms import UserForm
from django.contrib.auth import logout


def index(request):
    if request.user.is_authenticated:
        return redirect('account/index')
    return render(request, 'home/home.html')


class UserFormView(View):
    form_class = UserForm
    template_name = 'home/register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            # create object
            user = form.save(commit=False)
            # clean data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            return render(request, 'home/registersucces.html')


def Logout(request):
    logout(request)
    return redirect('books:index')
