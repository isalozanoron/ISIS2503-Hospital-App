from MRI.models import MRI

def get_MRI():
    queryset = MRI.objects.all().order_by('-dateTime')[:10]
    return (queryset)

def create_MRI(form):
    measurement = form.save()
    measurement.save()
    return ()