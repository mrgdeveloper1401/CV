from django import forms
from .models import ContactUsModel, AboutMeModels, EducationModel, ExpreienceWorkModel, ProjectModel, SciolModel, SkillModel

    
class AboutMeForm(forms.ModelForm):
    class Meta:
        model = AboutMeModels
        exclude = ('created_at', 'user')
        

class SciolForm(forms.ModelForm):
    class Meta:
        model = SciolModel
        exclude = ('created_at', 'user')
        

class SkillForm(forms.ModelForm):
    class Meta:
        model = SkillModel
        exclude = ('user', 'created_at', 'image')
        
        
class EducationForm(forms.ModelForm):
    class Meta:
        model = EducationModel
        exclude = ('user', 'created_at')
        
        
class ExprienceWorkForm(forms.ModelForm):
    class Meta:
        model = ExpreienceWorkModel
        exclude = ('user', 'created_at')
        
        
class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUsModel
        exclude = ('created_at', )
        
        
class ProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectModel
        exclude = ('user', 'created_at')