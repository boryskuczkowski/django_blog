
from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Post


class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('content',)


admin.site.register(Post, SomeModelAdmin)
