import django_filters
from django_filters import DateFilter

from .models import *

# a Python class that will build a filter for us
# very similar to model forms
class OrderFilter(django_filters.FilterSet):
    # making a custom input field
    start_date = DateFilter(field_name="date_created", lookup_expr='gte')
    end_date = DateFilter(field_name="date_created", lookup_expr='lte')
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date_created']