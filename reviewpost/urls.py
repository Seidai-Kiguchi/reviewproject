from .views import signupview, loginview, listview, detailview, CreateClass, logoutview, evaluationview, DeleteClass
from django.urls import path

urlpatterns = [
    path("signup/", signupview, name="signup"),
    path('login/', loginview, name="login"),
    path("list/", listview, name="list"),
    path("detail/<int:pk>/", detailview, name="detail"),
    path("create/", CreateClass.as_view(), name="create"),
    path("logout/", logoutview, name="logout"),
    path('evaluation/<int:pk>/',evaluationview, name='evaluation'),
    path("delete/<int:pk>/",DeleteClass.as_view(), name='delete'),
]
