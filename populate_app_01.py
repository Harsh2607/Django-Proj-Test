# from faker import faker
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Django_Project_01.settings")

import django
django.setup()

# Script to populate models with fake data
import random
from Django_App_01.models import Musician, Album
from faker import Faker as fk

fake_obj_1 = fk()

# Create fake Musician data
def create_musician():
    first_name = fake_obj_1.first_name()
    last_name = fake_obj_1.last_name()
    instrument = fake_obj_1.random_element(elements=('Guitar', 'Piano', 'Violin', 'Drums'))
    musician, created  = Musician.objects.get_or_create(first_name=first_name, last_name=last_name, instrument=instrument)
    # musician.save()
    return musician

# Create fake Album data
def create_album(musician):
    name = fake_obj_1.catch_phrase()
    release_date = fake_obj_1.date_this_decade()
    num_stars = random.randint(1, 5)
    album, created = Album.objects.get_or_create(artist=musician, name=name, release_date=release_date, num_stars=num_stars)
    # album.save()
    return album

# Populate models
def populate_models(n=10):
    for entry in range(n):
        new_musician = create_musician()
        create_album(new_musician)

if __name__ == '__main__':
    print("Populate models start")
    populate_models(10)
    print("Populate models complete")
