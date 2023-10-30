from django.shortcuts import render
# from .models import NvbarModel, HeaderConetent, HeaderConetentSciol, AboutMeModels, SkillModel, ExpreiencModel, ExprienceProjec
from django.views import View
from django.contrib import messages
from .models import HeaderConetent, HeaderConetentSciol, AboutMeModels, SkillModel, EducationModel
from .models import ExpreiencModel, ExprienceProject
from .form import ContactUsForm


class HomeView(View):
    templated_name = 'home/home.html'
    form_class = ContactUsForm
    def get(self, request):
        # navbar = NvbarModel.objects.published()
        header_content = HeaderConetent.objects.all()
        sciol = HeaderConetentSciol.objects.all()
        about = AboutMeModels.objects.all()
        skill = SkillModel.objects.all()
        education = EducationModel.objects.all()
        project = ExprienceProject.objects.all()
        exprience = ExpreiencModel.objects.all()
        form = self.form_class()
        context = {
            # 'navbar': navbar,
            'hcontent': header_content,
            'sciol':sciol,
            'about': about,
            'skills': skill,
            'education': education,
            'projects': project,
            'expriece': exprience,
            'form': form
            
        }
        return render(request, self.templated_name, context)