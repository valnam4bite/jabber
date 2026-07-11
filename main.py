from catalog import Catalog
from sample_data import albums
from statistics import show_statistics

catalog = Catalog()

for album in albums:
    catalog.add(album)

print("=" * 40)
print("MUSIC COLLECTION")
print("=" * 40)

for album in catalog.all():
    print(album)
    print()

show_statistics(catalog.all())
