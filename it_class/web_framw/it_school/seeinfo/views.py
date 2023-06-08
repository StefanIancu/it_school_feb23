from django.views.generic import TemplateView
from seeinfo.models import SeeInfo
# Create your views here.

class AccesInfo(TemplateView):

    template_name = "seeinfo/info.html"
    model = SeeInfo
