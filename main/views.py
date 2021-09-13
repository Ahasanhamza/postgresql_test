from django.views.generic import ListView
from .models import Pigeons
from .models import Pigeons_Info
from .models import Pigeons_Status

class Homeview(ListView):
    template_name = "home.html"
    model = Pigeons_Info

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.select_related('pigeons_name')
