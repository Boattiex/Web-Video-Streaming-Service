import django_tables2 as tables
from .models import Livestream

class MyStreamTable(tables.Table):
    class Meta:
        model = Livestream
        template_name = 'django_tables2/bootstrap.html'
        fields = ('user', 'key', 'started_at', 'stopped_at')
