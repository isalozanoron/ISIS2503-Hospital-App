from ..models import Measurement

def get_measurements():
    queryset = Measurement.objects.a().order_by('-dateTime')[:10]
    return (queryset)

def create_measurement(form):
    measurement = form.save()
    measurement.save()
    return ()