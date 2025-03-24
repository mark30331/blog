"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',include('blog.urls', namespace='blog')), #Namespaces have to be unique across your entire project. Later, 
    # you will refer to your blog URLs easily by using the namespace followed by a colon and the URL name, for example, blog:post_list
    # app_namespace will be the default application namespace when provided in include(). If app_namespace is not provided, then it will 
    # look for app_name in blog/urls.py and that will be the default namespace.

]
