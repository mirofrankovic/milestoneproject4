from django.shortcuts import render, HttpResponse

# Create your views here.


def get_project4_list(request):
    return render(request, "project4_list.html")
