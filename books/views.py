from django.shortcuts import render
from django.views import View
from .forms import UserForm


def index(request):
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


























# class LoginView(View):
#         form_class = UserForm
#         template_name = 'home/login.html'
#
#         def get(self, request):
#             form = self.form_class(None)
#             return render(request, self.template_name, {'form': form})
#
#         def post(self, request):
#             form = self.form_class(request.POST)
#             if form.is_valid():
#                 username = form.cleaned_data['username']
#                 password = form.cleaned_data['password']
#                 user = authenticate(username=username, password=password)
#                 if user is not None:
#                     if user.is_active:
#                         login(request, user)
#                         return (request, 'home/registersucces.html')
#                 return render(request, self.template_name, {'form': form})
#             else:
#                 return render(request, 'home/home.html')
