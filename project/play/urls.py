from django.urls import path, include
from .views import *

app_name = "play"

urlpatterns = [
    ## services urls
    path('', rentListView.as_view(), name='rent_list',),
    path('create/', rentCreateView.as_view(), name='rent_create'),
    path('<int:pk>/update/', rentUpdateView.as_view(), name='rent_update'),
    # path('delete/<int:pk>', ServiceDeleteView.as_view(), name='rent_delete'),

    ##  RENT ORDERS URLS 
    path('rent/<int:pk>/orders/', rentOrderListView.as_view(), name='rent_order_list',),
    path('rent/orders/create/', rentOrderCreatView.as_view(), name='rent_order_create'),
]