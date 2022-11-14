from django.urls import path
from . import views



app_name = 'webapp'
urlpatterns = [
   
    path('', views.home, name='home'),
    # path('', views.nav_ministries),
    path('event/<int:event_id>/', views.event, name='event'),
    path('sermon/<int:sermon_id>/', views.sermon, name='sermon'),
    path('sermons', views.sermons, name='sermons'),
    path('spiritlife', views.spirit, name='spirit'),
    path('sundaycelebration', views.sunday, name='sunday'),
    path('propheticvoice', views.prophetic, name='prophet'),
    path('monthlyPrayerFestival', views.month, name='month'),
    path('graceBalm', views.grace, name='grace'),
    path('praiseHour', views.praise, name='praise'),
    path('VoiceofMySpirit', views.voice, name='voice'),
    path('ministry/<int:ministry_id>', views.ministries, name='ministries'),
   
    path('about us', views.aboutus, name='about'),
    path('quotes', views.quotes, name='quote'),
    path('podcast/', views.podcast, name='podcast'),
    path('give/', views.give, name='give'),
    path('ministry/', views.ministry, name='ministry'),
    path('statementoffaith/', views.statement_of_faith, name='statement'),
    path('wordconfession/', views.word_of_confession, name='confession'),
    path('churchleaders/', views.leaders, name='leadership'),

    # ====================
    path('lay/', views.lay, name='lay'),

]
