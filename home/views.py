from django.shortcuts import render
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
        pass
    

class SciolView(View):
    templated_name = 'home/sciol.html'
    form_class = SciolForm
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.templated_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        pass
    
    
class SkillView(View):
    templated_name = 'home/skill.html'
    form_class = SkillForm
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.templated_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        pass
    

class EducationView(View):
    templated_name = 'home/education.html'
    form_class = EducationForm
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.templated_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        pass
    
    
class ExprienceWorkView(View):
    templated_name = 'home/exprience_work.html'
    form_class = ExprienceWorkForm
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.templated_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        pass
    

class ProjectView(View):
    templated_name = 'home/project.html'
    form_class = ProjectForm
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.templated_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        pass