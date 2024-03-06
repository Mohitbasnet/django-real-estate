from django.contrib import admin

# Register your models here.
from . models import Rating

class RatingAdmin(admin.ModelAdmin):
    list_display = ["rating", "agent", "rater"]

admin.site.register(Rating,RatingAdmin)