from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.conf import settings

from .forms import FundusRetinaForm
from .models import FundusRetina

from diabeticretinopathy.code.dr_cam_viz import find_pred_one

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
    
    def get_context_data(self, **kwargs):
        context = super(FundusRetinaAnalysis, self).get_context_data(**kwargs)
        left_cam, left_prob = find_pred_one(settings.MEDIA_ROOT, context['object'].lefteye.name)
        right_cam, right_prob = find_pred_one(settings.MEDIA_ROOT, context['object'].righteye.name)
        context['object'].left_cam = settings.MEDIA_URL + left_cam
        context['object'].left_prob = left_prob
        context['object'].right_cam = settings.MEDIA_URL + right_cam
        context['object'].right_prob = right_prob
        #import pdb; pdb.set_trace()
        return context


class UploadListView(ListView):
    model = FundusRetina
    paginate_by = 100  # if pagination is desired