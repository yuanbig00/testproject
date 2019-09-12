from django.views import generic
from django.shortcuts import get_list_or_404,get_object_or_404
from .models import HotEvents
from django.shortcuts import render_to_response,render
class IndexView(generic.ListView):
    model = HotEvents
    template_name = 'index.html'
    context_object_name = 'index'
def event(request,ids):
    event_list= HotEvents.objects.get(id=ids)
    return render(request,'event.html',{'event_list':event_list})



