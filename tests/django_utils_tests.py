import unittest

from django.template.context import Context

from pants_utils import django_utils

class PantsUtilsDjangoTestCase(unittest.TestCase):
    def setUp(self):
        self.loader = django_utils.EggAppLoader()
        self.storage = django_utils.EggStorage('tests')
        self.finder = django_utils.EggFinder('tests')

    def test_eggapploader(self):
        template, display_name  = self.loader('tests/index.html')
        self.assertEquals(template.render(Context()), 'hello world\n')

    def test_eggstorage_exists(self):
        self.assertTrue(self.storage.exists("static/staticfile.txt"))
        self.assertFalse(self.storage.exists("static/this/does/not/exist.txt"))

    def test_eggstorage_open(self):
        self.assertEqual(self.storage.open("templates/index.html").read(), 'hello world\n')
        self.assertRaises(IOError, self.storage.open, "THISDOESNTEXIST")

    def test_eggfinder_find(self):
        self.assertIsNotNone(self.finder.find('templates/index.html'))
        self.assertIsNone(self.finder.find('this/does/not/exist'))

    def test_eggfinder_list(self):
        found = self.finder.list([])
        self.assertIn('django_utils_tests.py', [file for file, storage in list(found)])
