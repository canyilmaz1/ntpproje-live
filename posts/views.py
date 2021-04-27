from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from django.shortcuts import render


class PostListView(LoginRequiredMixin, ListView):
	paginate_by = 10
	model = Post
	template_name = "post_list.html"
	login_url='login'
	ordering = ['-date','-id']

class PostResearchView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "post_research.html"
    login_url='login'

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "post_detail.html"
    login_url='login'

class PostUpdateView(LoginRequiredMixin, UpdateView):
	model = Post
	fields = ('title', 'body',)
	template_name = 'post_edit.html'
	login_url = 'login'	
	def dispatch(self, 	request, *args, **kwargs):
		obj = self.get_object()
		if obj.author != self.request.user and not self.request.user.is_superuser:
			return render(request, 'denied.html')
		return super().dispatch(request,*args, **kwargs)

class PostDeleteView(LoginRequiredMixin, DeleteView):
	model = Post
	template_name = 'post_delete.html'
	success_url = reverse_lazy('post_list')
	login_url = 'login'	
	def dispatch(self, request, *args, **kwargs):
		obj = self.get_object()
		if obj.author != self.request.user and not self.request.user.is_superuser:
			return render(request, 'denied.html')
		return super().dispatch(request, *args, **kwargs)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "post_new.html"
    fields=('title','body')
    login_url='login'

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)





