from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Load data from fixture"

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()
        call_command("loaddata", "catalog.json")
        self.stdout.write(self.style.SUCCESS(
            "Successfully loaded data from fixture"
            )
        )
