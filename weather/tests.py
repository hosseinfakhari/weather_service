import asyncio
import aiohttp

from django.test import TestCase

from weather.services import fetch_city_weather


class IntegrationTestCases(TestCase):

    async def test_fetch_city_weather_success_response(self):
        async with aiohttp.ClientSession() as client:
            task = asyncio.ensure_future(
                fetch_city_weather(client, 'Tehran', 'en')
            )
            response = await task
            self.assertEqual('Tehran', response.get('name'))

    async def test_fetch_city_weather_not_found(self):
        async with aiohttp.ClientSession() as client:
            task = asyncio.ensure_future(
                fetch_city_weather(client, 'NotInEntireUniverse', 'en')
            )
            response = await task
            self.assertEqual(404, response)
