from django.core.paginator import Paginator
from django.shortcuts import render

from .models import *

# from .forms import NameForm
from .forms import GiveForm
from django.contrib.auth.decorators import login_required




def get_name(request):
    if response.method == 'POST':
        form = GiveForm(response.POST)
        if form.is_valid():
            author = form.save()
            # Do something with the author (model instance)
            return render(response, 'webapp/home.html', {'message': 'Successful'})
        else:
            return render(response, 'webapp/giving.html', {'form': form})

    else:
        form = AuthorForm()
        return render(response, 'webapp/giving.html', {'form': form})




def home(request):
    sermon = Sermons.objects.order_by('-date_added')
    events = Events.objects.order_by('-date_added')
    ministries = Ministries.objects.all()
    departments = Department.objects.all()
    quote = Quotes.objects.order_by('-date_added')
    context = {'sermon':sermon, 'events':events, 'ministries': ministries, 'quote':quote, 'departments': departments}
    return render(request, 'webapp/home.html', context)



def ministry(request):
    ministries = Ministries.objects.all()
    paginator = Paginator(ministries, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj':page_obj}
    return render(request, 'webapp/ministries.html', context)

def event(request, event_id):
    events = Events.objects.get(id=event_id)
    context = {'events': events}
    return render(request, 'webapp/event.html', context)



def sermon(request, sermon_id):
    more = Sermons.objects.order_by('-date_added')
    sermons = Sermons.objects.get(id=sermon_id)
    context = {'sermons': sermons, 'more': more}
    return render(request, 'webapp/sermons.html', context)


def ministries(request, ministry_id):
    ministry = Ministries.objects.get(id=ministry_id)
    context = {'ministry': ministry}
    return render(request, 'webapp/ministry.html', context)


def departments(request, department_id):
    department = Department.objects.get(id=department_id)
    context = {'department': department}
    return render(request, 'webapp/department.html', context)


def sermons(request):
    sermons = Sermons.objects.order_by('-date_added')
    more_paginator = Paginator(sermons, 6)
    page_number = request.GET.get('page')
    sermons_obj = more_paginator.get_page(page_number)
    dist = Sermons.objects.order_by('-date_added')
    context = {'sermons_obj':sermons_obj, 'dist':dist}
    return render(request, 'webapp/sermon.html', context)

def spirit(request):
    spir = Sermons.objects.filter(tag__name="Spirit Life")
    spir_paginator = Paginator(spir, 6)
    page_number = request.GET.get('page')
    spir_obj = spir_paginator.get_page(page_number)
    context = {'spir_obj':spir_obj}
    return render(request, 'webapp/spiritlife.html', context)


def sunday(request):
    sun = Sermons.objects.filter(tag__name="Sunday celebration")
    paginator = Paginator(sun, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj':page_obj}
    return render(request, 'webapp/sunday.html', context)


def prophetic(request):
    prophet = Sermons.objects.filter(tag__name="Prophetic Voice")
    paginator = Paginator(prophet, 6)
    prophetic_number = request.GET.get('page')
    prophetic_obj = paginator.get_page(prophetic_number)
    context = {'prophetic_obj':prophetic_obj}
    return render(request, 'webapp/prophet.html', context)

def month(request):
    prayer = Sermons.objects.filter(tag__name="Monthly Prayer Festivals")
    paginator = Paginator(prayer, 6)
    prayer_number = request.GET.get('page')
    prayer_obj = paginator.get_page(prayer_number)
    context = {'prayer_obj':prayer_obj}
    return render(request, 'webapp/prayer.html', context)

def grace(request):
    balm = Sermons.objects.filter(tag__name="Grace Balm")
    paginator = Paginator(balm, 6)
    balm_number = request.GET.get('page')
    balm_obj = paginator.get_page(balm_number)
    context = {'balm_obj':balm_obj}
    return render(request, 'webapp/gracebalm.html', context)

def praise(request):
    pra = Sermons.objects.filter(tag__name="Praise Hour")
    paginator = Paginator(pra, 6)
    pra_number = request.GET.get('page')
    pra_obj = paginator.get_page(pra_number)
    context = {'pra_obj':pra_obj}
    return render(request, 'webapp/praise.html', context)


def voice(request):
    voi = Sermons.objects.filter(tag__name="Voice of my spirit")
    paginator = Paginator(voi, 6)
    voi_number = request.GET.get('page')
    voi_obj = paginator.get_page(voi_number)
    context = {'voi_obj':voi_obj}
    return render(request, 'webapp/voice.html', context)

@login_required
def aboutus(request):
    about = AboutUS.objects.all()
    pastors = ChurchPastors.objects.all()
    context = {'about':about, 'pastors':pastors}
    return render(request, 'webapp/about.html', context)


def quotes(request):
    quote = Quotes.objects.order_by('-date_added')
    paginator = Paginator(quote, 12)
    quote_number = request.GET.get('page')
    quote_obj = paginator.get_page(quote_number)
    context = {'quote_obj': quote_obj}
    return render(request, 'webapp/quotes.html', context)


@login_required
def podcast(request):
    podcast = Podcast.objects.order_by('-date_added')
    context = {'podcast': podcast}
    return render(request, 'webapp/podcast.html', context)



def give(request, response):
    if response.method == 'POST':
        form = GiveForm(response.POST)
        if form.is_valid():
            author = form.save()
            # Do something with the author (model instance)
            return render(response, 'webapp/home.html', {'message': 'Successful'})
        else:
            return render(response, 'webapp/giving.html', {'form': form})

    else:
        form = AuthorForm()
        return render(response, 'webapp/giving.html', {'form': form})

    # # podcast = Podcast.objects.order_by('-date_added')
    # # context = {'podcast': podcast}
    # giving_info = Giving.objects.all()
    # context = {'giving_info': giving_info}
    # return render(request, 'webapp/giving.html', context)





def lay(request):
    context = {}
    return render(request, 'webapp/layout.html', context)