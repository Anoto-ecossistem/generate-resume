from django import forms

class ResumeForm(forms.Form):
    full_name = forms.CharField(label='Nome Completo', max_length=100)
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Telefone', max_length=15)
    address = forms.CharField(label='Endereço', max_length=255, widget=forms.Textarea)
    education = forms.CharField(label='Educação', widget=forms.Textarea)
    experience = forms.CharField(label='Experiência Profissional', widget=forms.Textarea)
    skills = forms.CharField(label='Habilidades', widget=forms.Textarea)