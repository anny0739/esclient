from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^bulk/(?P<index_nm>\w+)$', views.bulk, name='bulk'),
    # url(r'^check/(?P<index_nm>\w+)$', views.chk_cluster, name='chk_cluster'),
    url(r'^search/(?P<index_nm>\w+)$', views.search, name='search'),

]