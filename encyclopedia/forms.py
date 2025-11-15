from django import forms

class NuevoSearchForm(forms.Form):
    q = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "search",
                "placeholder": "Search Encyclopedia"
            }
        )
    )
