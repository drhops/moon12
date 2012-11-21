from django.core.serializers.json import Serializer as JSONSerializer
from django.core.serializers.json import Deserializer as JSONDeserializer
from django.core.serializers.json import DjangoJSONEncoder
from django.utils import simplejson

class Serializer(JSONSerializer):
  def end_serialization(self):
    simplejson.dump(self.objects, self.stream, cls=DjangoJSONEncoder, ensure_ascii=False, **self.options)

Deserializer = JSONDeserializer
