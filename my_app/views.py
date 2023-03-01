from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import ServerImages
from .forms import ServerForm

# Create your views here.

def index_view(request):
    if request.method == 'POST':
        form = ServerForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = ServerForm()

    return render(request, 'index.html', {'form': form})