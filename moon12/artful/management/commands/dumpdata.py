import sys

import codecs
from django.core.management.commands.dumpdata import Command as Dumpdata

class Command(Dumpdata):
  def execute(self, *args, **options):
    print 'XXX'
    stdout = options.get('stdout', sys.stdout)
    options['stdout'] = codecs.getwriter('utf8')(stdout)
    return super(Command, self).execute(*args, **options)
