from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from main_gusto.models import UsersMessages
from django.core.paginator import Paginator

def messege_processed(request,pk):
    try:
        messege = UsersMessages.objects.get(id=pk)
        messege.is_processed=True
        messege.save()
        return HttpResponseRedirect("/user_messeges/view")
    except UsersMessages.DoesNotExist:
        return HttpResponseNotFound("<h2>Messege not found</h2>")

def messeges_view(request):
    messeges = UsersMessages.objects.filter(is_processed=False).order_by('-send_date')
    paginator = Paginator(messeges,5)
    page= request.GET.get('page')
    messeges_page = paginator.get_page(page)
    return render(request,'messeges_view.html',context={'items':messeges_page})
