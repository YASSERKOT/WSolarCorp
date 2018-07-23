from django.conf.urls import url, include
from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateUserView
from .views import CreateLayerView
from .views import showRegions
from .views import showFiltredRegions

urlpatterns = {
    url(r'regions/$', showRegions),
    path(r'regions/<arg>/', showFiltredRegions),
    url(r'users/$', CreateUserView.as_view()),
    url(r'users/layers/$', CreateLayerView.as_view()),
}

urlpatterns = format_suffix_patterns(urlpatterns)