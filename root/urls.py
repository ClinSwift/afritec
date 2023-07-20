from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .import views


app_name = 'root'

urlpatterns =[
path('', views.index, name = 'index'),
path('register/', views.register_view, name = 'register'),
path('login/', views.login_view, name = 'login'),
path('logout/', views.logout_view, name = 'logout'),

path('dashboard/', views.home, name = 'dashboard'),
path('make_complaint/', views.make_complaint,name='make_complaint'),
path('complaint_history/', views.complaint_history,name='complaint_history'),
path('orders/', views.orders, name = 'my_orders'),

path('dealers/', views.shop_list, name = 'dealers'),
path('store/', views.itemstore, name = 'store'),
path('contacts/', views.contacts, name = 'contacts'),
path('about/', views.about, name = 'about'),
path('cart/', views.cart, name="cart"),
path('checkout/', views.checkout, name="checkout"),
path('update_item/', views.updateItem, name="update_item"),
path('process_order/',views.processOrder, name="process_order"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)