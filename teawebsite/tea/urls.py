# add patterns here later
from django.conf.urls import url
from django.conf import settings
from django.contrib.staticfiles.urls import static

from .import views


urlpatterns = [
    # for the home page
    url(r'^$', views.index, name='index'),
    # for the Teas page
    url(r'^teas/$', views.TeaListView.as_view(), name='teas'),
    # for the Tea Description page
    url(r'^teas/(?P<pk>\d+)$', views.TeaDetailView.as_view(), name='tea-detail'),
               
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

