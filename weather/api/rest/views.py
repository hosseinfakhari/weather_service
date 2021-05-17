import asyncio
import aiohttp
from django.utils import translation
from django.utils.translation import gettext as _
from django.http.response import (
    JsonResponse,
    HttpResponseNotFound,
    HttpResponseForbidden,
    HttpResponseBadRequest
)
from weather.utils import transform_openweather_response
from weather.services import fetch_city_weather


async def get_weather_by_city(request, city_name):
    """
    provides rest api to get a weather information by its city.
    """
    user_lang = request.GET.get("LANG") if request.GET.get("LANG") else 'en'
    translation.activate(user_lang)
    timeout = aiohttp.ClientTimeout(total=60)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        task = asyncio.ensure_future(
            fetch_city_weather(session, city_name, user_lang)
        )
        response = await task
    if response == 404:
        return HttpResponseNotFound(_('City not found'))
    elif response == 401:
        return HttpResponseForbidden(_('Unauthorized'))
    elif response == 429:
        return HttpResponseBadRequest(_('API Rate Limit'))
    else:
        result = transform_openweather_response(response)
        return JsonResponse(result)
