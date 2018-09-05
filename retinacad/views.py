from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import FundusRetinaForm
from .models import FundusRetina

# Create your views here.
class FundusRetinaView(FormView):
    template_name = 'retinacad/index.html'
    form_class = FundusRetinaForm
    success_url = '/analysis'
    
    def post(self, request):
        form = FundusRetinaForm(self.request.POST, self.request.FILES)
        if (form.is_valid()):
            fundus = form.save()
            return HttpResponseRedirect(reverse('retinacad:analysis', args=(fundus.pk,)))
        else:
            return HttpResponseRedirect(reverse('retinacad:index'))

class FundusRetinaAnalysis(DetailView):
    model = FundusRetina
    template_name = 'retinacad/analysis.html'


class UploadListView(ListView):
    model = FundusRetina
    paginate_by = 100  # if pagination is desired