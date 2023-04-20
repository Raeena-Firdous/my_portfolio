from django.contrib import admin
from django.urls import path
from . import views

#Django admin header customization

admin.site.site_header = "login to developer raeena"
admin.site.site_title = "Welcome to raeena's Dashboard"
admin.site.index_title = "Welcome to this Portal"

urlpatterns = [
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('project',views.project,name='project'),
    path('contact',views.contact,name='contact'),
    path('education',views.education,name='education'),
    path('skills',views.skills,name='skills'),
    path('internships',views.internships,name='internships'),


]