from django import forms
from . models import Users

# class Usersforms(forms.Form):
#     first_name = forms.CharField(max_length=50)
#     last_name = forms.CharField(max_length=50)
#     age = forms.IntegerField()
#     email = forms.EmailField()
#     date_of_birth = forms.DateField()

class Usersforms1(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'age', 'email', 'picture']