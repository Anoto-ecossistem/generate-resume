from django.shortcuts import render
from .forms import ResumeForm

def generate_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            # Obtenha os dados do formulário
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            education = form.cleaned_data['education']
            experience = form.cleaned_data['experience']
            skills = form.cleaned_data['skills']

            # Renderizar o template do currículo com os dados
            context = {
                'full_name': full_name,
                'email': email,
                'phone': phone,
                'address': address,
                'education': education,
                'experience': experience,
                'skills': skills,
            }
            return render(request, 'generated_resume.html', context)
    else:
        form = ResumeForm()
    
    return render(request, 'resume_form.html', {'form': form})