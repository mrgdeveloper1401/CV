from django.contrib import admin
from .models import NvbarModel, HeaderConetent, HeaderConetentSciol, AboutMeModels, SkillModel, EducationModel, ExpreiencModel, ContactUsModel, ContentInfoModel
import django_jalali.admin as jadmin
from django_jalali.admin.filters import JDateFieldListFilter



@admin.register(NvbarModel)
class NvbarModelAdmin(admin.ModelAdmin):
    list_display = ('navbar_name', 'navbar_status', 'id')
    list_editable = ('navbar_status', )
    list_filter = (
        ('created_at', JDateFieldListFilter),
    )
    

@admin.register(HeaderConetent)
class HeaderConetentAdmin(admin.ModelAdmin):
    list_display = ('text', 'id')
    list_filter = (('created_at', JDateFieldListFilter),)
    search_fields = ('text',)
    
    
@admin.register(HeaderConetentSciol)
class HeaderConetentScio(admin.ModelAdmin):
    list_display = ('sciol_name', 'sciol_url', 'id')
    search_fields = ('sciol_name', 'sciol_url', )
    list_filter = (('created_at', JDateFieldListFilter),)


@admin.register(AboutMeModels)
class AboutMeModelsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'explain', 'id')
    search_fields = ('explain', )
    list_filter = (('created_at', JDateFieldListFilter),)
    


@admin.register(SkillModel)
class SkillModelAdmin(admin.ModelAdmin):
    list_display = ('skill_name', 'created_at', 'id')
    search_fields = ('skill_name',)


@admin.register(EducationModel)
class EducationModelAdmin(admin.ModelAdmin):
    list_display = ('title_education', 'at_education', 'to_education', 'busy', 'id')
    list_filter = (('created_at', JDateFieldListFilter),)
    
    
@admin.register(ExpreiencModel)
class ExpreiencModelAdmin(admin.ModelAdmin):
    list_display = ('exprense_title', 'at_date_exprence', 'to_date_exprence', 'status_project','id')
    list_editable = ('status_project', )
    search_fields = ('exprense_title', 'created_at')
    
    
@admin.register(ContactUsModel)
class ContactUsModelAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'mobile_phone', 'id')
    
    
# @admin.register(ContentInfoModel)
# class ContentInfoModelAdmin(admin.ModelAdmin):
#     list_display = ('full_name', 'email', 'mobile_phone', 'id')