from django.urls import path
from . import views




urlpatterns = [
    path('',views.home.as_view(),name='home'),
     path('post/<int:pk>/',views.PostDetailView.as_view(), name='post-detail'),
    path('login/',views.UserLoginView.as_view(),name='login'),
    path('register/',views.RegisterView.as_view(), name='register'),
     path('comment-submit/',views.comment_submit, name='comment-submit'),
    path('like-submit/', views.like_submit, name='like-submit'),
    path('logout/', views.logout_view, name='logout'),
]
