from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing
# Create your views here.
def index(request):
    # get an object using its id ALTERNATIVE TO:     product = get_object_or_404(Product, pk=id)
    try:
        allListings = Listing.objects.all()

        # PAGINATOR #
        paginator = Paginator(allListings, 2)# 2 elements per page
        page = request.GET.get('page') # gets the query value 'page'
        # pases the value of page to the paginator so we only display 2 per page clicked.
        paged_listings = paginator.get_page(page)
        ############# 

        context = {'listings':paged_listings}

    except Exception as anyException:
        return render(request,'listings.html', {'error':anyException})
    #else will only run if try was successful
    else:
        return render(request,'listings.html', context)

def listing(request, listing_id):
    # get an object using its id ALTERNATIVE TO:     product = get_object_or_404(Product, pk=id)
    try:
        listing = Listing.objects.get(pk=listing_id)
    except Exception as anyException:
        return render(request,'listing.html', {'error':anyException})
    #else will only run if try was successful
    else:
        return render(request,'listing.html', {'listing':listing})

def search(request):
    return render(request, 'search.html')