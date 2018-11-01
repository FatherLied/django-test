from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # pdb.set_trace()   # BreakPoint
    return HttpResponse("Hello, world. You're at the polls index.")