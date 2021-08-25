from django.urls import path
from jobs import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('jobs/<str:pk>/', views.jobsview, name='jobs'),
    path('companies/', views.companies, name='companies'),
    path('companies_detail/<str:pk>/',
         views.companiesDetailview, name='companies_detail'),
    path('applicant-register/', views.applicant_register,
         name='applicant-register'),
    path('applicant-login/', views.applicant_login, name='applicant-login'),
    path('applicant-logout/', views.applicant_logout, name='applicant-logout'),
    #path('application/<str:pk>/', views.applicationCreate,name='application-create'),


]
