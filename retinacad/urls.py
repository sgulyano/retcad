from django.urls import path

from . import views

app_name = 'retinacad'
urlpatterns = [
    path('', views.FundusRetinaView.as_view(), name='index'),
    path('fundus_list', views.UploadListView.as_view(), name='fundus-list'),
    path('<int:pk>/analysis', views.FundusRetinaAnalysis.as_view(), name='analysis'),
]