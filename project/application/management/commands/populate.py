import requests

from django.core.management.base import BaseCommand
from application.models import Province, City, Barangay

class Command(BaseCommand):
    def handle(self, *args, **options):
        data_url = 'https://raw.githubusercontent.com/flores-jacob/philippine-regions-provinces-cities-municipalities-barangays/master/philippine_provinces_cities_municipalities_and_barangays_2019v2.json'

        request = requests.get(data_url)
        data = request.json()

        region_keys = ["01", "02", "03", "4A", "4B", "05", "06", "07", "08", "09", "10", "11", "12", "13", "BARMM", "CAR", "NCR"]


        for region in region_keys:
            province_list = data[region]['province_list']

            for _province, municipality in province_list.items():
                Province(name=_province).save()
                get_province = Province.objects.filter(name=_province).last()
                print('Processing province...')

                for _municipal, barangay in municipality['municipality_list'].items():
                    city = City(name=_municipal, province=get_province).save()
                    get_city = City.objects.filter(name=_municipal).last()
                    print('Processing city...')

                    for place in barangay['barangay_list']:
                        Barangay(name=place, city=get_city).save()
                        print('Processing barangay...')

        self.stdout.write(self.style.SUCCESS('Successful!'))