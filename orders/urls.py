from django.urls import path

from .views import (
    ClothingItemDetailView,
    ClothingItemListCreateView,
    OrderDetailView,
    OrderItemListCreateView,
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
    path(
        "<int:pk>/",
        OrderDetailView.as_view(),
        name="order-detail",
    ),
    path(
    "items/",
    OrderItemListCreateView.as_view(),
    name="order-item-list-create",
),
]