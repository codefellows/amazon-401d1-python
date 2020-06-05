from django.views.generic import ListView

from .models import Snack

class SnacksListView(ListView):
    model = Snack
    template_name="snacks/snacks_list.html"
