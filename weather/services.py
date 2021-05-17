from django.conf import settings


async def fetch_city_weather(session, city_name, language):
    """
    fetching weather information from openweathermap by city
    """
    api_key = settings.OPEN_WEATHER_MAP_API_KEY
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}" \
          f"&appid={api_key}&units=metric&lang={language}"
    async with session.get(url) as response:
        if response.status == 200:
            return await response.json()
        else:
            return response.status
