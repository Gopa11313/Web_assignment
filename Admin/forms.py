from django import forms

from Admin.models import Customer, Admin


class login(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailField)

    class Meta:
        model = Customer
        fields = "__all__"


class AdminForm(forms.ModelForm):

    class Meta:
        model = Admin
        fields = "__all__"
