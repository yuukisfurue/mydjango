from django.urls import path
from . import views
from .views import MemberList
from .views import MemberDetail

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('edit/<int:num>', views.edit, name='edit'),
    path('delete/<int:num>', views.delete, name='delete'),
    path('list', MemberList.as_view()), #☆
    path('detail/<int:pk>', MemberDetail.as_view()), #☆
    path('find', views.find, name='find'), 
    path('<int:num>', views.index, name='index'),
    path('export/', views.csv_export, name='csv_export'),
]