from django.shortcuts import render
from django.views import View
from django.contrib import messages
from .models import SciolModel, AboutMeModels, SkillModel, EducationModel, ExpreienceWorkModel, ProjectModel
from .form import ContactUsForm


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