from django.contrib import admin

# Register your models here.
from blog.models import Posting,likes
admin.site.register(Posting)
admin.site.register(likes)
