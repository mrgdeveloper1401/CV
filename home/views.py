from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .models import SciolModel, AboutMeModels, SkillModel, EducationModel, ExpreienceWorkModel, ProjectModel
from .form import ContactUsForm, AboutMeForm, SciolForm, SkillForm, EducationForm, ExprienceWorkForm, ProjectForm


class HomeView(View):
    templated_name = 'home/home.html'
    form_class = ContactUsForm
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == request.user:
            messages.error(request, 'You are not authorized to', 'danger')
        return super().dispatch(request, *args, **kwargs)

    
    
    def get(self, request):
        # navbar = NvbarModel.objects.published()
        # header_content = HeaderConetent.objects.all()
        sciol = SciolModel.objects.all()
        about = AboutMeModels.objects.all()
        skill = SkillModel.objects.all()
        education = EducationModel.objects.all()
        project = ProjectModel.objects.all()
        exprience = ExpreienceWorkModel.objects.all()
        form = self.form_class()
        context = {
            # 'navbar': navbar,
            # 'hcontent': header_content,
            'sciol':sciol,
            'about': about,
            'skills': skill,
            'education': education,
            'projects': project,
            'expriece': exprience,
            'form': form
            
        }
        return render(request, self.templated_name, context)
    
    
class AboutMeView(View):
    templated_name = 'home/about_me.html'
    form_class = AboutMeForm
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.templated_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            AboutMeModels.objects.create(
                user = request.user,
                image = cd['image'],
                explain = cd['explain'],
                job = cd['job'],
            )
            return redirect('home:sciol', request.user.id )
        return render(request, self.templated_name, {"form": form})
    

class SciolView(View):
    templated_name = 'home/sciol.html'
    form_class = SciolForm
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.templated_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            SciolModel.objects.create(
                user = request.user,
                sciol_name = cd['sciol_name'],
                sciol_url = cd['sciol_url'],
            )
            return redirect('home:skill', request.user.id)
        return render(request, self.templated_name, {'form': form})
    
    
class SkillView(View):
    templated_name = 'home/skill.html'
    form_class = SkillForm
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.templated_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            SkillModel.objects.create(
                user = request.user,
                skill_name = cd['skill_name'],
            )
            return redirect('home:education', request.user.id)
        return render(request, self.templated_name, {'form': form})
    

class EducationView(View):
    templated_name = 'home/education.html'
    form_class = EducationForm
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.templated_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            EducationModel.objects.create(
                user = request.user,
                title_education = cd['title_education'],
                explain_education = cd['explain_education'],
                at_education = cd['at_education'],
                to_education = cd['to_education'],
                status_education =cd['status_education']   
            )
            return redirect('home:exprience', request.user.id)
        return render(request, self.templated_name, {'form': form})
    
    
class ExprienceWorkView(View):
    templated_name = 'home/exprience_work.html'
    form_class = ExprienceWorkForm
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.templated_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            ExpreienceWorkModel.objects.create(
                user = request.user,
                exprience_title = cd['exprience_title'],
                explain_exprence = cd['explain_exprence'],
                link_company = cd['link_company'],
                image = cd['image'],
                at_date_exprence = cd['at_date_exprence'],
                to_date_exprence = cd['to_date_exprence'],
            )
            return redirect('home:project', request.user.id)
        return render(request, self.templated_name, {'form': form})
    

class ProjectView(View):
    templated_name = 'home/project.html'
    form_class = ProjectForm
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.templated_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            ProjectModel.objects.create(
                user = request.user,
                title = cd['title'],
                project_url = cd['project_url'],
                image = cd['image'],
                status_project = cd['status_project']
            )
            messages.success(request, 'resemeh created successfully', 'success')
            return redirect('home:home')
        return render(request, self.templated_name, {'form': form})
        