from django.forms import ModelForm
from .models import *


class FabricForm(ModelForm):
    class Meta:
        model = Fabric
        fields = '__all__'
