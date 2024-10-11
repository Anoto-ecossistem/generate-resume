from django.shortcuts import render
from .forms import ResumeForm
import requests
import json

def generate_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            # Obtenha os dados do formulário
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            education = form.cleaned_data['education']
            experience = form.cleaned_data['experience']
            skills = form.cleaned_data['skills']

            # Renderizar o template do currículo com os dados
            context = {
                'full_name': full_name,
                'email': email,
                'address': address,
                'education': education,
                'experience': experience,
                'skills': skills,
            }
            return render(request, 'generated_resume.html', context)
    else:
        form = ResumeForm()
    
    return render(request, 'resume_form.html', {'form': form})

def get_job_listings(keywords, location):
    host = 'jooble.org'
    api_key = 'YOUR_API_KEY'
    
    url = f'https://{host}/api/{api_key}'
    headers = {"Content-Type": "application/json"}
    body = {
        "keywords": keywords,
        "location": location
    }

    # Fazer a requisição
    response = requests.post(url, headers=headers, json=body)
    
    # Verificar se a resposta foi bem-sucedida
    if response.status_code == 200:
        jobs = response.json()
        return jobs
    else:
        return "erro na requisição"
    