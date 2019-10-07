"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf import settings

from my_app.views import index, MyView

urlpatterns = [

    url(r'^admin/', admin.site.urls),

    # custom urls:
    url(r'^form/', MyView.as_view(), name='form'),
    url(r'^$', index, name='index'),
]

# This urlconf is for development use only:
# if settings.DEBUG:
#     # Media files serving:
#     from django.conf.urls.static import static
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
