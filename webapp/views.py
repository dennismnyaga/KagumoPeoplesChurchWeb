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

# def nav_ministries(request):
#     ministry = Ministries.objects.all()
#     context = {'ministry': ministry}
#     return render(request, 'webapp/layout.html', context)



def home(request):
    sermon = Sermons.objects.order_by('-date_added')
    events = Events.objects.order_by('-date_added')
    ministries = Ministries.objects.all()
    
    quote = Quotes.objects.order_by('-date_added')
    context = {'sermon':sermon, 'events':events, 'ministries': ministries, 'quote':quote}
    return render(request, 'webapp/home.html', context)



def ministry(request):
    ministries = Ministries.objects.all()
    paginator = Paginator(ministries, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj':page_obj}
    return render(request, 'webapp/ministries.html', context)

def event(request, event_id):
    ministries = Ministries.objects.all()
    events = Events.objects.get(id=event_id)
    context = {'events': events, "ministries":ministries}
    return render(request, 'webapp/event.html', context)



def sermon(request, sermon_id):
    ministries = Ministries.objects.all()
    more = Sermons.objects.order_by('-date_added')
    sermons = Sermons.objects.get(id=sermon_id)
    context = {'sermons': sermons, 'more': more, 'ministries':ministries}
    return render(request, 'webapp/sermons.html', context)


def ministries(request, ministry_id):
    ministries = Ministries.objects.all()
    ministry = Ministries.objects.get(id=ministry_id)
    context = {'ministry': ministry, 'ministries':ministries}
    return render(request, 'webapp/ministry.html', context)






def sermons(request):
    ministries = Ministries.objects.all()
    sermons = Sermons.objects.order_by('-date_added')
    more_paginator = Paginator(sermons, 6)
    page_number = request.GET.get('page')
    sermons_obj = more_paginator.get_page(page_number)
    dist = Sermons.objects.order_by('-date_added')
    context = {'sermons_obj':sermons_obj, 'dist':dist, 'ministries':ministries}
    return render(request, 'webapp/sermon.html', context)

def spirit(request):
    ministries = Ministries.objects.all()
    spir = Sermons.objects.filter(tag__name="Spirit Life")
    spir_paginator = Paginator(spir, 6)
    page_number = request.GET.get('page')
    spir_obj = spir_paginator.get_page(page_number)
    context = {'spir_obj':spir_obj, 'ministries':ministries}
    return render(request, 'webapp/spiritlife.html', context)


def sunday(request):
    ministries = Ministries.objects.all()
    sun = Sermons.objects.filter(tag__name="Sunday celebration")
    paginator = Paginator(sun, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj':page_obj, 'ministries':ministries}
    return render(request, 'webapp/sunday.html', context)


def prophetic(request):
    ministries = Ministries.objects.all()
    prophet = Sermons.objects.filter(tag__name="Prophetic Voice")
    paginator = Paginator(prophet, 6)
    prophetic_number = request.GET.get('page')
    prophetic_obj = paginator.get_page(prophetic_number)
    context = {'prophetic_obj':prophetic_obj, 'ministries':ministries}
    return render(request, 'webapp/prophet.html', context)

def month(request):
    ministries = Ministries.objects.all()
    prayer = Sermons.objects.filter(tag__name="Monthly Prayer Festivals")
    paginator = Paginator(prayer, 6)
    prayer_number = request.GET.get('page')
    prayer_obj = paginator.get_page(prayer_number)
    context = {'prayer_obj':prayer_obj, 'ministries':ministries}
    return render(request, 'webapp/prayer.html', context)

def grace(request):
    ministries = Ministries.objects.all()
    balm = Sermons.objects.filter(tag__name="Grace Balm")
    paginator = Paginator(balm, 6)
    balm_number = request.GET.get('page')
    balm_obj = paginator.get_page(balm_number)
    context = {'balm_obj':balm_obj, 'ministries':ministries}
    return render(request, 'webapp/gracebalm.html', context)

def praise(request):
    ministries = Ministries.objects.all()
    pra = Sermons.objects.filter(tag__name="Praise Hour")
    paginator = Paginator(pra, 6)
    pra_number = request.GET.get('page')
    pra_obj = paginator.get_page(pra_number)
    context = {'pra_obj':pra_obj, 'ministries':ministries}
    return render(request, 'webapp/praise.html', context)


def voice(request):
    ministries = Ministries.objects.all()
    voi = Sermons.objects.filter(tag__name="Voice of my spirit")
    paginator = Paginator(voi, 6)
    voi_number = request.GET.get('page')
    voi_obj = paginator.get_page(voi_number)
    context = {'voi_obj':voi_obj, 'ministries':ministries}
    return render(request, 'webapp/voice.html', context)

def aboutus(request):
    ministries = Ministries.objects.all()
    pastors = ChurchPastors.objects.all()
    context = {'ministries':ministries}
    return render(request, 'webapp/about.html', context)


def quotes(request):
    ministries = Ministries.objects.all()
    quote = Quotes.objects.order_by('-date_added')
    paginator = Paginator(quote, 12)
    quote_number = request.GET.get('page')
    quote_obj = paginator.get_page(quote_number)
    context = {'quote_obj': quote_obj, 'ministries':ministries}
    return render(request, 'webapp/quotes.html', context)


def podcast(request):
    ministries = Ministries.objects.all()
    podcast = Podcast.objects.order_by('-date_added')
    context = {'podcast': podcast, 'ministries':ministries}
    return render(request, 'webapp/podcast.html', context)



def give(request, response):
    ministries = Ministries.objects.all()
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
    ministries = Ministries.objects.all()
    context = {'ministries':ministries}
    return render(request, 'webapp/layout.html', context)


def statement_of_faith(request):
    ministries = Ministries.objects.all()
    context = {'ministries':ministries}
    return render(request, 'webapp/faith.html', context)



def word_of_confession(request):
    ministries = Ministries.objects.all()
    context = {'ministries':ministries}
    return render(request, 'webapp/confession.html', context)


def leaders(request):
    ministries = Ministries.objects.all()
    context = {'ministries':ministries}
    return render(request, 'webapp/leaders.html', context)