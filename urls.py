from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.compare, name='compare'),
    url(r'^submit$', views.compare_products, name='compare_products'),
    url(r'^jsontomodel$', views.jsontomodel, name='jsontomodel'),
    url(r'^api/products$', views.get_product_names, name="get_product_names")
]
