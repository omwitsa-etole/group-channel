from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import Video, Channel, User, Image, Comment, Question
from .forms import VideoForm, ImageForm, SignUpForm
from .forms import LoginForm, CommentForm, QuestionForm
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework import viewsets, parsers, permissions, status, authentication
from .serializers import ImageSerializer, VideoSerializer
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

def log_in(request):
    error = '';
    username = 'not logged in'
    video_list = Video.objects.all()
    if request.method == "POST":
        MyLoginForm = LoginForm(request.POST)
  
        if MyLoginForm.is_valid():
         username = MyLoginForm.cleaned_data['username']
         password = MyLoginForm.cleaned_data['password']
         user = authenticate(username=username, password=password)
         if user:
             login(request, user)
             request.session['username'] = username
             return render(request, 'indexhome.html', locals())
         else: 
            error = 'invalid username or passord';
       
    else:
      MyLoginForm = LoginForm()
        
    return render(request, 'login.html', locals())
    
def formView(request):
    error = '';
    search_query = request.GET.get('search')
    if request.session.has_key('username'):
        username = request.session['username']
        if search_query:
            video_list = Video.objects.filter(Q(title__icontains=search_query) & Q(description__icontains=search_query)).order_by("-date_created")
        else:
            video_list = Video.objects.all().order_by("-date_created")
        index = 0
    else:
        return render(request, 'login.html', {"error_log":error})
        
    return render(request, 'indexhome.html', locals())

def logout(request):
   try:
      del request.session['username']
   except:
      pass
   return HttpResponse("<strong>You are logged out.</strong><a href='/video/in/'>login </a>")
  
class SignUpView(View):
    form_class = SignUpForm
    initial = {'key': 'value'}
    template_name = 'signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'Account created for {username}')

        return render(request, self.template_name, {'form': form})
    
def SaveVideo(request):
    
    
    if saved == True:
        return HttpResponse("<strong>File Uploaded Succesfully.</strong><br><a href='/video/in/upload/'>back</a>")
    else:
        return HttpResponse("<strong>Failed.</strong><br><a href='/video/in/upload/'>back</a>")
    
