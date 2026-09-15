from django.urls import path

from .views import (
    ClothingItemDetailView,
    ClothingItemListCreateView,
    OrderListCreateView,
)


urlpatterns = [
    path(
        "clothing-items/",
        ClothingItemListCreateView.as_view(),
        name="clothing-item-list-create",
    ),
    path(
        "clothing-items/<int:pk>/",
        ClothingItemDetailView.as_view(),
        name="clothing-item-detail",
    ),
    path(
        "",
        OrderListCreateView.as_view(),
        name="order-list-create",
    ),
]