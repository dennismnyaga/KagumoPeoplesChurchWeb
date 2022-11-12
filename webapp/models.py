from django.db import models
from embed_video.fields import EmbedVideoField




class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name

class Sermons(models.Model):
    sermon_title = models.CharField( max_length=200)
    Speaker = models.CharField(max_length=20)
    image = models.ImageField()
    static_video = models.FileField(null=True, blank=True)
    video_url = EmbedVideoField()
    tag = models.ManyToManyField(Tag)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Sermons"
    

    def __str__(self):
        return self.sermon_title


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    


class Events(models.Model):
    event_name = models.CharField("Event Name", max_length=200)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    start_time = models.TimeField('Start time', null=True, blank=True)
    end_time = models.TimeField("End at", null=True, blank=True)
    host = models.CharField('Host', max_length=200, null=True, blank=True)
    venue = models.CharField('venue', max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    location_codinates = models.CharField(max_length=500, null=True, blank=True)
    entry_fee = models.CharField(max_length=200, null=True, blank=True)
    event_description = models.TextField( null=True, blank=True)
    requirements = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Events"

    def __str__(self):
        return self.event_name


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url



class Podcast(models.Model):
    title = models.CharField(max_length=2000)
    # audio = models.FileField()
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.title)


    
class Testimonies(models.Model):
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    testimony = models.TextField()
    name = models.CharField(max_length=200)
    image = models.ImageField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Testimonies"


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class ChurchPastors(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    image = models.ImageField()
    facebook = models.CharField(max_length=200, null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)
    twitter = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Ministerial Team"


    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Quotes(models.Model):
    image = models.ImageField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Quotes"

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class ServiceTimeline(models.Model):
    service_name = models.CharField(max_length=200)
    start_time = models.TimeField()
    ends_in = models.TimeField()

    def __str__(self):
        return self.service_name


class VideoClips(models.Model):
    title = models.CharField(max_length=200)
    video_url = EmbedVideoField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Video Clips"

    def __str__(self):
        return self.title

class Ministries(models.Model):
    ministry_name = models.CharField(max_length=200)
    decription = models.TextField()
    latest_yt = EmbedVideoField()
    image = models.ImageField()
    team_leader_name = models.CharField(max_length=200)
    team_leader_message = models.TextField()
    team_leader_image = models.ImageField()
    gallery = models.ImageField()

    class Meta:
        verbose_name_plural = "Ministries"


    def __str__(self):
        return self.ministry_name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    @property
    def team_leader_imageURL(self):
        try:
            url = self.team_leader_image.url
        except:
            url = ''
        return url
    
    @property
    def galleryURL(self):
        try:
            url = self.gallery.url
        except:
            url = ''
        return url





class Department(models.Model):
    department_name = models.CharField(max_length=200)
    decription = models.TextField()
    image = models.ImageField()
    team_leader_name = models.CharField(max_length=200)
    team_leader_message = models.TextField()
    team_leader_image = models.ImageField()
    gallery = models.ImageField()

    class Meta:
        verbose_name_plural = "Department"


    def __str__(self):
        return self.department_name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    @property
    def team_leader_imageURL(self):
        try:
            url = self.team_leader_image.url
        except:
            url = ''
        return url
    
    @property
    def galleryURL(self):
        try:
            url = self.gallery.url
        except:
            url = ''
        return url





class AboutUS(models.Model):
    title = models.CharField(max_length=200)
    decription = models.TextField()
    image1 = models.ImageField(null=True, blank = True)
    image2 = models.ImageField(null=True, blank = True)

    class Meta:
        verbose_name_plural = "About Us"


    def __str__(self):
        return self.title

    @property
    def image1URL(self):
        try:
            url = self.image1.url
        except:
            url = ''
        return url
    @property
    def image2URL(self):
        try:
            url = self.image2.url
        except:
            url = ''
        return url





class Giving(models.Model):
    giving = (
        ('GTN', 'GRACE TO NATION'),
        ('VOICE OF MY SPIRIT', 'VOICE OF MY SPIRIT'),
        ('PRAISE', 'PRAISE'),
        ('CHURCH SERVICE', 'CHURCH SERVICE'),
        ('CHILDREN MINISTRY', 'CHILDREN MINISTRY')
    )

    currency = (
        ('USD', 'USD'),
        ('KES', 'KES'),
        ('EUR', 'EUR'),
        ('GBP', 'GBP'),
        ('CAD', 'CAD')
    )

    firsname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    phoneNumber =  models.IntegerField()
    # giving = models.TextChoices('GTN', 'VOICE OF MY SPIRIT', 'PRAISE', 'CHURCH SERVICE')
    reasons_for_giving = models.CharField( choices=giving, max_length=200)
    # currency = models.TextChoices('USD', 'KES', 'EUR', 'GBP', 'CAD')
    give_in_currency = models.CharField(choices=currency, max_length=20)
    amount = models.IntegerField()


    def __str__(self):
        return self.firsname