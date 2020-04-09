from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor

# Create your views here.
def index(request):
    context = {
        'listings': Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    }
    return render(request, 'pages/index.html', context)

def about(request):
    context = {
        'realtors': Realtor.objects.all().order_by('-hire_date'), # just: Realtor.objects.order_by('-hire_date')
        'mvp_realtors': Realtor.objects.all().filter(is_mvp=True)[:1], # any mvp, no preference
    }
    return render(request, 'pages/about.html', context)