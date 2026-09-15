from django.urls import path

from .views import ClothingItemListCreateView


urlpatterns = [
    path(
        "clothing-items/",
        ClothingItemListCreateView.as_view(),
        name="clothing-item-list-create",
    ),
]