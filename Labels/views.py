from django.shortcuts import render
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
