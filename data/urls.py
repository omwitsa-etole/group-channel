from django.urls import path 
from django.views.generic import TemplateView
from .import views

urlpatterns = [
    path('out/videos/', views.IndexView,name='index_out'),
    path('in/videos/', views.formView,name='index'),
    path('out/', views.IndexView, name='video_out'),
    path('out/images/', views.ImageOutView,name='image_out_view'),
    path('out/images/<int:pk>/', views.ImageDetailOutView.as_view(),name='image_detail_out'),
    path('out/questions/', views.QuestionOutView, name='questions_out'),
    path('in/questions/', views.QuestionView, name='questions_in'),
    path('in/questions/<int:pk>/', views.QuestionDetailView, name='questions_url_in'),
    path('out/questions/<int:pk>/', views.QuestionDetailOutView.as_view(), name='questions_url_out'),
    path('in/forgetpass/', views.ForgotPass,name='forgot_pass'),
    path('in/images/', views.ImageView,name='image_view'),
    path('in/images/<int:pk>/', views.ImageDetailView,name='image_detail'),
    path('in/', views.formView, name='loginform'),
    path('in/signup', views.SignUpView, name='sign_up'),
    path('out/videos/<int:pk>/', views.VideoDetailOutView.as_view(), name='video_detail_out'),
    path('in/videos/<int:pk>/', views.VideoDetailView, name='video_detail'),
    path('in/login/', views.log_in, name='login'),
    path('in/settings/', views.Settings, name="my_settings"),
    path('in/settings/password/', views.PassView, name="pass_set"),
    path('in/settings/details/', views.DetailView, name="details"),
    path('logout/', views.logout, name='logout'),
    path('in/upload/video/', views.UploadView, name="upload_video"),
    path('in/upload/image/', views.SaveImage, name="upload_image"),
    path('channels/<int:id>/', views.ChannelDetailView.as_view(), name='channel_detail'),
   # path('user/<int:pk>', views.UserDetailView.as_view(), name='user-detail'),
]