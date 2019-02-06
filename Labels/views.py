from django.shortcuts import render, redirect
from django.views.generic import UpdateView

from .models import Labels
    # MapLabels
from django.http import HttpResponse
# Create your views here.
from .forms import CreateLabels,UpdateLabels

def create_label(request):

    # obj=Labels.objects.get(label='1st')
    # print(obj.label,obj.user,obj.id ,obj.created_time)
    #
    # obj2=MapLabels.objects.get(label_id=obj)
    # print(obj2.note_id,' ----object2 ----')
    # print(obj2.note_id.color,' ----object2 ----')

    if request.method=='POST':

        label=request.POST.get('label')
        form=CreateLabels(request.POST)
        print(label, ' label ')
        if form.is_valid():
            form1=form.save(commit=True)
            # form1.label=label_name
            # form1.save(commit=True)
            # print(form1,' ---form1')
            return HttpResponse(form1)

    else:

        form=CreateLabels()
    return render(request,'Labels/Create_Labels.html',{'form':form})

def update_label(request,pk):

    label=Labels.objects.get(id=pk)
    print(label)
    # form=UpdateLabels(request.POST)
    # print(form)
    if request.method=='POST':
        label_name=request.POST.get('label')
        label.label=label_name
        label.save()
        return HttpResponse('hi')
    return render(request,'Labels/update_label.html')

from Notes.models import Notes
import json

def note_lable(request, pk):
    note = Notes.objects.get(id=pk)
    label_obj=Labels.objects.filter(note_id=note)
    print(label_obj,'label_obj------------>')
    print(note,' --------->note')

    # return render(request, 'Labels/note_lable.html', {'note': note,'label_obj':label_obj})
    return render(request, 'Labels/Create_Labels.html', {'note': note,'label_obj':label_obj})

def delete_label(request,pk):

    print(pk,' ==>id')
    obj=Labels.objects.get(id=pk)
    print(obj,'  ---->obj')
    obj.note_id=None
    obj.save()
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

def note_lable_note(request,pk):

    # label=Labels.objects.get(id=pk)
    # print(label)
    # form=UpdateLabels(request.POST)
    # print(form)
    if request.method=='POST':

        obj = Notes.objects.get(id=pk)
        print(obj,'----->obj')
        # obj.label = request.POST.get('label')
        # obj.save()
        # user=request.user # it will give me logged in user
        # print(user,' --->User')
        # return HttpResponse('hi')

        my_label = request.POST.get('label')
        # form = CreateLabels(request.POST)
        # print(my_label, ' label --->')
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
        form = CreateLabels(request.POST)
        print(my_label, ' label==> ')
        if form.is_valid():
            form1 = form.save(commit=False)
            print(form1,'   ===>form1')
            form1.label=my_label
            print(form1,'form1--===>')
            form1.user=request.user
            form1.note_id=obj
            form1.save()

    return redirect('show_notes')



