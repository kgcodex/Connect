import os
import uuid

from django.utils.deconstruct import deconstructible


@deconstructible
class UploadWithUUIDFilename:
    """
    Callable class to rename uploaded files to a UUID while preserving the file extension.
    """

    def __init__(self, path):
        self.path = path

    def __call__(self, instance, filename):
        # instance and filename are required by Django
        ext = os.path.splitext(filename)[-1].lower()
        new_filename = f"{uuid.uuid4()}{ext}"
        return os.path.join(self.path, new_filename)
