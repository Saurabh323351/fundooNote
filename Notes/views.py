"""
views.py

    This is responsible to handle each request which is send by user.
        Actually when request comes to the django ,it send it to the urls.py
        and urls.py send that request to views.py to handle that request and
        return proper response.

:return it returns desired response to each request

Author: Saurabh Singh

Since : 4 Feb , 2019
"""
import jwt
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpRequest
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.base import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.template.response import TemplateResponse
# from .forms import SignUpForm, create_note_form, registrationForm, loginForm, update_note_form, reminder_form
from rest_framework.exceptions import AuthenticationFailed
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
from Labels.models import Labels, MapLabels


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
        form = create_note_form(request.POST or None, request.FILES or None)

        print(form, '===============>form_obj')
        img = request.FILES
        data = request.POST
        print(img, '==========>img')
        print(data, '==========>data')
        """
        checking whether submitted form data is valid or not 
        """

        if form.is_valid():

            # p=request.POST
            # print(p,'------------>p')
            # is_pinned = request.POST.get('is_pinned')
            # # is_pinned_no=request.POST.get('is_pinned_no')
            title = request.POST.get('title')
            description = request.POST.get('description')
            color = request.POST.get('color')
            # is_archived = request.POST.get('color')
            # print(is_pinned, ' --> is_pinned')
            # # print(is_pinned_no, ' --> is_pinned_no')
            # print(title, ' --> title')
            # print(description, ' --> description')
            # print(color, ' --> color')
            #
            image = request.FILES.get('image')

            #
            print(image, '============>image')

            is_exists = Notes.objects.filter(title=title, description=description).exists()
            if is_exists is not True:
                k = form.save()

                print(k, '=========>k')

                k.user = request.user
                k.save()

            #     print(f, '======>f')
            #     f.user = request.user
            #     f.is_pinned = is_pinned
            #     f.title = title
            #     f.description = description
            #     f.color = color
            #     f.image=image
            #
            #     f.save()
            #     # print(f.is_pinned, '------>')

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

    # notes_obj = Notes.objects.all().order_by('-created_time')
    user = request.user

    print(user, '=========>user')
    notes_obj = Notes.objects.filter(is_archived=False, is_pinned=False, trash=False, user=user).order_by('-created_time')

    all_notes = Notes.objects.all()

    note_list = []
    for note_obj in all_notes:

        list_note_users = note_obj.collaborate.all()
        # print(list_note_users, '==========>list_note_users')

        for users in list_note_users:

            if users == request.user:
                note_list.append(note_obj.id)
                # notes_obj.append(note_obj)
                # print(note_list,'note_list=================>')

        collaborator_notes = Notes.objects.filter(pk__in=note_list)
        # print(collaborator_notes, '===========>collaborator_notes')

        records = (notes_obj | collaborator_notes).distinct()  # Here i am taking Union of two Queryset to get objects from both the Queryset

        # print(records, '==============>records')

    pin_notes = Notes.objects.filter(is_pinned=True, trash=False).order_by('-created_time')
    # print(pin_notes, '-->', 'pin_notes')

    # labels_object=Labels.objects.exclude(note_id=None)

    map_label_obj = MapLabels.objects.all()

    # print(map_label_obj, '------------------->map')
    # l_note_obj=map_label_obj[0].note_id
    # print(l_note_obj,'===========>')

    # labels_object2=Labels.objects.all()
    # l=labels_object2.__contains__(labels_object1)==False

    # Name.objects.exclude(alias__isnull=True)
    #
    # Name.objects.exclude(alias__isnull=True).exclude(alias__exact='')

    # print(labels_object,"labels_object====>")
    # print(labels_object[0].label)

    context = {'notes_obj': records,
               'pin_notes': pin_notes,

               'map_label_obj': map_label_obj,

               }
    return render(request, 'users/dashboard.html', context=context)


def note_edit(request, pk):
    """

    :param request:
    :param pk:get id of particular note to edit
    :return:it will render html file
    """
    note = Notes.objects.get(id=pk)
    print("note = ", note)
    print("id = ", note.id, '->', pk)
    # form = update_note_form(request.POST)
    # for name, value in request.POST.items()
    return render(request, 'Notes/note_update.html', {'note': note})


