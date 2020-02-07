from django import forms

class testimoniform(forms.Form):
    nama = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'input-md round form-control',
                'placeholder':'nama',
            }
        )
    )
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'input-md round form-control',
                'placeholder':'email',
            }
        )
    )
    perihal = forms.CharField(
        required=True,
        widget=forms.TextInput(
            
            attrs={
                'class':'input-md round form-control',
                'placeholder':'perihal',
            }
        )
    )
    deskripsi = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'class':'input-md round form-control',
                'placeholder':'deskripisi',
                'style':'height: 130px;',
            }
        )
    )