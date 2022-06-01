from django.contrib import admin

from .models import Country, City, Restaurant
admin.site.site_header='Restaurant Admin'
admin.site.site_title='Restaurant Admin'


class InlineRestaurant(admin.TabularInline):
    model = Restaurant
    extra = 1


class CityAdmin(admin.ModelAdmin):
    inlines = [InlineRestaurant]


class RestaurantAdmin(admin.ModelAdmin):
    fields = ('name','city','address')
    list_display = ('name','city','address','Full_Address')
    # list_editable = ('name','city')
    list_filter = ('city','name')
    search_fields = ('name','city')

    def Full_Address(self,obj):
        return "{},{}".format(obj.city,obj.address)


admin.site.register(Country)
admin.site.register(City,CityAdmin)
admin.site.register(Restaurant,RestaurantAdmin)


