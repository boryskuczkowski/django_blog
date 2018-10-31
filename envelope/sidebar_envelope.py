from .forms import MyContactForm


def foo(request):
    """
    Adds form to context
    """

    context = {
        'e_form': MyContactForm()

    }

    return context
