from pydoc_data.topics import topics
from django.shortcuts import render, redirect
from django.views import View
from .models import Topic

class IndexView(View):

    def get(self, request, *args, **kwargs):
        
        topics  = Topic.objects.all()
        context = { "topics":topics }

        return render(request,"hikitugi/index.html")
    
    def post(self, request, *args, **kwargs):

        posted  = Topic( comment = request.POST["comment"] )
        posted.save()

        return redirect("hikitugi:index")

index   = IndexView.as_view()