from django_seed import Seed
seeder = Seed.seeder()
from .models import sports,player
seeder.add_entity(sports,14)
seeder.add_entity(player,14)
inserted_pks = seeder.execute()
