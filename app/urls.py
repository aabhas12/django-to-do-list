"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls.static import static
from app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^$', views.lists, name='list'),
                  url(r'^login/$', auth_views.login,{'template_name': 'login.html'}, name='login'),
                  url(r'^signup/$', views.signup, name='signup'),
                  url(r'^logout/$', views.log_out, name='logout'),

                  url(r'^lists/create/$', views.create, name='create'),
                  url(r'^lists/edit/(\d+)/', views.editlist, name='editlist'),
                  url(r'^lists/view/(\d+)/', views.viewlist, name='viewlist'),
                  url(r'^lists/view/markcom/(\d+)/', views.martaskcomplete, name='martaskcom'),
                  url(r'^lists/view/markincom/(\d+)/', views.martaskincomplete, name='martaskincom'),
                  url(r'^lists/deltask/(\d+)/', views.deletetask, name='del1task'),
                  url(r'^lists/edittask/(\d+)/', views.edittask, name='edittask'),
                  url(r'^lists/viewtask/(\d+)/', views.view1task, name='view1task'),
                  url(r'^lists/delete/(\d+)/', views.deletelist, name='deletelist'),
                  url(r'^lists/add_task/(\d+)/', views.createtask, name='createtask'),
                  url(r'^lists/add_comment/(\d+)/', views.createcomment, name='createcom'),


                 # url(r'^lists/', views.lists, name='list'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
