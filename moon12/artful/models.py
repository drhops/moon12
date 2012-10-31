'''
Models for Moon12.

Created on Oct 30, 2012
@author: Daniel Hopkins (drhops@gmail.com)
'''
from django.db import models

EMAIL_MAX_LENGTH = 25

class Artist(models.Model):
  """Model to represent an artist."""
  full_name = models.CharField(max_length=255)
  username = models.CharField(max_length=25, db_index=True, unique=True, blank=True, null=True)
  email = models.EmailField(max_length=EMAIL_MAX_LENGTH, blank=True, null=True, db_index=True, unique=True)
  short_bio = models.CharField(max_length=255, blank=True, null=True)
  website = models.CharField(max_length=255, blank=True, null=True)
  last_modified = models.DateTimeField(null=True, editable=False)

  def get_first_name(self):
    return self.full_name.split(" ")[0]