class note_update(UpdateView):
    """
    This method is used to update note information
    """

    def post(self, request, *args, **kwargs):
        """
        This will accept POST request to update note information

        :param request: POST request
        :param args: optional
        :param kwargs: it will provide pk of note
        :return: it will return json response
        """
        print('----------------------------------')
        response_data = {}
        response_data['status'] = False
        if kwargs.get('pk', None):
            try:
                print(request.POST.get('color'), 'mai hu============>')
                print(request.POST.get('title'), 'mai hu============>')
                print(request.POST.get('description'), 'mai hu============>')
                print(request.POST.get('is_pinned'), 'mai hu============>')
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
        """
        This will accept GET request to provide note information

        :param request: GET request
        :param args: optional
        :param kwargs:optional
        :return: it will return json response
        """

        print("in get call")
        response_data = {}
        for name, value in request.POST.items():
            print("name = ", name)  # dict.items()
            Notes(**dict([(name, value)])).save()
        response_data['status'] = False
        response_data['message'] = "Note not found.."
        return HttpResponse(json.dumps(response_data), content_type='application/json')


def note_delete(request, pk):
    """
    This function is used to render particular note
    html file

    :param request:POST
    :param pk: pk of particular note
    :return: render
    """
    note = Notes.objects.get(id=pk)
    print("note = >", note)
    return render(request, 'Notes/note_delete.html', {'note': note})


class note_delete_note(DeleteView):
    """
    This class based view is used to delete particular Note

    """

    def post(self, request, *args, **kwargs):

        """
        This will accept POST request to delete Note

        :param request: POST request
        :param args: optional
        :param kwargs: it will provide pk of note
        :return: it will return json response
        """

        response_data = {}
        response_data['status'] = False
        if kwargs.get('pk', None):
            try:
                pk = kwargs.get('pk', None)
                obj = Notes.objects.get(pk=pk)
                print("obj => ", obj)

                if obj.trash is False:
                    obj.trash = True
                    obj.save()

                else:
                    obj.trash = False
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


def show_trash_notes(request):
    """
    This function is used to display trash notes

    :param request:request from user
    :return: render html file
    """

    notes = Notes.objects.filter(trash=True).order_by('-created_time')

    return render(request, 'users/dashboard.html', {'notes_obj': notes})


# class note_reminder(CreateView):
#     model = Notes
#     form = reminder_form
#     fields = ['reminder']
#     template_name = 'Notes/note_reminder.html'

# def note_reminder(request,pk):
#     note=Notes.objects.get(id=pk)
#     return render(request,'Notes/note_reminder.html',{'note':note})

from time import gmtime, strftime


def note_reminder(request, pk):
    """
    This function  is used to set reminder

    :param request:request from user
    :param pk: pk of particular note to set reminder
    :return: render and redirect
    """
    note = Notes.objects.get(id=pk)
    if request.method == 'POST':
        print(request.POST, 'Hii i am post wala')
        print(request.body, 'Hii i am body wala')
        print(request.POST.get('date_and_time'), 'Hii i am body wala')
        date = request.POST.get('date_and_time')

        note = Notes.objects.get(id=pk)

        date = str(date)
        # strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

        note.reminder = date
        print(note.reminder, '---->note reminder')
        note.save()
        print(note, '--->', pk)

        return redirect('show_notes')
    return render(request, 'Notes/note_reminder.html', {'note': note})


def copy_note(request, pk):
    """
    This function is used to make copy of existing note

    :param request:request from specific note
    :param pk: pk of particular note to make copy of it
    :return:redirect
    """
    note = Notes.objects.get(id=pk)

    note2 = note
    note2.id = note.id + 1
    note2.save()

    return redirect('show_notes')


def archive(request, pk):
    """
    This function is used to make particular Note archive
    and Un-archive.
    :param request:
    :param pk:
    :return:
    """

    note = Notes.objects.get(id=pk)

    if note.is_archived is True:
        note.is_archived = False
        note.save()
        return redirect('show_archive_notes')
    else:
        note.is_archived = True
        note.save()

    return redirect('show_notes')


def show_archive_notes(request):
    """
    This function is used to display Archive  Notes

    :param request: request
    :return: render html file
    """
    notes_obj = Notes.objects.filter(is_archived=True).order_by('-created_time')
    print(notes_obj)

    return render(request, 'users/dashboard.html', {'notes_obj': notes_obj})


def pin(request, pk):
    """
    This function is used to pin or Unpin particular Note

    :param request:request of particular Note to pin or Unpin
    :param pk: pk of that Note
    :return: redirect
    """
    note = Notes.objects.get(id=pk)

    if note.is_pinned is True:
        note.is_pinned = False
        note.save()

    else:
        note.is_pinned = True
        note.save()

    return redirect('show_notes')


