from django.contrib import admin
from .models import NvbarModel, HeaderConetent, HeaderConetentSciol, AboutMeModels, SkillModel, EducationModel, ExpreiencModel, AboutMeModel, ContactUsModel, ContentInfoModel




@admin.register(NvbarModel)
class NvbarModelAdmin(admin.ModelAdmin):
    list_display = ('navbar_name', 'navbar_status', 'id')
    list_editable = ('navbar_status', )
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('created_at',)
    

@admin.register(HeaderConetent)
class HeaderConetentAdmin(admin.ModelAdmin):
    list_display = ('text', 'id')
    
    
@admin.register(HeaderConetentSciol)
class HeaderConetentScio(admin.ModelAdmin):
    pass


@admin.register(AboutMeModels)
class AboutMeModelsAdmin(admin.ModelAdmin):
    pass


@admin.register(SkillModel)
class SkillModelAdmin(admin.ModelAdmin):
    pass


@admin.register(EducationModel)
class EducationModelAdmin(admin.ModelAdmin):
    list_display = ('title_education', 'text', 'id')
    list_filter = ('created_at', 'updated_at')
    
    
@admin.register(ExpreiencModel)
class ExpreiencModelAdmin(admin.ModelAdmin):
    list_display = ('title_expreienc', 'text', 'idtitle_education', 'to_date_exprence')
    

@admin.register(AboutMeModel)
class AboutMeModelAdmin(admin.ModelAdmin):
    list_display = ('title_expreienc', 'text', 'id')
    
    
@admin.register(ContactUsModel)
class ContactUsModelAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'moile_phone', 'id')
    
    
@admin.register(ContentInfoModel)
class ContentInfoModelAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'moile_phone', 'id')