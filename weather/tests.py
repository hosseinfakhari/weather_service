import asyncio
import aiohttp

from django.test import TestCase
from selenium import webdriver

from weather.services import fetch_city_weather
from weather.utils import wind_degree_to_direction


class FunctionalTestCases(TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def test_there_is_homepage(self):
        self.browser.get('http://localhost:8000/')
        self.assertIn('Weather App', self.browser.page_source)

    def test_temp_of_fereydunkenar(self):
        self.browser.get('http://localhost:8000/')
        city_name_input = self.browser.find_element_by_id('city_name_input')
        city_name_input.send_keys('fereydunkenar')
        self.browser.find_element_by_id('get_weather_button').click()
        time.sleep(5)
        self.assertIn('Fereydūnkenār', self.browser.page_source)

    def tearDown(self) -> None:
        self.browser.quit()

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


class UtilsUnitTestCases(TestCase):

    def test_wind_to_degree_wrong_degree(self):
        negative = -10
        out_of_degree = 361
        with self.assertRaises(ValueError):
            wind_degree_to_direction(negative)
        with self.assertRaises(ValueError):
            wind_degree_to_direction(out_of_degree)

    def test_wind_to_degree_north(self):
        lower = 11.24
        upper = 348.75
        inside = 10
        self.assertEqual(wind_degree_to_direction(lower), 'North')
        self.assertEqual(wind_degree_to_direction(upper), 'North')
        self.assertEqual(wind_degree_to_direction(inside), 'North')

    def test_wind_to_degree_north_northeast(self):
        lower = 11.25
        upper = 33.74
        inside = 15
        self.assertEqual(wind_degree_to_direction(lower), 'North-Northeast')
        self.assertEqual(wind_degree_to_direction(upper), 'North-Northeast')
        self.assertEqual(wind_degree_to_direction(inside), 'North-Northeast')

    def test_wind_to_degree_northeast(self):
        lower = 33.75
        upper = 56.24
        inside = 45
        self.assertEqual(wind_degree_to_direction(lower), 'Northeast')
        self.assertEqual(wind_degree_to_direction(upper), 'Northeast')
        self.assertEqual(wind_degree_to_direction(inside), 'Northeast')

    def test_wind_to_degree_east_northeast(self):
        lower = 56.25
        upper = 78.74
        inside = 60
        self.assertEqual(wind_degree_to_direction(lower), 'East-Northeast')
        self.assertEqual(wind_degree_to_direction(upper), 'East-Northeast')
        self.assertEqual(wind_degree_to_direction(inside), 'East-Northeast')

    def test_wind_to_degree_east(self):
        lower = 78.75
        upper = 101.24
        inside = 80
        self.assertEqual(wind_degree_to_direction(lower), 'East')
        self.assertEqual(wind_degree_to_direction(upper), 'East')
        self.assertEqual(wind_degree_to_direction(inside), 'East')

    def test_wind_to_degree_east_southeast(self):
        lower = 101.25
        upper = 123.74
        inside = 115
        self.assertEqual(wind_degree_to_direction(lower), 'East-Southeast')
        self.assertEqual(wind_degree_to_direction(upper), 'East-Southeast')
        self.assertEqual(wind_degree_to_direction(inside), 'East-Southeast')

    def test_wind_to_degree_southeast(self):
        lower = 123.75
        upper = 146.24
        inside = 135
        self.assertEqual(wind_degree_to_direction(lower), 'Southeast')
        self.assertEqual(wind_degree_to_direction(upper), 'Southeast')
        self.assertEqual(wind_degree_to_direction(inside), 'Southeast')

    def test_wind_to_degree_south_southeast(self):
        lower = 146.25
        upper = 168.74
        inside = 155
        self.assertEqual(wind_degree_to_direction(lower), 'South-Southeast')
        self.assertEqual(wind_degree_to_direction(upper), 'South-Southeast')
        self.assertEqual(wind_degree_to_direction(inside), 'South-Southeast')

    def test_wind_to_degree_south(self):
        lower = 168.75
        upper = 191.24
        inside = 175
        self.assertEqual(wind_degree_to_direction(lower), 'South')
        self.assertEqual(wind_degree_to_direction(upper), 'South')
        self.assertEqual(wind_degree_to_direction(inside), 'South')

    def test_wind_to_degree_south_southwest(self):
        lower = 191.25
        upper = 213.74
        inside = 200
        self.assertEqual(wind_degree_to_direction(lower), 'South-Southwest')
        self.assertEqual(wind_degree_to_direction(upper), 'South-Southwest')
        self.assertEqual(wind_degree_to_direction(inside), 'South-Southwest')

    def test_wind_to_degree_southwest(self):
        lower = 213.75
        upper = 236.24
        inside = 220
        self.assertEqual(wind_degree_to_direction(lower), 'Southwest')
        self.assertEqual(wind_degree_to_direction(upper), 'Southwest')
        self.assertEqual(wind_degree_to_direction(inside), 'Southwest')

    def test_wind_to_degree_west_southwest(self):
        lower = 236.25
        upper = 258.74
        inside = 240
        self.assertEqual(wind_degree_to_direction(lower), 'West-Southwest')
        self.assertEqual(wind_degree_to_direction(upper), 'West-Southwest')
        self.assertEqual(wind_degree_to_direction(inside), 'West-Southwest')

    def test_wind_to_degree_west(self):
        lower = 258.75
        upper = 281.24
        inside = 260
        self.assertEqual(wind_degree_to_direction(lower), 'West')
        self.assertEqual(wind_degree_to_direction(upper), 'West')
        self.assertEqual(wind_degree_to_direction(inside), 'West')

    def test_wind_to_degree_west_northwest(self):
        lower = 281.25
        upper = 303.74
        inside = 290
        self.assertEqual(wind_degree_to_direction(lower), 'West-Northwest')
        self.assertEqual(wind_degree_to_direction(upper), 'West-Northwest')
        self.assertEqual(wind_degree_to_direction(inside), 'West-Northwest')

    def test_wind_to_degree_northwest(self):
        lower = 303.75
        upper = 326.24
        inside = 310
        self.assertEqual(wind_degree_to_direction(lower), 'Northwest')
        self.assertEqual(wind_degree_to_direction(upper), 'Northwest')
        self.assertEqual(wind_degree_to_direction(inside), 'Northwest')

    def test_wind_to_degree_north_northwest(self):
        lower = 326.25
        upper = 348.74
        inside = 335
        self.assertEqual(wind_degree_to_direction(lower), 'North-Northwest')
        self.assertEqual(wind_degree_to_direction(upper), 'North-Northwest')
        self.assertEqual(wind_degree_to_direction(inside), 'North-Northwest')