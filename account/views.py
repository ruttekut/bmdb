from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
from account.models import Books


@method_decorator(login_required(login_url='login/'), name='dispatch')
class IndexView(generic.ListView):
    template_name = 'account/home.html'

    def get_queryset(self):
        return Books.objects.all()
# # Create your views here.
# @login_required(login_url='login')
# def index(request):
#     return render(request, 'account/home.html')