class UserDetailView(LoginRequiredMixin, generic.DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'details.html'
    
def HomeView(request):
    error = '';
    search_query = request.GET.get('search')
    if request.session.has_key('username'):
        username = request.session['username']
        if search_query:
            video_list = Video.objects.filter(Q(title__icontains=search_query) & Q(description__icontains=search_query)).order_by("-date_created")
        else:
            video_list = Video.objects.all().order_by("-date_created")
        index = 0
    else:
        return render(request, 'login.html', {"error_log":error})
    
def IndexView(request):
    username = 'not loged in'
    search_query = request.GET.get('search')
    if search_query:
        video_list = Video.objects.filter(Q(title__icontains=search_query) & Q(description__icontains=search_query)).order_by("-date_created")
    else:
        video_list = Video.objects.all().order_by("-date_created")
    return render(request, 'index.html', {"username" : username, "video_list": video_list})

class VideoDetailOutView(generic.DetailView):
    model = Video
    context_object_name = 'query'
    template_name = 'video_detail_out.html'
    
class ImageDetailOutView(generic.DetailView):
    model = Image
    context_object_name = 'query'
    template_name = 'image_detail_out.html'

def VideoDetailView(request, pk):
    template_name = 'video_detail.html'
    query = get_object_or_404(Video, pk=pk)
    video_list = Video.objects.all().order_by("-date_created")
    comments = Comment.objects.all()
    new_comment = None
    username = request.session['username']
    
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.query = query
            new_comment.save()
    else:
        comment_form = CommentForm()
        
    return render(request, template_name, locals())
    
def ImageDetailView(request, pk):
    template_name = 'image_detail.html'
    query = get_object_or_404(Image, pk=pk)
    comments = Comment.objects.all()
    new_comment = None
    username = request.session['username']
    
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.query = query
            new_comment.save()
    else:
        comment_form = CommentForm()
        
    return render(request, template_name, locals())
    
class ImageViewset(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'upload2.html'
    
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = ImageSerializer()
        error = ''
        return Response({'serializer':serializer,'error':error})
        
    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = ImageSerializer(data=request.data)
        if not serializer.is_valid():
            error = 'upload failed'
            messages.success(request, f'Image Upload failed')
            return Response({'serializer':serializer,'error':error})   
        serializer.save()
        messages.success(request, f'Image Uploaded Successfully')
        error = 'upload success'
        return Response({'serializer':serializer,'error':error})
 
class VideoViewset(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'upload.html'
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = VideoSerializer()
        error = ''
        return Response({'serializer':serializer,'error':error})
        
    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = VideoSerializer(data=request.data)
        if not serializer.is_valid():
            error = 'upload failed'
            messages.success(request, f'Video Upload failed')
            return Response({'serializer':serializer,'error':error})   
        serializer.save()
        messages.success(request, f'Video Uploaded Successfully')
        error = 'upload success'
        return Response({'serializer':serializer,'error':error})
        
class FileUploadCompleteHandler(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.SessionAuthentication]
    
    def post(self, request, *args, **kwargs):
        file_id = request.POST.get('file')
        size = request.POST.get('fileSize')
        data = {}
        type_ = request.POST.get('fileType')
        if file_id:
            obj = FileItem.objects.get(id=int(file_id))
            obj.size = int(size)
            obj.uploaded = True
            obj.type = type_
            obj.save()
            data['id'] = obj.id
            data['saved'] = True
        return Response(data, status=status.HTTP_200_OK)
    
   
def Settings(request):
    if request.session.has_key('username'):
         username = request.session['username']
         return render(request, 'settings.html', {"username" : username})
    else:
      return render(request, 'login.html', {})
def PassView(request):
    if request.session.has_key('username'):
        username = request.session['username']
        return render(request, 'pass_set.html', {"username" : username})
    else:
        return render(request, 'login.html', {})
def DetailView(request):
    if request.session.has_key('username'):
        username = request.session['username']
        user = User.objects
        return render(request, 'details.html', {"username" : username,"user":user})
    else:
        return render(request, 'login.html', {})
def ImageView(request):
    if request.session.has_key('username'):
        username = request.session['username']
        search_query = request.GET.get('search') 
        if search_query:
            image_list = Video.objects.filter(Q(title__icontains=search_query) & Q(description__icontains=search_query)).order_by("-date_created")
        else:
            image_list = Image.objects.all().order_by("-date_created")
    else:
        return render(request, 'login.html', {}) 
        
    return render(request, 'images.html', {"username" : username,"image_list":image_list})
def ImageOutView(request):
    username = "not logged in"
    search_query = request.GET.get('search') 
    if search_query:
        image_list = Image.objects.filter(Q(title__icontains=search_query) & Q(description__icontains=search_query)).order_by("-date_created")
    else:
        image_list = Image.objects.all().order_by("-date_created")
        
    return render(request, 'images_out.html', {"username" : username,"image_list":image_list})
def QuestionView(request):
    error = '';
    saved =False
    search_query = request.GET.get('search')
    if request.session.has_key('username'):
        username = request.session['username']
        if search_query:
            question_list = Question.objects.filter(Q(question__icontains=search_query) & Q(more_description__icontains=search_query)).order_by("-date_created")
        else:
            question_list = Question.objects.all().order_by("-date_created")
        index = 0
    else:
        return render(request, 'login.html', {"error_log":error})
        
    if request.method == "POST":
        MyQuestionForm = QuestionForm(request.POST, request.FILES) 
        if MyQuestionForm.is_valid():
            new_question=MyQuestionForm.save(commit=False)
            new_question.save()
            saved = True
        else:
            MyQuestionForm = QuestionForm()
    
        
    return render(request, 'questions.html', locals())
def QuestionOutView(request):
    error = '';
    new_question = None
    search_query = request.GET.get('search')
    username = "not logged in"
    if search_query:
        question_list = Question.objects.filter(Q(question__icontains=search_query) & Q(more_description__icontains=search_query)).order_by("-date_created")
    else:
        question_list = Question.objects.all().order_by("-date_created")
    index = 0
    
    return render(request, 'questionsout.html', locals())
    
def QuestionDetailView(request, pk):
    template_name = 'q&adetail.html'
    question = get_object_or_404(Question, pk=pk)
    answers = Comment.objects.all()
    new_answer = None
    username = request.session['username']
    
    if request.method == 'POST':
        answer_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_answer = comment_form.save(commit=False)
            new_answer.question = question
            new_answer.save()
    else:
        answer_form = CommentForm()
        
    return render(request, template_name, locals())
class QuestionDetailOutView(generic.DetailView):
    model = Question;
    context_object_name = "question";
    template_name = "q&adetailout.html"
def ForgotPass(request):
        return render(request, 'password_reset.html', {})
class ChannelDetailView(generic.DetailView):
    model = Channel
    
class UploadsListView(generic.ListView):
    model = Video

