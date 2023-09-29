from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from .forms import TaskCreateForm
from django.db.models import Q

# Task List View

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = Task.objects.all()
        
        # Get filter parameters from URL query parameters
        title_query = self.request.GET.get('title')
        priority_query = self.request.GET.get('priority')
        completed_query = self.request.GET.get('completed')
        
        # Apply filters based on query parameters
        if title_query:
            queryset = queryset.filter(title__icontains=title_query)
        
        if priority_query:
            queryset = queryset.filter(priority=priority_query)
        
        if completed_query in ['True', 'False']:
            queryset = queryset.filter(completed=(completed_query == 'True'))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Pass filter parameters to the template
        context['title_query'] = self.request.GET.get('title', '')
        context['priority_query'] = self.request.GET.get('priority', '')
        context['completed_query'] = self.request.GET.get('completed', '')
        
        return context

# Task Create View

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = 'task_create.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# Task Update View
class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'task_update.html'
    form_class = TaskCreateForm  # Use the modified TaskForm
    success_url = reverse_lazy('task_list')
# Task Delete View
class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('task_list')

# Task Detail View
class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'

