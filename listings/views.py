from django.shortcuts import render
from django.http import HttpResponse
from .models import Listing
# Create your views here.
def index(request):
        # get an object using its id ALTERNATIVE TO:     product = get_object_or_404(Product, pk=id)
    try:
        allListings = Listing.objects.all()
    except Exception as anyException:
        return render(request,'listings.html', {'error':anyException})
    #else will only run if try was successful
    else:
        return render(request,'listings.html', {'listings':allListings})

def listing(request, listing_id):
    return render(request, 'listing.html')

def search(request):
    return render(request, 'search.html')