from django import forms

class form_keranjang(forms.Form):
    jumlah = forms.IntegerField(
        label=False,
        widget=forms.TextInput(
            attrs={
                'id':'jumlah',
                'type':'number',
                'min':'0',
                'class':'input-md form-control',
                'placeholder':'Jumlah',
            }
        ))