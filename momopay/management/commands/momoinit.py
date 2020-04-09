import os
from uuid import uuid4

import requests
from django.core.management.base import BaseCommand, CommandError
from dotenv import load_dotenv
from momopay.util import create_api_user, get_api_user


load_dotenv()

class Command(BaseCommand):
    help = "Create Momo Api User"

    def add_arguments(self, parser):
        parser.add_argument('key')
        parser.add_argument('--uuid')

    def handle(self,*args, **options):
        key = options['key']
        if options['uuid']:
            id = options['uuid']
        else:
            id = create_api_user(key)
            if id is None:
                raise CommandError('Momo init failed')
        output = get_api_user(id, key)
        if output is None:
            raise CommandError('Momo init failed')
        self.stdout.write(self.style.SUCCESS(f"id: {output['id']}  apiKey: {output['apiKey']}"))
