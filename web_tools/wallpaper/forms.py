from django.forms import ModelForm
from .models import Wallpaper


class WallpaperForm(ModelForm):
    class Meta:
        model = Wallpaper
        fields = '__all__'