def show_pin_notes(request):
    """
    This function is used to display PINNED note
    :param request: request to display PINNED notes
    :return: render html file
    """
    try:
        response = {}
        response['message'] = 'Somthing wrong happened!'
        response['message'] = False
        response['data'] = {}
        pin_notes = Notes.objects.filter(is_pinned=True).order_by('-created_time')
        print(pin_notes, '-->', 'pin_notes')

        response['data'] = {
            'notes_obj': pin_notes
        }
        return render(request, 'users/dashboard.html', context=response)
    except Notes.DoesNotExist:
        print('Note doesnt exist')
        return render(request, 'users/dashboard.html', context=response)
    except Exception as e:
        return render(request, 'users/dashboard.html', context=response)


from django.db.models import Q


def search(request):
    """
    This function is used to provide search result according to users query.

    :param request: GET request
    :return: it will render results.html file and return it as users query response

    """

    response = {}
    response['success'] = False
    response['message'] = None
    response['data'] = None
    if request.method == 'GET':

        title = request.GET.get('title')

        if title is '':
            response['success'] = True
            response['message'] = 'title is None'
            response['data'] = None
            return render(request, 'Notes/results.html', {'results': response})

        if title is not None:
            user = request.user
            queryset = Notes.objects.filter(user=user)
            print(queryset, 'queryset===========>ye wla hai')
            all_notes = Notes.objects.all()

            note_list = []
            for note_obj in all_notes:

                list_note_users = note_obj.collaborate.all()
                print(list_note_users, '==========>list_note_users')

                for users in list_note_users:

                    if users == request.user:
                        note_list.append(note_obj.id)
                        # notes_obj.append(note_obj)
                        # print(note_list,'note_list=================>')

                collaborator_notes = Notes.objects.filter(pk__in=note_list)
                print(collaborator_notes, '===========>collaborator_notes')

                records = queryset | collaborator_notes  # Here i am taking Union of two Queryset to get objects from both the Queryset

                print(records, '==============>records')

            queryset = records.filter(Q(title__icontains=title) | Q(description__icontains=title))

            response['success'] = True
            response['message'] = 'your query result is as follows'
            response['data'] = queryset

            return render(request, 'Notes/results.html', {'results': response})

    else:

        response['success'] = False
        response[
            'message'] = 'Your request is not Get request.It must be Get request in order to get proper query results'
        response['data'] = []
        return render(request, 'Notes/results.html', {'results': response})


from .forms import colaborator_form
from rest_framework_jwt.settings import api_settings
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)



def note_collaborator(request, note_id):
    response = {}
    response['success'] = False
    response['message'] = None
    response['data'] = None
    try:

        if request.method == 'POST':

            # print(request.POST,'========>request.POST')
            # print(request.META.get('HTTP_TOKEN'),'========>request.META')
            # print(data,'========>data')
            form = colaborator_form(request.POST)

            if 'token' in cache:
                token = cache.get('token')
                print(token, '=======>token=cache.get(token)')

                if token is not request.META.get('HTTP_TOKEN'):
                    cache.set("token", request.META.get('HTTP_TOKEN'))
                    token = request.META.get('HTTP_TOKEN')
                    print(token, '=========>cache.set("token",token,timeout=CACHE_TTL) but IN IF ONLY I AM SETTING')

            else:
                token = request.META.get('HTTP_TOKEN')
                cache.set("token", token, timeout=CACHE_TTL)

                print(token, '=========>cache.set("token",token,timeout=CACHE_TTL)')

            jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
            try:
                decode = jwt_decode_handler(token)
                print(decode, 'decode============>')

                user_id = request.POST.get('collaborate')
                print(user_id, '===============>user_id')

                print(user_id, '===========>user_id')
                note_obj = Notes.objects.get(id=note_id)

                user_obj = User.objects.get(id=user_id)

                note_obj.collaborate.add(user_obj)

                response['message'] = 'Collaborator added successfully'
                response['success'] = True

            except jwt.ExpiredSignature:
                msg = 'Signature has expired'
                raise AuthenticationFailed(msg)
            except jwt.DecodeError:
                msg = 'Error decoding signature.'
                raise AuthenticationFailed(msg)
            except jwt.InvalidTokenError:
                msg = "token is not valid"
                raise AuthenticationFailed(msg)



            return JsonResponse(response)

        else:
            form = colaborator_form()
            return render(request, 'Notes/colaborator.html', {'form': form, 'note_id': note_id})
    except Notes.DoesNotExist:
        response['message'] = 'Unable to find the note details'
        print("Note Not Found")
        return render(request, 'Notes/colaborator.html', {'form': form, 'note_id': note_id})
    except User.DoesNotExist:
        response['message'] = 'Unable to find the user details'
        print("User Not Found")
        return render(request, 'Notes/colaborator.html', {'form': form, 'note_id': note_id})
    except Exception as e:
        response['message'] = 'Something went wrong!'
        print(e)
        return render(request, 'Notes/colaborator.html', {'form': form, 'note_id': note_id})




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
