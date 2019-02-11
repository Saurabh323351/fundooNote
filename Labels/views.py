
from django.shortcuts import render, redirect
from django.views.generic import UpdateView

from .models import Labels, MapLabels
# MapLabels
from django.http import HttpResponse
# Create your views here.
from .forms import CreateLabels, UpdateLabels


def create_label(request):
    # obj=Labels.objects.get(label='1st')
    # print(obj.label,obj.user,obj.id ,obj.created_time)
    #
    # obj2=MapLabels.objects.get(label_id=obj)
    # print(obj2.note_id,' ----object2 ----')
    # print(obj2.note_id.color,' ----object2 ----')

    if request.method == 'POST':

        label = request.POST.get('label')
        label1 = request.POST.get('name')
        # form = CreateLabels(request.POST)
        print(label, ' label ====================>label')
        print(label1, ' label1 ====================>label1')
        user=request.user
        is_exists=Labels.objects.filter(label=label).exists()
        if is_exists is not True:
            Labels.objects.create(label=label,user=user)

    return redirect('show_notes')

    # else:
    #     return render(request, 'Labels/note_lable.html')


def update_label(request, pk):
    label = Labels.objects.get(id=pk)
    print(label)
    # form=UpdateLabels(request.POST)
    # print(form)
    if request.method == 'POST':
        label_name = request.POST.get('label')
        label.label = label_name
        label.save()
        return HttpResponse('hi')
    return render(request, 'Labels/update_label.html')


from Notes.models import Notes
import json


def note_lable(request, pk):
    note = Notes.objects.get(id=pk)
    # label_obj = Labels.objects.filter(note_id=note)
    # print(label_obj, 'label_obj------------>')
    print(note, ' --------->note')

    # return render(request, 'Labels/note_lable.html', {'note': note,'label_obj':label_obj})
    return render(request, 'Labels/Create_Labels.html', {'note': note})


def delete_label(request, pk):
    print(pk, ' ==>id')
    # notes_obj=Notes.objects.get(id=pk)

    # print(notes_obj,'==============>notes_obj')
    obj = MapLabels.objects.get(id=pk)

    print(obj, '==============>obj')
    print(obj, '  ---->obj')
    obj.delete()

    return redirect('show_notes')



# model = Notes
# fields = ['label']
# template_name = 'note_lable.html'

# class note_lable_note(UpdateView):
#     def post(self, request, *args, **kwargs):
#         response_data = {}
#         response_data['status'] = False
#         if kwargs.get('pk', None):
#             try:
#                 pk = kwargs.get('pk', None)
#                 print(pk,'--------------->')
#                 obj = Notes.objects.get(pk=pk)
#                 obj.label = request.POST.get('label')
#                 obj.save()
#                 response_data['status'] = True
#                 response_data['message'] = "Labeled Successfully"
#             except Exception.DoesNotExist as e:
#                 response_data['message'] = "Note doesnt exists"
#             except Exception as e:
#                 response_data['message'] = 'something went wrong'
#         else:
#             response_data['message'] = "Missing note identifier (id)"
#         return HttpResponse(json.dumps(response_data), content_type='application/json')
#

