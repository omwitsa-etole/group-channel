from django import forms
from .models import User, Comment, Video, Image, Question
from django.contrib.auth.forms import UserCreationForm
   
class LoginForm(forms.Form):
   username = forms.CharField(max_length = 100)
   password = forms.CharField(widget = forms.PasswordInput())
   
class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
   
class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('upload','title','description')
      
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('picture','title','description')
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('commenting',)
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question','more_description')
