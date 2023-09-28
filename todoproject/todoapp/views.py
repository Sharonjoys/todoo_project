from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import newmodelform
from .models import task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
# Create your views here.

class tasklistview(ListView):
    model=task
    template_name = 'home.html'
    context_object_name = 'det'
class taskdetailview(DetailView):
    model = task
    template_name = 'detail.html'
    context_object_name = 'task'


class taskupdateview(UpdateView):
    model = task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})


class taskdeleteview(DeleteView):
    model = task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')



def firsts(request):
    qaz = task.objects.all()
    if request.method=='POST':
        n=request.POST.get('task','')
        s=request.POST.get('priority','')
        nsg=request.POST.get('date','')
        ns=task(name=n,priority=s,date=nsg)
        ns.save()

    return render(request,'home.html',{'det':qaz})

# def detail(request):
#      qaz=task.objects.all()
#      return render(request,'detail.html',{'det':qaz})

def delete(request,mid):
    if request.method=='POST':
        aspire=task.objects.get(id=mid)
        aspire.delete()
        return redirect('/')
    return render(request,'delete.html')


def update(request,id):
    new=task.objects.get(id=id)
    form=newmodelform(request.POST or None,instance=new)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form})