from django.contrib import admin
from .models import SciolModel, AboutMeModels, SkillModel, AwardsModel
from .models import EducationModel, ExpreienceWorkModel, ContactUsModel, ProjectModel
from django_jalali.admin.filters import JDateFieldListFilter

    
    
@admin.register(SciolModel)
class SciolAdmin(admin.ModelAdmin):
    list_display = ('user', 'sciol_name', 'sciol_url', 'id')
    search_fields = ('sciol_name', 'sciol_url', )
    list_filter = (('created_at', JDateFieldListFilter),)


@admin.register(AboutMeModels)
class AboutMeModelsAdmin(admin.ModelAdmin):
    list_display = ('user', 'job', 'marital_status', 'gender_choose', 'birth_day', 'age', 'id')
    search_fields = ('user', )
    list_filter = (('created_at', JDateFieldListFilter), 'marital_status' ,'gender_choose', )
    


@admin.register(SkillModel)
class SkillModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'skill_name', 'created_at', 'id')
    search_fields = ('skill_name',)


@admin.register(EducationModel)
class EducationModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'fields_of_study', 'at_education', 'to_education', 'status_education', 'id')
    list_filter = (('created_at', JDateFieldListFilter),)
    
    
@admin.register(ExpreienceWorkModel)
class ExpreienceWorkAdmin(admin.ModelAdmin):
    list_display = ('user', 'job_title', 'at_date_exprence', 'to_date_exprence', 'status_work', 'id')
    
    
@admin.register(ProjectModel)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'from_date', 'up_to_date', 'status_project', 'id')
    search_fields = ('title', )
    list_filter = ('created_at',)
    

class AwardsAdmin(admin.ModelAdmin):
    list_display = ('awards_name', 'year_awards', 'id')
    list_filter = ('year_awards',)
    
@admin.register(ContactUsModel)
class ContactUsModelAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'mobile_phone', 'id')
    list_filter = ('created_at', )
    

class AwardsModelAdmin(admin.ModelAdmin):
    list_display = ('awards_name', 'year_awards', 'id')
    list_filter = ('created_at',)