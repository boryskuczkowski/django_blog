from .models import Category


def category_list(request):

    return {'category_list': Category.objects.order_by('name')}
