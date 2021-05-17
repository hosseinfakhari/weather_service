from django.utils.translation import gettext as _


def wind_degree_to_direction(degree: float) -> str:
    """
    converting wind direction to meaningful string
    Based on http://snowfence.umn.edu/Components/winddirectionanddegrees.htm
    """
    if 360 >= degree >= 348.75 or 0 <= degree < 11.25:
        return _('North')
    elif 11.25 <= degree < 33.75:
        return _('North-Northeast')
    elif 33.75 <= degree < 56.25:
        return _('Northeast')
    elif 56.25 <= degree < 78.75:
        return _('East-Northeast')
    elif 78.75 <= degree < 101.25:
        return _('East')
    elif 101.25 <= degree < 123.75:
        return _('East-Southeast')
    elif 123.75 <= degree < 146.25:
        return _('Southeast')
    elif 146.25 <= degree < 168.75:
        return _('South-Southeast')
    elif 168.75 <= degree < 191.25:
        return _('South')
    elif 191.25 <= degree < 213.75:
        return _('South-Southwest')
    elif 213.75 <= degree < 236.25:
        return _('Southwest')
    elif 236.25 <= degree < 258.75:
        return _('West-Southwest')
    elif 258.75 <= degree < 281.25:
        return _('West')
    elif 281.25 <= degree < 303.75:
        return _('West-Northwest')
    elif 303.75 <= degree < 326.25:
        return _('Northwest')
    elif 326.25 <= degree < 348.75:
        return _('North-Northwest')
    else:
        raise ValueError(f'Wind degree is not valid: {degree}')


def transform_openweather_response(response: dict) -> dict:
    """
    transforming openweathermap response to smaller and flatted dict
    as we need in our service.
    """
    wind_direction = wind_degree_to_direction(
        response.get('wind').get('deg')
    )
    return {
        'city': response.get('name'),
        'temp': response.get('main').get('temp'),
        'temp_min': response.get('main').get('temp_min'),
        'temp_max': response.get('main').get('temp_max'),
        'humidity': response.get('main').get('humidity'),
        'pressure': response.get('main').get('pressure'),
        'wind_speed': response.get('wind').get('speed'),
        'wind_direction': wind_direction,
        'description': response.get('weather')[0].get('description')
    }
