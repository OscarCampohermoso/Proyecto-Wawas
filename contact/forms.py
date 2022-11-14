"""from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):

    Name = forms.CharField(widget=forms.TimeInput(attrs={"class":"form-control"}))
    Email = forms.CharField(widget=forms.TimeInput(attrs={"class":"form-control"}))
    Phone = forms.CharField(widget=forms.TimeInput(attrs={"class":"form-control"}))

    class Meta:
        model = Contact
        fields = ["Name", "Email", "Phone"]
        #"    "= '__all__'"""