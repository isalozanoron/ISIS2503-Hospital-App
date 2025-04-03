from django.shortcuts import render
from .forms import MRIForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_MRI import create_mri, get_mris 

def MRI_list(request):
    mris = get_mris()  
    context = {
        'MRI_list': mris
    }
    return render(request, 'MRI/MRI.html', context)

def MRI_create(request):
    if request.method == 'POST':
        form = MRIForm(request.POST)
        if form.is_valid():
            create_mri(form)
            messages.add_message(request, messages.SUCCESS, 'MRI creado exitosamente')
            return HttpResponseRedirect(reverse('MRICreate'))
        else:
            print(form.errors)
    else:
        form = MRIForm()

    context = {
        'form': form,
    }

    return render(request, 'MRI/MRICreate.html', context)
