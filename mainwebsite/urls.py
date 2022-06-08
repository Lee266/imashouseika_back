from django.urls import path
from mainwebsite import views

#http://127.0.0.1:8000/api/
urlpatterns = [
    path('post/', views.GalleryView.as_view(), name='Gallery'),
    path('post/<str:pk>/', views.GalleryDetailView.as_view(), name='post-detail'),
    path('news/', views.NewsView.as_view({'get': 'list', 'post':'list'}), name="News"),
    path('news/<str:pk>/', views.NewsDetailView.as_view(), name="news-detail"),
    path('send-email-user/', views.SendEmailUsersView.as_view(), name="SendEmailUser"),
    path('send-email-user/<str:pk>/', views.SendEmailUsersDetailView.as_view(), name="SendEmailUser-detail"),
    path('companies/', views.CompaniesView.as_view(), name="Companies"),
    path('companies/<str:pk>/', views.CompaniesDetailView.as_view(), name="companies-detail"),
]