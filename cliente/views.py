from django.shortcuts import render
from .forms import ClienteForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_cliente import create_cliente, get_cliente

def cliente_list(request):
    measurements = get_cliente()
    context = {
        'measurement_list': measurements
    }
    return render(request, 'Cliente/cliente.html', context)

def cliente_create(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            create_cliente(form)
            messages.add_message(request, messages.SUCCESS, 'cliente create successful')
            return HttpResponseRedirect(reverse('clienteCreate'))
        else:
            print(form.errors)
    else:
        form = ClienteForm()

    context = {
        'form': form,
    }

    return render(request, 'Cliente/clienteCreate.html', context)