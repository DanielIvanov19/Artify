from django.urls import path
from . import views

urlpatterns = [
    path('order/tshirt/', views.TShirtOrderView.as_view(), name='tshirt_order_form'),
    path('order/accessories/', views.AccessoriesOrderView.as_view(), name='accessories_order_form'),
    path('order/canvas/', views.CanvasOrderView.as_view(), name='canvas_order_form'),
    path('my_orders/', views.MyOrdersView.as_view(), name='my_orders'),
]
