from django.core.management.base import BaseCommand

from crm.cli import run


class Command(BaseCommand):
    help = 'CRM CLI'

    def add_arguments(self, parser):
        parser.add_argument('extra', nargs='+', type=str)

    def handle(self, *args, **options):
        run(*options['extra'])
