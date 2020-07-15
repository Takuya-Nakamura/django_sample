from django.views import generic
from django.http import JsonResponse
from django.views import View
from .lib.util import echo, MyClass  # original path


class IndexView(generic.TemplateView):
    """
    Create your views here.
    """

    template_name = "index.html"


class ClassApiView(View):
    """
     original class base
    """

    def get(self, request, *args, **kwargs):
        message = echo()
        mc = MyClass()
        res = mc.getProperty()
        print(res)
        mc.setParam()
        res = mc.getProperty()
        print(res)
        return JsonResponse({"name": message})


def function_api(request):
    """
    function base
    """
    return JsonResponse({"name": "function base view"})
