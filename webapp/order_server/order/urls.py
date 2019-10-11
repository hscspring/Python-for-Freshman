from django.urls import path

from order import views


urlpatterns = [
    path('orders/', views.ListOrderView.as_view(), name='order_index'),
    path('orders/<int:pk>/', views.DetailOrderView.as_view(), name='order_detail'),
    path('food/', views.ListFoodView.as_view(), name='food_index'),
    path('food/<int:pk>/', views.DetailFoodView.as_view(), name='food_detail'),
    path('show_menu/', views.ShowMenuView.as_view(), name='show_menu'),
    path('submit_order/', views.SubmitView.as_view(), name='submit'),
]
