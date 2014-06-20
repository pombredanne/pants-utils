import pkg_resources
import sys

from django.contrib.staticfiles.finders import BaseStorageFinder
from django.contrib.staticfiles import utils
from django.core.files.storage import Storage
from django.utils.functional import LazyObject
from django.core.files.base import File


class EggStorage(Storage):
    '''
    Assumes that absolute path is:
    <module>/<resource_path>

    Read-only Storage. Raise NotImplemented if attempt to write
    '''

    def __init__(self, module):
        self.module = module

    def _open(self, name, mode='rb'):
        return File(pkg_resources.resource_stream(self.module, name))

    def _save(self, name, content):
        raise NotImplementedError("This backend is read-only")

    def exists(self, name):
        return pkg_resources.resource_exists(self.module, name)

    def listdir(self, name):
        directories, files = [], []
        for entry in pkg_resources.resource_listdir(self.module, name):
            if pkg_resources.resource_isdir(self.module, entry):
                directories.append(entry)
            else:
                files.append(entry)
        return directories, files

    def size(self, name):
        return sys.getsizeof(self._open(name))

class EggFinder(BaseStorageFinder):
    storage = EggStorage
    def __init__(self, module, storage=None, *args, **kwargs):
        self.module = module

        if not isinstance(self.storage, (Storage, LazyObject)):
            self.storage = self.storage(module)

        super(EggFinder, self).__init__(storage, *args, **kwargs)

    def find(self, path, all=False):
        return path if self.storage.exists(path) else None

    def list(self, ignore_patterns):
        for path in utils.get_files(self.storage, ignore_patterns):
            yield path, self.storage
