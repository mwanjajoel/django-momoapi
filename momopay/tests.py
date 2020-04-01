from io import StringIO

import json
import httpretty
from django.core.management import call_command
from django.core.management.base import CommandError
from django.test import TestCase
from momopay.util import create_api_user, get_api_user


class MomoinitTest(TestCase):

    @httpretty.activate
    def test_create_api_user(self):
        httpretty.register_uri(
            httpretty.POST, "https://ericssonbasicapi2.azure-api.net/v1_0/apiuser",
            status=201)
        key = 'aaglgttgwg325262532gsgsdsdg'
        res = create_api_user(key)
        self.assertNotEquals(None, res)

    @httpretty.activate
    def test_get_api_user(self):
        httpretty.register_uri(
            httpretty.POST, "https://ericssonbasicapi2.azure-api.net/v1_0/apiuser/1/apikey",
            body=json.dumps({"apiKey": "aaglgttgwg325262532gsgsdsdg"}),status=201)
        key = 'aaglgttgwg325262532gsgsdsdg'
        id = 1
        res = get_api_user(id, key)
        self.assertNotEquals(None, res)

    @httpretty.activate
    def test_command_output(self):
        key = 'aaglgttgwg325262532gsgsdsdg'
        httpretty.register_uri(
            httpretty.POST,
            "https://ericssonbasicapi2.azure-api.net/v1_0/apiuser/1/apikey",
            body=json.dumps({"apiKey": "aaglgttgwg325262532gsgsdsdg"}),status=201)
        out = StringIO()
        call_command('momoinit', key, '--uuid', 1, stdout=out)
        self.assertIn('apiKey', out.getvalue())

    @httpretty.activate
    def test_command_error_raised(self):
        key = 'aaglgttgwg325262532gsgsdsdg'
        httpretty.register_uri(
            httpretty.POST,
            "https://ericssonbasicapi2.azure-api.net/v1_0/apiuser/1/apikey",
            status=400)
        out = StringIO()
        try:
            call_command('momoinit', key, '--uuid', 1, stdout=out)
        except CommandError:
            pass
