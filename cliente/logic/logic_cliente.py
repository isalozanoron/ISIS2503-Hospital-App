from ..models import Cliente

def get_cliente():
    queryset = Cliente.objects.all().order_by('-dateTime')[:10]
    return (queryset)

def create_cliente(form):
    measurement = form.save()
    measurement.save()
    return ()