import json

from account.my_auth import requirelogin, check_login
from .models         import (
    Store,
    City,
    District,
    ServiceOne,
    ServiceTwo,
    StoreServiceOne,
    StoreServiceTwo,
    FavoriteStore
)

from django.views     import View
from django.http      import HttpResponse, JsonResponse
from django.db.models import F


class CityView(View):
    def get(self, request):
        return JsonResponse({'cities':list(City.objects.values())}, status = 200)

class DistrictView(View):
    def get(self, request): 
        try:
            city_id = request.GET['city']
            districts = District.objects.filter(city_id = city_id).values()

            return JsonResponse({'districts':list(districts)}, status = 200)
        
        except KeyError:
            return JsonResponse({'message': 'INVALID_KEY'}, status = 400)

class StoreSearchView(View):
    @check_login
    def get(self, request):
        if request.GET.get('favorite'):

            if request.user:
                store = Store.objects.filter(favoritestore__account_id = request.user.id)
            else:
                return HttpResponse(status = 403)
        else:
            data = {
                'city_id'        : request.GET.get('city'),
                'district_id'    : request.GET.get('district'),
                'name__icontains': request.GET.get('store')
            }

            data  = {key: value for key, value in data.items() if value}
            store = Store.objects.filter(**data)

        if store.exists():
            stores = store.annotate(
                city_name     = F('city__name'),
                district_name = F('district__name'),
                time          = F('business_time__time')
            ).values(
                'id',
                'name',
                'phone_number',
                'longitude',
                'latitude',
                'distance',
                'city_name',
                'district_name',
                'street_name',
                'time',
            ).order_by('distance')

            return JsonResponse({'stores':list(stores)}, status = 200)

        return JsonResponse({'message': 'NO_STORE'}, status = 400)

class StoreDetailView(View):
    def get(self, request, store_id):
        try:
            store            = Store.objects.get(id=store_id)
            store_attributes = {      
                'id'           : store.id,
                'name'         : store.name,
                'phone_number' : store.phone_number,
                'service_info' : list(store.service_one.values()),
                'store_info'   : list(store.service_two.values()),
                'city'         : store.city.name,
                'district'     : store.district.name,
                'street'       : store.street_name,
                'business_time': store.business_time.time
            }

            return JsonResponse({'store': list(store_attributes)}, status = 200)

        except Store.DoesNotExist:
            return HttpResponse(status = 404)

class FavoriteStoreView(View):
    @requirelogin
    def post(self, request, store_id):
        user           = request.user.id
        favorite_store = FavoriteStore.objects.filter(account_id = user, store_id = store_id)

        if not favorite_store.exists():
            FavoriteStore.objects.create(account_id = user, store_id = store_id)
    
            return JsonResponse({'message': 'SAVED'}, status = 200)

        favorite_store.get().delete()
        
        return JsonResponse({'message': 'DELETED'}, status = 200)