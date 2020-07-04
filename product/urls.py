from django.urls import path
from .views      import (
    CategoryView,
    ProductDetailView,
    SizeView,
    BestFlavorView,
    SearchBarView,
    ProductSearchView
)


urlpatterns = [
    path('/categories', CategoryView.as_view()),
    path('/<int:product_id>', ProductDetailView.as_view()),
    path('/sizes', SizeView.as_view()),
    path('/bests', BestFlavorView.as_view()),
    path('/searchbar', SearchBarView.as_view()),
    path('/products', ProductSearchView.as_view())
]