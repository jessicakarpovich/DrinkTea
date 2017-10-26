"""teawebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
# include allows me to use URLS from tea
from django.conf.urls import include
# by using RedirectView I can change the base URL of my website
from django.views.generic import RedirectView
# the following two imports allow me to serve static files
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

"""
    The following pattern is super important to be able to add images through the admin page
    and then display them to the user.
    It checks for the files in the imgs folder and allows saved images to load, regardless of file extension. Should only be used in production.
    
    url(r'^imgs/(?P<path>.*)$', serve, {
    'document_root': settings.MEDIA_ROOT }),
    """

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tea/', include('tea.urls')),
    url(r'^$', RedirectView.as_view(url='/tea/', permanent=True)),
               
   # the following line enambles me to serve static files, images
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


