from django.contrib import admin
from .models import *
from shopping.models import *


admin.site.register(Sermons)
admin.site.register(Tag)
admin.site.register(Events)
admin.site.register(Podcast)
admin.site.register(ChurchPastors)
admin.site.register(Quotes)
admin.site.register(ServiceTimeline)
admin.site.register(Ministries)
admin.site.register(Giving)
admin.site.register(MailMessage)
admin.site.register(Subcribers)





# admin.site.register(Customer)
# admin.site.register(Product)
# admin.site.register(Order)
# admin.site.register(OrderItem)
# admin.site.register(ShippingAddress)
