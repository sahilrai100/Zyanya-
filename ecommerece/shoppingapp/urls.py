from django.urls import path
from shoppingapp import views

urlpatterns=[
    path('',views.home,name="home"),
    path('register/',views.regiter,name="register"),
    path('login/',views.login_view,name="login"),
    path('logout/',views.logout_view,name="logout"),
    path('profile/',views.profile,name="profile"),
    path('forgetpassword/',views.forgetpassword,name="forgetpassword"),
    path('<int:pk>/', views.SectionDetailView.as_view(), name='detail'),
    path('about/', views.about.as_view(), name='about'),
    path('cart/', views.cart_view, name='cart'),
    path('validation/',views.validation,name="validation"),
    path('cart/add/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('productdetails/<int:pk>/',views.moredetails.as_view(),name="moredetails"),
    path('cart/add_quantity/<int:id>/', views.add_quantity, name='add_quantity'),
    path('cart/subtract_quantity/<int:id>/', views.subtract_quantity, name='subtract_quantity'),
    path('cart/remove_item/<int:id>/', views.remove_item, name='remove_item'),
    path('checkout',views.checkout,name="checkout"),
    path('orderplaced',views.orderplaced,name="orderplaced"),
    path('wishlist',views.wishlist,name="wishlist")

]