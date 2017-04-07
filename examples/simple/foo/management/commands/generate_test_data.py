from django.core.management.base import BaseCommand

from admin_timeline.tests.test_core import generate_data


class Command(BaseCommand):
    def handle(self, *args, **options):
        generate_data()
