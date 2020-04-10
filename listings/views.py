from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing
from .choices import price_choices,bedroom_choices,state_choices

# Create your views here.
def index(request):
    # get an object using its id ALTERNATIVE TO:     product = get_object_or_404(Product, pk=id)
    try:
        # allListings = Listing.objects.all()
        # Order by list_date in '-' desc order and filter by is_published=True
        allListings = Listing.objects.order_by('-list_date').filter(is_published=True)

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
    queryset_list = Listing.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords: #CHECK IS NOT AN EMPTY STRING
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__gte=bedrooms)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'listings': queryset_list,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'values': {
            'keywords': request.GET['keywords'], # this value is always passed, as empty.
            'city': request.GET.get('city', default = None),
            'state': request.GET.get('state', default = None),
            'bedrooms': request.GET.get('bedrooms', default = None),
            'price': request.GET.get('price', default = None)
        }
    }
    return render(request, 'search.html', context)