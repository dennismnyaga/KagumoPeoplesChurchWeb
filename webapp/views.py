from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
from django_pandas.io import read_frame
from .forms import *
from .models import *

# from .forms import NameForm
# from .forms import GiveForm
# from django.contrib.auth.decorators import login_required





def home(request):
    
    # myFilter = OrderFilter(request.GET, queryset=orders)
    form = SubscriberForm()

    

    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            if Subcribers.objects.filter(email=instance.email).exists():
                messages.warning(request, 'Email Already Exists!')
            else:
                instance.save()
                messages.success(request, 'Successfuly Subscribed')
                return redirect('/')
    else:
        form = SubscriberForm()
    sermon = Sermons.objects.order_by('-date_added')
    events = Events.objects.order_by('-date_added')
    ministries = Ministries.objects.all()
    
    quote = Quotes.objects.order_by('-date_added')
    context = {'sermon':sermon, 'events':events, 'ministries': ministries, 'quote':quote, 'form':form, 'forms':forms}
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



def give(request):
    ministries = Ministries.objects.all()
   
    return render(request, 'webapp/giving.html', {'ministries': ministries})

    # # podcast = Podcast.objects.order_by('-date_added')
    # # context = {'podcast': podcast}
    # giving_info = Giving.objects.all()
    # context = {'giving_info': giving_info}
    # return render(request, 'webapp/giving.html', context)





def lay(request):
    emails = Subcribers.objects.all()
    df = read_frame(emails, fieldnames=['email'])
    mail_list = df['email'].values.tolist()
    print(mail_list)
    ministries = Ministries.objects.all()
    form = MailMessageForm()
    if request.method == 'POST':
        form = MailMessageForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            message = form.cleaned_data.get('content')
            send_mail(
                title,
                message,
                '',
                mail_list,
                fail_silently=False,
            )
            messages.success(request, 'Message has been sent to mail list!')
            return redirect('webapp:lay')
    else:
        form = MailMessageForm()
    context = {'ministries':ministries, 'form':form}
    return render(request, 'webapp/ema.html', context)


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