from django.shortcuts import render
from django.http import HttpResponse
from .models import Technology
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def technologies(request):
    tech = Technology.objects.all()

    paginator = Paginator(tech, 10)
    page = request.GET.get('page')
    paged_tech = paginator.get_page(page)

    context = {
        'tech': paged_tech
    }

    return render(request, 'technologies/technologies.html', context)

def search(request):
    queryset_list = Technology.objects.all()

    if 'stack' in request.GET:
        stack = request.GET['stack']
        if stack:
            queryset_list = queryset_list.filter(softwaretype__iexact=stack)

    if 'software' in request.GET:
        software = request.GET['software']
        if software:
            queryset_list = queryset_list.filter(software__icontains=software)

    context = {
        'tech': queryset_list
    }

    return render(request, 'technologies/search.html', context)