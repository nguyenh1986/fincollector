from django.shortcuts import render, redirect
import logging

# Add the following import
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Finch, Study
from .forms import FeedingForm

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  finches = Finch.objects.all()
  return render(request, 'finches/index.html', { 'finches': finches })

def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  feeding_form = FeedingForm()
  id_list = finch.studys.all().values_list('id')
  studys_finch_doesnt_have = Study.objects.exclude(id__in=id_list)
  logging.warning(studys_finch_doesnt_have)
  return render(request, 'finches/detail.html', { 'finch': finch, 
  'feeding_form': feeding_form,
  'studys': studys_finch_doesnt_have
  })

class FinchCreate(CreateView):
  model = Finch
  fields = ['name', 'type', 'description', 'age']
  fields = '__all__'

class FinchUpdate(UpdateView):
  model = Finch
  fields = ['type', 'description', 'age']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches/'

def add_feeding(request, finch_id):
  # create a ModelForm instance using the data in the posted form
  form = FeedingForm(request.POST)
  # validate the data
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('detail', finch_id=finch_id)

class StudyList(ListView):
  model = Study

class StudyDetail(DetailView):
  model = Study

class StudyCreate(CreateView):
  model = Study
  fields = '__all__'

class StudyUpdate(UpdateView):
  model = Study
  fields = ['topic']

class StudyDelete(DeleteView):
  model = Study
  success_url = '/studys/'

def assoc_study(request, finch_id, study_id):
  Finch.objects.get(id=finch_id).studys.add(study_id)
  return redirect('detail', finch_id=finch_id)

def unassoc_study(request, finch_id, study_id):
  Finch.objects.get(id=finch_id).studys.remove(study_id)
  return redirect('detail', finch_id=finch_id)