from django.contrib import admin
from .models import Brand, Person,Project,Feature,Rating,Request

admin.site.register(Brand)
admin.site.register(Project)
admin.site.register(Feature)
admin.site.register(Rating)
admin.site.register(Request)
admin.site.register(Person)