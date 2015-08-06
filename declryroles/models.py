from django.db import models
from django.contrib.contenttypes.models import ContentType

class Role(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return u'{}'.format(self.name)



class Permission(models.Model):
    content_type = models.ForeignKey(ContentType, related_name="permissions")
    name = models.CharField(max_length=255)
    instance_perm = models.BooleanField(default=False)
    roles = models.ManyToManyField(Role)

    def __unicode__(self):
        return u'{} {}'.format(self.name, 'model' if not self.instance_perm else 'instance')
