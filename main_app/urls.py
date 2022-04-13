from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='finches_index'),
    path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
    path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
    path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'),
    path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
    path('finches/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('finches/<int:finch_id>/assoc_study/<int:study_id>/', views.assoc_study, name='assoc_study'),
    path('finches/<int:finch_id>/unassoc_study/<int:study_id>/', views.unassoc_study, name='unassoc_study'),
    path('studys/', views.StudyList.as_view(), name='studys_index'),
    path('stuyds/<int:pk>/', views.StudyDetail.as_view(), name='studys_detail'),
    path('studys/create/', views.StudyCreate.as_view(), name='studys_create'),
    path('studys/<int:pk>/update/', views.StudyUpdate.as_view(), name='studys_update'),
    path('studys/<int:pk>/delete/', views.StudyDelete.as_view(), name='studys_delete'),
]