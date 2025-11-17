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

class NuevaEntradaForm(forms.Form):
    title = forms.CharField(
        label="Title",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Entry Title",
                "class": "form-control"
            }
        )
    )
    content = forms.CharField(
        label="Content",
        widget=forms.Textarea(
            attrs={
                "placeholder": "Entry Content in Markdown",
                "class": "form-control"
            }
        )
    )
