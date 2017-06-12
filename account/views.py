from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views import generic
from account.models import Books


@method_decorator(login_required(login_url='books:login'), name='dispatch')
class IndexView(generic.ListView):
    template_name = 'account/mainpage.html'

    def get_queryset(self):
        return Books.objects.all()


class DetailView(generic.DetailView):
    model = Books
    template_name = 'account/bookdetails.html'


class ListMybooks(generic.ListView):
    template_name = 'account/mainpage.html'

    def get_queryset(self):
        return Books.objects.filter(users=self.request.user)


def change_to_favorite(request, operation, pk):
    new_book = Books.objects.get(pk=pk)
    if operation == 'add':
        Books.add_book(request.user, new_book)
    elif operation == 'remove':
        Books.remove_favorite(request.user, new_book)
    redirect('account:IndexView')
