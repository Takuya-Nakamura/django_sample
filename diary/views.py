
# https://blog.daisukekonishi.com/post/django-json-response-by-class-based-view/
# from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse
from django.views import View
import json

# Create your views here.
class IndexView(generic.TemplateView):
    template_name="index.html"


# original class base
class ApiView(View):
   def get(self, request, *args, **kwargs): 
         return JsonResponse({"test":"test"})


# function base
def api_test(request):
        return JsonResponse({"test":"function based object"})
