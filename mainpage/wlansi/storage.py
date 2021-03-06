from django.conf import settings

from filer import storage

class PrefixedStorageMixin(object):
    """
    Mixin for file-system based storage, which if file is missing locally, add
    a prefix to the URL, assuming it is stored somewhere else.
    """

    def url(self, name):
        url = super(PrefixedStorageMixin, self).url(name)
        if self.exists(name):
            return url
        else:
            return '%s%s' % (settings.FILE_STORAGE_PREFIX, url)

class PublicFileSystemStorage(PrefixedStorageMixin, storage.PublicFileSystemStorage):
    pass

class PrivateFileSystemStorage(PrefixedStorageMixin, storage.PrivateFileSystemStorage):
    pass
