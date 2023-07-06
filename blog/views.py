from django.views import generic
from django.contrib.auth import authenticate,login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views import View
from django.shortcuts import render
from .forms import RegistrationForm
from django.core.paginator import Paginator
from .models import Post,Comment,Like
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout




class home(LoginRequiredMixin,generic.ListView):
    template_name = "home.html"

    model = Post
    context_object_name = "posts"
    paginate_by = 5



class PostDetailView(LoginRequiredMixin,generic.DetailView):
    model = Post
    template_name = "detial.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.object)
        context['likes'] = Like.objects.filter(post=self.object)
        return context
    


class UserLoginView(View):
    template_name='auth/login.html'

    def get(self,request):
        return render (request,self.template_name)
    
    def post(self,request):
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            error_message='Invalid login credentials'
            return render(request,self.template_name,{'error_message':error_message})
        


class RegisterView(generic.FormView):
    template_name = 'auth/register.html'
    form_class = RegistrationForm
    success_url = '/login'  

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



@login_required
@csrf_exempt
def comment_submit(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        comment = request.POST.get('comment')
        post = get_object_or_404(Post, pk=post_id)
        Comment.objects.create(post=post, user=request.user, content=comment)
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})
    


@login_required
@csrf_exempt
def like_submit(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        Like.objects.create(post=post, user=request.user)
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})
    


def logout_view(request):
    logout(request)
    return redirect('login') 