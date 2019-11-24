from django.db import models
import uuid


class Application(models.Model):
    name = models.CharField('app name', max_length=255)
    key = models.UUIDField('api key', default=uuid.uuid4, editable=False)

    def generate_new_key(self):
        self.key = uuid.uuid4()
        self.save()