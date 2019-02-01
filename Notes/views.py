from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.base import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.template.response import TemplateResponse
# from .forms import SignUpForm, create_note_form, registrationForm, loginForm, update_note_form, reminder_form
from rest_framework.views import APIView

from .forms import create_note_form, reminder_form, update_note_form
from .models import Notes
from django.urls import reverse_lazy
from django.utils import timezone
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import json
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist


def create_note(request):
    """
    This method is used to create Note

    :param request:it is the request coming from user and
        this method is responsible to handle that request
    :return:this will render and return form
    """
    if request.method == "POST":

        """
        This will work  if the request is POST request
        if the request is post then we will the data with the form
        and create object of it
        """
        form = create_note_form(request.POST)

        """
        checking whether submitted form data is valid or not 
        """

        if form.is_valid():
            form.save()

        return redirect('show_notes')
    else:
        """
        if the request is other than POST then we will create blank form 
        and render it
         
        """
        form = create_note_form()
        return render(request, 'Notes/home.html', {'form': form})


def show_notes(request):
    """
    This method is used to display all Notes from database.

    :param request: it is the request coming from user and
        this method is responsible to handle that request
    :return: this will render and return form
    """

    # Here i am taking out all the notes from database
    # according to note '-created_time' but in descending order

    notes_obj = Notes.objects.all().order_by('-created_time')

    return render(request, 'users/base.html', {'notes_obj': notes_obj})


def note_edit(request, pk):

    """

    :param request:
    :param pk:
    :return:
    """
    note = Notes.objects.get(id=pk)
    print("note = ", note)
    print("id = ", note.id, '->', pk)
    # form = update_note_form(request.POST)
    # for name, value in request.POST.items()
    return render(request, 'Notes/note_update.html', {'note': note})


class note_update(UpdateView):
    def post(self, request, *args, **kwargs):
        print('----------------------------------')
        response_data = {}
        response_data['status'] = False
        if kwargs.get('pk', None):
            try:
                print(request.POST, 'mai hu')
                print(kwargs, 'mai hu kwargs')
                pk = kwargs.get('pk', None)
                print('i am pk', pk)
                obj = Notes.objects.get(pk=pk)
                obj.title = request.POST.get('title')
                obj.description = request.POST.get('description')
                obj.is_pinned = request.POST.get('is_pinned')
                obj.color = request.POST.get('color')
                obj.save()
                response_data['status'] = True
                response_data['message'] = "Updated Successfully"
                return redirect('show_notes')  # i have added to redirect after successful update
            except Exception.DoesNotExist as e:
                response_data['message'] = "Note doesnt exists"
            except Exception as e:
                response_data['message'] = 'something went wrong'

        else:
            response_data['message'] = "Missing note identifier (id)"
        return HttpResponse(json.dumps(response_data), content_type='application/json')

    def get(self, request, *args, **kwargs):
        print("in get call")
        response_data = {}
        for name, value in request.POST.items():
            print("name = ", name)  # dict.items()
            Notes(**dict([(name, value)])).save()
        response_data['status'] = False
        response_data['message'] = "Note not found.."
        return HttpResponse(json.dumps(response_data), content_type='application/json')




def note_delete(request, pk):
    note = Notes.objects.get(id=pk)
    print("note = >", note)
    return render(request, 'Notes/note_delete.html', {'note': note})




class note_delete_note(DeleteView):
    def post(self, request, *args, **kwargs):
        response_data = {}
        response_data['status'] = False
        if kwargs.get('pk', None):
            try:
                pk = kwargs.get('pk', None)
                obj = Notes.objects.get(pk=pk)
                print("obj => ", obj)
                obj.delete()
                response_data['status'] = True
                response_data['message'] = "Deleted Successfully"
                return redirect('show_notes')
            except Exception as e:
                response_data['message'] = "Note doesnt exists"
            except Exception as e:
                response_data['message'] = 'something went wrong'
        else:
            response_data['message'] = "Missing note identifier (id)"
        return HttpResponse(json.dumps(response_data), content_type='application/json')


# class note_reminder(CreateView):
#     model = Notes
#     form = reminder_form
#     fields = ['reminder']
#     template_name = 'Notes/note_reminder.html'

# def note_reminder(request,pk):
#     note=Notes.objects.get(id=pk)
#     return render(request,'Notes/note_reminder.html',{'note':note})


def note_reminder(request, pk):
    note = Notes.objects.get(id=pk)
    if request.method == 'POST':
        print(request.POST, 'Hii i am post wala')
        print(request.body, 'Hii i am body wala')
        print(request.POST.get('date'), 'Hii i am body wala')
        date = request.POST.get('date')
        note = Notes.objects.get(id=pk)
        note.reminder = date
        print(note.reminder, '---->note reminder')
        note.save()
        print(note, '--->', pk)

        return redirect('show_notes')
    return render(request, 'Notes/note_reminder.html', {'note': note})


# class reminder_save(View):
#
#     def post(self,request,*args,**kwargs):
#
#         date=request.body
#         print(date,'-----------',kwargs)
#         d=request.POST.get('date')
#         print(d)
#         return redirect('show_notes')
#
#
# def note_reminder(request,pk):
#
#     if request.method=='POST':
#         form=reminder_form(request.POST)
#     else:
#         form = reminder_form()
#     return render(request,'Notes/note_reminder.html',{'form':form})
#


# class note_colaborator(UpdateView):
#     model = Notes
#     fields = ['collaborate']
#     template_name = 'note_collaborate.html'


# -----pagination------------------

from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse


def index(request):
    notes = Notes.objects.all()[:5]
    print('hi->........notes', notes)
    return render(request, 'Notes/index.html', {'notes': notes})


def lazy_load_notes(request):
    page = request.POST.get('page')
    notes = Notes.objects.all()
    print(notes, '--------------------------------')
    # use Django's pagination
    # https://docs.djangoproject.com/en/dev/topics/pagination/
    results_per_page = 5
    paginator = Paginator(notes, results_per_page)
    try:
        notes = paginator.page(page)
    except PageNotAnInteger:
        notes = paginator.page(2)
    except EmptyPage:
        notes = paginator.page(paginator.num_pages)

    # build a html posts list with the paginated posts
    notes_html = loader.render_to_string('Notes/notes_list.html', {'notes': notes})

    # package output data and return it as a JSON object
    output_data = {'notes_html': notes_html, 'has_next': notes.has_next()}
    return JsonResponse(output_data)
    # return render(request, 'notes/notes_list.html', {{'notes': notes}})
