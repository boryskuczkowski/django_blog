from django.forms import ModelForm
from django_summernote.widgets import SummernoteInplaceWidget
from .models import Post


class PostFormModel(ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'category', 'title', 'content', ]
        widgets = {
            'content': SummernoteInplaceWidget(),
        }
