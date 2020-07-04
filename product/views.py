import json

from .models import (
    MainCategory,
    Product,
    Size,
    MenuBar,
    Allergy,
    Tag
)

from django.views     import View
from django.http      import HttpResponse, JsonResponse
from django.db.models import F


class CategoryView(View):
    def get(self, request):
        categories = MainCategory.objects.prefetch_related('menubar_set')
        categories = [{
            'category': category.name,
            'menu'    : list(category.menubar_set.values())
        } for category in categories.all()]

        return JsonResponse({'menu_bars':categories}, status = 200)

class ProductDetailView(View):
    def get(self, request, product_id):
        try:
            product = Product.objects.get(id = product_id)

            product_attribute = {
                'id'             : product.id,
                'name'           : product.name_kr,
                'name_en'        : product.name_en,
                'icecream_option': product.icecream_option,
                'description'    : product.description,
                'thumbnail'      : product.thumbnail,
                'release_date'   : product.release_date,
                'menu'           : product.menu_id,
                'flavors'        : list(
                    product.flavor.annotate(name = F('name_kr')).values(
                        'name',
                        'thumbnail'
                    )
                )
            }

            return JsonResponse({'product': product_attribute}, status = 200)

        except Product.DoesNotExist:
            return HttpResponse(status = 404)

class SizeView(View):
    def get(self, request):
        return JsonResponse({'sizes': list(Size.objects.values())}, status = 200)

class BestFlavorView(View):
    def get(self, request):
        products       = Product.objects.filter(rank__in = range(1,11)).order_by('rank')
        best_attribute = products.annotate(name = F('name_kr')).values(
            'id',
            'rank',
            'name',
            'thumbnail'
        )

        return JsonResponse({'products': list(best_attribute)}, status = 200)

class SearchBarView(View):
    def get(self, request):
        tag_id  = request.GET.getlist('id', [215, 216, 219])
        menu    = MenuBar.objects.filter(category_id = 1).values('id', 'name')
        allergy = Allergy.objects.values('name')
        tag     = Tag.objects.filter(id__in = tag_id).values('name')

        return JsonResponse({
            'data': {
                'menu'   : list(menu),
                'allergy': list(allergy),
                'tags'   : list(tag)
            }
        }, status = 200)

class ProductSearchView(View):
    def get(self, request):
        data = {
            'menu_id'           : request.GET.get('menu'),
            'name_kr__icontains': request.GET.get('product'),
            'tag__name'         : request.GET.get('tag'),
            'allergy__name__in' : request.GET.getlist('allergy')
        }

        data    = {key: value for key, value in data.items() if value}
        product = Product.objects.filter(**data)

        if product.exists():
            products = [{   
                'id'       : product.id,
                'name'     : product.name_kr,
                'thumbnail': product.thumbnail,
                'tags'     : list(
                    Tag
                    .objects
                    .filter(product__id = product.id)
                    .values('name')
                )
            } for product in product.distinct()]

            return JsonResponse({'count': len(products), 'data': products}, status = 200)

        return JsonResponse({'message': 'NO_PRODUCT'}, status = 400)