from django.shortcuts import render, HttpResponse
from django.views.generic import View
from py_math.models import OperationHistory
import time

class FunView(View):

    def get(self, request):
        context = {
            "page_title": "Fun",
            "render_ts": time.time()
        }
        return render(request, "py_math/fun.html", context)
    
    def post(self, request):
        a = int(request.POST["a"])
        b = int(request.POST["b"])
        result = a ** b
        oh = OperationHistory(base=a, exponent=b)
        oh.save()
        context = {
            "page_title": "Fun",
            "render_ts": time.time(),
            "result": result,
            "oh": oh
            }
        return render(request, "py_math/fun.html", context)
    

class AllHistory(View):

    def get(self, request):
        qs = OperationHistory.objects.filter(base=2)
        context = {
            "objects": qs
        }
        return render(request, "py_math/history.html", context)
    