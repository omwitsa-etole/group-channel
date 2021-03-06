from django.urls import path, reverse_lazy
from django.views.generic import TemplateView
from .import views
from django.contrib.auth import views as auth_views
from data.views import ImageViewset, VideoViewset, FileUploadCompleteHandler
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
urlpatterns = router.urls

urlpatterns = [
    path('out/videos/', views.IndexView,name='index_out'),
    path('in/videos/', views.HomeView,name='index'),
    path('out/', views.IndexView, name='video_out'),
    path('out/images/', views.ImageOutView,name='image_out_view'),
    path('out/images/<int:pk>/', views.ImageDetailOutView.as_view(),name='image_detail_out'),
    path('out/questions/', views.QuestionOutView, name='questions_out'),
    path('in/questions/', views.QuestionView, name='questions_in'),
    path('in/questions/<int:pk>/', views.QuestionDetailView, name='questions_url_in'),
    path('out/questions/<int:pk>/', views.QuestionDetailOutView.as_view(), name='questions_url_out'),
    path('in/forgetpass/',auth_views.PasswordResetView.as_view(
             template_name='password_reset.html',
             subject_template_name='password_reset_subject.txt',
             email_template_name='password_reset_email.html',
              success_url=reverse_lazy('login')
         ),name='forgot_pass'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
    path('in/images/', views.ImageView,name='image_view'),
    path('in/images/<int:pk>/', views.ImageDetailView,name='image_detail'),
    path('in/', views.formView, name='loginform'),
    path('in/signup', views.SignUpView.as_view(), name='sign_up'),
    path('out/videos/<int:pk>/', views.VideoDetailOutView.as_view(), name='video_detail_out'),
    path('in/videos/<int:pk>/', views.VideoDetailView, name='video_detail'),
    path('in/login/', views.log_in, name='login'),
    path('in/settings/', views.Settings, name="my_settings"),
    path('in/settings/password/', views.PassView, name="pass_set"),
    path('in/settings/details/', views.DetailView, name="details"),
    path('logout/', views.logout, name='logout'),
    path('in/upload/video/<int:pk>', VideoViewset.as_view(), name="upload_video"),
    path('api/files/policy/<int:pk>', VideoViewset.as_view(), name='upload_policy'),
    path('api/files/complete/<int:pk>', FileUploadCompleteHandler.as_view(), name='upload_complete'),
    path('in/upload/image/<int:pk>', views.ImageViewset.as_view(), name="upload_image"),
    path('channels/<int:id>/', views.ChannelDetailView.as_view(), name='channel_detail'),
]+ router.urls