from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.utils.crypto import get_random_string
from user.models import City
import random


class Command(BaseCommand):
   
    help = "Create default Cities"

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of cities to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        cities=['kathmandu','lalitpur','Bhaktapur','Jhapa','Biratnagar','Birgunj','Daharan','Dahading','Pokhara','Chitwan']
        
        for i in range(total):
            city_name=random.choice(cities)

            City.objects.create(city=city_name,district=city_name,state=random.randint(1,7))
           