from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^categories$', views.categories, name="categories"),
    url(r'^result$', views.result, name="result"),
]