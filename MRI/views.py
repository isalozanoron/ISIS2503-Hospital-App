from django.shortcuts import render
from .forms import MRIForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_measurement import create_MRI, get_MRI

def MRI_list(request):
    MRI = get_MRI()
    context = {
        'MRI_list': MRI
    }
    return render(request, 'MRI/MRI.html', context)

def MRI_create(request):
    if request.method == 'POST':
        form = MRIForm(request.POST)
        if form.is_valid():
            create_MRI(form)
            messages.add_message(request, messages.SUCCESS, 'MRI create successful')
            return HttpResponseRedirect(reverse('MRICreate'))
        else:
            print(form.errors)
    else:
        form = MRIForm()

    context = {
        'form': form,
    }

    return render(request, 'MRI/MRICreate.html', context)