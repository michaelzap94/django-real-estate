from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    #Fields we want to show in the Listing
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title') # clickable element to access object
    list_filter = ('realtor',) #Filter box to filter by Realtor
    list_editable = ('is_published',) # Edit field on the Table Row itself
    #Fields we'll use to search in the search box
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    list_per_page = 25


# Register your models here.
admin.site.register(Listing, ListingAdmin)