from django.db import models
import uuid


class Application(models.Model):
    name = models.CharField('app name', max_length=255, unique=True)
    key = models.UUIDField('api key', default=uuid.uuid4, editable=False, db_index=True)

    def __str__(self):
        return self.name

    def generate_new_key(self):
        """ Generates new api key """
        self.key = uuid.uuid4()
        self.save()
