from django.urls import path
from .views      import (
    CityView,
    DistrictView,
    StoreSearchView,
    StoreDetailView,
    FavoriteStoreView
    )


urlpatterns = [
    path('/cities', CityView.as_view()),
    path('/districts', DistrictView.as_view()),
    path('/stores', StoreSearchView.as_view()),
    path('/<int:store_id>', StoreDetailView.as_view()),
    path('/favorites/<int:store_id>', FavoriteStoreView.as_view())
]