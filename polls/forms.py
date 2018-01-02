from django import forms

class myform(forms.Form):
    myfield = forms.CharField(label='Youre Name', max_length='100')



