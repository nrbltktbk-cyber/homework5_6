from django.urls import path  
from orders.views import CreateOrderView, OrderListView, UpdateOrderView, DeleteOrderView

urlpatterns = [
    path('create_order/', CreateOrderView.as_view()),
    path('order_list/', OrderListView.as_view()),
    path('order_list/<int:id>/update/', UpdateOrderView.as_view()),
    path('order_list/<int:id>/delete/', DeleteOrderView.as_view()),
]