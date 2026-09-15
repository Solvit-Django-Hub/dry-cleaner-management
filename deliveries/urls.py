from django.urls import path

from .views import DeliveryDetailView, DeliveryListCreateView


urlpatterns = [
    path(
        "",
        DeliveryListCreateView.as_view(),
        name="delivery-list-create",
    ),
    path(
        "<int:pk>/",
        DeliveryDetailView.as_view(),
        name="delivery-detail",
    ),
]