from django.shortcuts import render
from django.views.generic import ListView,CreateView,DeleteView,UpdateView,DetailView
from .models import *
from .forms import StudentForm
# Create your views here.
# def base(request):
#     return render(request,'base.html')

class StundetListView(ListView):
    model = Student
    template_name = 'index.html'
    context_object_name = 'student'


class StudentCreateView(CreateView):
    model = Student
    fields = "__all__"
    template_name = 's_create.html'
    success_url = '/'
class DeleteView(DeleteView):
    model = Student
    template_name = 's_delete.html'
    success_url = '/'
    context_object_name = 'student'
class UpdateView(UpdateView):
    model = Student
    template_name ='s_update.html'
    form_class = StudentForm
    context_object_name = 'student'
    success_url = '/'

class DetailView(DetailView):
    model = Student
    template_name = 's_detail.html'
    context_object_name = 'd_student'
    