import unittest

from django.template.context import Context

from pants_utils import django_utils

class PantsUtilsDjangoTestCase(unittest.TestCase):
    def test_hello_world(self):
        loader = django_utils.EggAppLoader()
        template, display_name  = loader('tests/index.html')
        self.assertEquals(template.render(Context()), 'hello world\n')
