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

def get_job_listings():
    host = 'jooble.org'
    api_key = 'YOUR_API_KEY'
    
    url = f'https://jooble.org/api/{api_key}/'
    headers = {"Content-Type": "application/json"}
    body = {
        "keywords": "web developer in USA",
        "location": "USA" 
    }

    try:
        response = requests.post(url, headers=headers, json=body)
        
        # Verifica se a resposta foi bem-sucedida
        if response.status_code == 200:
            jobs = response.json()
            return jobs
        else:
            print(f"Erro na requisição. Status Code: {response.status_code}, Conteúdo: {response.text}")
            return None
    except Exception as e:
        print(f"Erro ao tentar se conectar à API: {str(e)}")
        return None

def job_listings(request):
    jobs = get_job_listings()
    
    # Verifica se a função retornou algo
    if jobs:
        return render(request, 'job_listings.html', {'jobs': jobs['jobs']})
    else:
        return render(request, 'job_listings.html', {'error': 'Nenhum emprego encontrado ou erro na requisição.'})