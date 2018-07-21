from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateUserView
from .views import CreateLayerView

urlpatterns = {
    url(r'^users/$', CreateUserView.as_view(), name="create"),
    url(r'^users/layers/$', CreateLayerView.as_view(), name="create"),
}

urlpatterns = format_suffix_patterns(urlpatterns)