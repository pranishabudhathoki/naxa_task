from secrets import randbelow
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.utils.crypto import get_random_string
from user.models import City, UserProfile
import random


class Command(BaseCommand):
   
    help = "Create default UserProfile"

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        city_count=City.objects.all().count()
        users=User.objects.first()
        for i in range(total):
            my_city=City.objects.get(id=random.randint(1,city_count))
            username=get_random_string()
            UserProfile.objects.create(user=users,first_name=get_random_string(),last_name=get_random_string(), email=f"{username}@gmail.com",city=my_city)