from django.http import HttpResponse
from django.template import loader
from django.views.decorators.cache import never_cache


@never_cache
def home(request):
    """
    rendering ui by template for homepage
    this view never cache for delivering correct translation inside template
    """
    template = loader.get_template('weather/home.html')
    return HttpResponse(template.render({}, request))
