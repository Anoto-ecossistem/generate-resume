from django import forms

class ResumeForm(forms.Form):
    full_name = forms.CharField(label='Name', max_length=100,widget=forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:border-blue-500 bg-gray-700 text-white'}))
    email = forms.EmailField(label='E-mail' , widget=forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:border-blue-500 bg-gray-700 text-white'}))
    address = forms.CharField(label='Adress or Location', max_length=255, widget=forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:border-blue-500 bg-gray-700 text-white'}))
    education = forms.CharField(label='Education', widget=forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:border-blue-500 bg-gray-700 text-white'}))
    experience = forms.CharField(label='Experience',widget=forms.Textarea(attrs={'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:border-blue-500 bg-gray-700 text-white',
     'rows': '4',
     'placeholder': 'write your experience...'}))
    skills = forms.CharField(label='Habilities and tags', widget=forms.Textarea(attrs={'class': 'w-full px-3 py-2 border rounded-md focus:outline-none focus:border-blue-500 bg-gray-700 text-white',
     'rows': '4',
     'placeholder': 'tags and certificates like aws, javascript, java, framework...'}))