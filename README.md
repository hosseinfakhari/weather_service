
# Weather Service

Show the current weather for any city.

## Build and Run

To build and run this project using docker and docker-compose simply run:

```bash
echo "DEBUG=False
SECRET_KEY='oneOfTheMostSecureSecretsInTheWorld'
OPEN_WEATHER_MAP_API_KEY='your api key from OWM'
MEMCACHED_URL=memcached:11211
CACHE_TTL=60" >> .env

docker-compose up -d
```
* replace `OPEN_WEATHER_MAP_API_KEY` And `SECRET_KEY` with your own string in `.env` file

then open your browser and navigate to `http://localhost:8000`## API Reference

## API Reference

#### Get item

```http
  GET /api/v1/weather/city/${city_name}?LANG=${LANGUAGE_CODE}
```

| Parameter  | Type     | Description                       |
| :--------  | :------- | :-------------------------------- |
| `city_name`| `string` | **Required**. Id of item to fetch |
| `LANG`     | `string` | **Optional**. lang code. e.g: `es`|

Returns weather information by desired language.

## Testing 

run the blow command for testing service

```bash 
  python3 -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
  python manage.py test
```
Testing includes `selenium firefox webdriver`, so make sure that you have the `geckodriver` in your os PATH and Firefox browser is installed on your computer.
- [Download geckodriver](https://github.com/mozilla/geckodriver/releases)