def note_lable_note(request, pk):
    # label=Labels.objects.get(id=pk)
    # print(label)
    # form=UpdateLabels(request.POST)
    # print(form)
    if request.method == 'POST':
        obj = Notes.objects.get(id=pk)
        print(obj, '----->obj')
        # obj.label = request.POST.get('label')
        # obj.save()
        # user=request.user # it will give me logged in user
        # print(user,' --->User')
        # return HttpResponse('hi')

        my_label = request.POST.get('label')
        # form = CreateLabels(request.POST)
        print(my_label, ' label --->')
        # L=Labels.objects.create(label=my_label)
        # print(L, '  L ---->')
        # # label_obj=Labels.objects.filter(label=my_label)
        # # print(label_obj,'----------->label_obj')
        # # label_obj.user=request.user
        # # label_obj.note_id=obj
        #
        # L.user=request.user
        # L.note_id=obj
        # # L.save()
        # label_obj.save()
        # if form.is_valid():
        #     form1 = form.save()
        #     print(form)

        # queryset_2 = MapLabels.objects.filter(
        #     label_id__startswith='R'
        # ) & MapLabels.objects.filter(
        #     note_id__startswith='D'
        # )
        if Labels.objects.filter(label=my_label).exists():
            L1 = Labels.objects.get(label=my_label)
            L2 = MapLabels.objects.filter(label_id=L1, note_id=obj).exists()
            if L2 is not True:
                MapLabels.objects.create(label_id=L1, note_id=obj)

        else:
            # Labels.objects.cre(label=my_label)
            form = CreateLabels(request.POST)
            if form.is_valid():

                form1=form.save(commit=False)
                form1.label=my_label
                form1.user=request.user
                form1.save()

            L2 = MapLabels.objects.filter(label_id=form1, note_id=obj).exists()
            if L2 is not True:
                MapLabels.objects.create(label_id=form1, note_id=obj)

        # L2 = MapLabels.objects.filter(label_id=L1,note_id=obj).exists()
        # print(L2,'=======>L2')
        #
        #
        # L1 = Labels.objects.filter(label=my_label).exists()
        # print(L1,'              ---------->L1')
        #
        # L2=MapLabels.objects.filter(label_id=L1)
        #
        #
        # print(L1, '===========>L1')
        # # except Labels.DoesNotExist:
        #
        #
        #
        # form = CreateLabels(request.POST)
        # print(my_label, ' label==> ')
        # if form.is_valid():
        #     form1 = form.save(commit=False)
        #     print(form1, '   ===>form1')
        #     form1.label = my_label
        #     print(form1, 'form1--===>')
        #     form1.user = request.user
        #     # form1.note_id=obj
        #     form1.save()
        #
        #
        #



    return redirect('show_notes')

# from django_ajax.decorators import ajax

def get_labels(request):
    labels = Labels.objects.all()
    return render(request, 'users/base.html', {'labels': labels})

from django.http import JsonResponse
from django.core import serializers

def get_labels1(request):
    if request.method=='POST':
        labels1 = Labels.objects.all()
        print(labels1,'===========>labels1')
        label1 = request.POST.get('name')
        print(label1, ' label1 ====================>label1====>')
        # context = {'labels1': labels1}
        # list1=[]
        # for i in range(len(labels1)):
        #     list1.append()
        # users_list = list({'La':labels1})  # important: convert the QuerySet to a list object
        response_data = {}

        response_data['message'] = serializers.serialize('json', labels1,fields=('label'))
        # print(serializers.serialize('json', labels1,fields=('label')),'==========>message')
        # print(serializers.serialize('json', labels1,fields=('label')),'yaha ckeck ker raha hu')
        # print(users_list,'0--------------->')
        # print(response_data['message'][1]['pk'])
        # response_data['message']=labels1
        # return JsonResponse(response_data, safe=False)
        context={'labels1':labels1}

        return HttpResponse({'labels1':labels1})
    else:
        return HttpResponse('hi')
    # return render(request,'users/base.html',context=context)
    # return render(request, 'users/base.html', context={'labels1': labels1})
    # return HttpResponse(json.simplejson.dumps(context), mimetype="application/json")

def get_label_notes(request, id):
    label = Labels.objects.get(id=id)
    # n_id = label.note_id

    try:
        L = MapLabels.objects.filter(label_id=label)
    except:
        return render(request, 'users/base.html', context=[])

    note_list = []

    for i in range(len(L)):
        obj = L[i]
        note_obj = Notes.objects.get(title=obj)
        print('-------------')
        print(note_obj, '-->note_obj')
        note_list.append(note_obj)
        print('-----------')

    print(label, '=========>label')
    print(L, '=========> L ===>')
    print(note_list, '=========> note_list ===>')
    # print(note_obj, '=========> note_obj ===>')
    context = {'notes_obj': note_list,
               }
    return render(request, 'users/base.html', context=context)

