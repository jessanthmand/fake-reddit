"""fake_reddit_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.FrontendAppView.as_view()), #New URL for the index route
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('fake_reddit.urls')),
    # path('accounts/signup/', tunr_views.sign_up, name='signup'),

    # path('api/v1/', include('fake_reddit.urls')),
]


# from django.contrib import admin
# from django.urls import path, include
# from tunr import views as tunr_views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('tunr.urls')),
#     path('accounts/', include('django.contrib.auth.urls')),
#     path('accounts/signup/', tunr_views.sign_up, name='signup'),
# ]
