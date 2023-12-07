"""Forms of the project."""

# Create your forms here.
from .models import Thing
from django import forms

class ThingForm(forms.ModelForm):
    """Form for the Thing model."""

    class Meta:
        """Meta class to define the model and fields."""

        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {'description': forms.Textarea(),
                   'quantity': forms.NumberInput(attrs={'min': 0, 'max': 50})
        }




