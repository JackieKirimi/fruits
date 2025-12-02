from django.forms import ModelForm #helps create the input form
from .models import Fruit #helps bring in the data

class FruitForm(ModelForm):
    class Meta:
        model=Fruit
        fields='__all__' #to bring in all the fields from the model