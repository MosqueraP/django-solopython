from django.views.generic import View
from django.shortcuts import render

# para POST y GET
class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'index.html',context)

