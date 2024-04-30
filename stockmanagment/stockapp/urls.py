from django.urls import path
from .views import ListView, updateView, delete,AddView,RegisterView,LoginView,logoutView

urlpatterns = [
    path('listview/', ListView.as_view(), name='list_view'),
    path('logout/', logoutView.as_view(), name='logout_view'),
    path('addlist/', AddView.as_view(), name='add_list'),
    path('updateview/<int:pk>/', updateView.as_view(), name='update_view'),
    path('deleteview/<int:pk>/', delete.as_view(), name='delete_view'),
    path('register/', RegisterView.as_view(), name='registraion_view'),
     path('',LoginView.as_view(), name='login_view'),
    # path('deleteview/<int:pk>/', delete.as_view(), name='registraion_view'),
]
