from django.urls import path

from . import views

urlpatterns = [
    path('cryptohome',views.cryptohome,name='cryptohome'),
    path('index', views.index, name='index'),
    path('predCrypt', views.predCrypt, name='predCrypt'),
    path('contact', views.contact, name='contact'),
    path('add_crypto', views.add_crypto, name="add_crypto"),
    path('delete/<crypto_id>', views.delete, name="deletecrypto"),
   ]