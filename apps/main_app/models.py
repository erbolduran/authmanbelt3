from __future__ import unicode_literals
from django.db import models
from ..login.models import User



class T_plan(models.Model):
    destination = models.CharField(max_length=60)
    description = models.TextField(max_length=400)
    startdate = models.TextField(max_length=400)
    enddate = models.TextField(max_length=400)
    user = models.ForeignKey(User, related_name="messages")
    joined_by = models.ManyToManyField(User, related_name="joinedplans")

    # objects = UserManager()
    def __unicode__(self):
        return 'destination: {}, user: {}, description: {}, startdate: {}, enddate: {},  joined_by: {}, id: {}'.format(self.destination, self.user, self.description, self.startdate, self.enddate, self.joined_by, self.id)

