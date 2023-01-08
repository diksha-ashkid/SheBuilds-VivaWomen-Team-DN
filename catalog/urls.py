from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.UsersList.as_view(), name='users'),
    path('users/<int:pk>', views.UsersDetail.as_view(), name='user-detail'),
    path('users/emergency', views.emergency, name='emergency'),
    path('users/services', views.services, name='services'),
    path('users/map', views.map, name='map'),
    path('users/schemes', views.schemes, name='schemes'),
    path('users/community', views.community, name='community'),


]

urlpatterns += [
    path('users/create/', views.UsersCreate.as_view(), name='user-create'),
    path('users/<int:pk>/delete/', views.UsersDelete.as_view(), name='user-delete')
]
