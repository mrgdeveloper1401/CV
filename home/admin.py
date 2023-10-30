from django.contrib import admin
from .models import SciolModel, AboutMeModels, SkillModel
from .models import EducationModel, ExpreienceWorkModel, ContactUsModel, ProjectModel
from django_jalali.admin.filters import JDateFieldListFilter

    
    
@admin.register(SciolModel)
class HeaderConetentScio(admin.ModelAdmin):
    list_display = ('user', 'sciol_name', 'sciol_url', 'id')
    search_fields = ('sciol_name', 'sciol_url', )
    list_filter = (('created_at', JDateFieldListFilter),)


@admin.register(AboutMeModels)
class AboutMeModelsAdmin(admin.ModelAdmin):
    list_display = ('user', 'explain', 'id')
    search_fields = ('explain', )
    list_filter = (('created_at', JDateFieldListFilter),)
    


@admin.register(SkillModel)
class SkillModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'skill_name', 'created_at', 'id')
    search_fields = ('skill_name',)


@admin.register(EducationModel)
class EducationModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'title_education', 'at_education', 'to_education', 'status_education', 'id')
    list_filter = (('created_at', JDateFieldListFilter),)
    
    
@admin.register(ExpreienceWorkModel)
class ExpreiencModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'exprience_title', 'at_date_exprence', 'to_date_exprence', 'id')
    
    
@admin.register(ProjectModel)
class ExprienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'project_url', 'created_at', 'status_project', 'id')
    search_fields = ('title', )
    list_filter = ('created_at',)
    list_editable = ('status_project', )
    
@admin.register(ContactUsModel)
class ContactUsModelAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'mobile_phone', 'id')
    list_filter = ('created_at', )