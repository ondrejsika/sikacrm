from django.core.management.base import BaseCommand

from crm.cli import run

class Command(BaseCommand):
    help = 'CRM CLI'

    def handle(self, *args, **options):
        run(*args, **options)
