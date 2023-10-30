from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from core.models import CreateModel
from django_jalali.db import models as jmodels
from accounts.models import User


# navbar
class NvbarModel(CreateModel):
    navbar_name = models.CharField(_('Name'), max_length=20)

    class NavbarChoose(models.TextChoices):
        publish = 'pb', _('Publish'),
        reject = 'rj', _('Reject'),
    navbar_status = models.CharField(_('Status'), max_length=2, choices=NavbarChoose.choices,
                                     default=NavbarChoose.publish)
    def __str__(self) -> str:
        return self.navbar_name
    
    class Meta:
        verbose_name = _('navbar')
        verbose_name_plural = _('navbars')
        db_table = 'navbar'
        # ordering = ('-navbar_name',)
    
class HeaderConetent(CreateModel):
    text = models.CharField(_('tell me about you'), max_length=50)
    image = models.ImageField(blank=True)
    
    def __str__(self) -> str:
        return self.text
    
    class Meta:
        verbose_name = _('header conetent')
        verbose_name_plural = _('header conetents')
        db_table = 'header_conetent'
        
class HeaderConetentSciol(CreateModel):
    sciol_name = models.CharField(_('sciol name'), max_length=20)
    sciol_url = models.CharField(_('sciol url'), max_length=255)    
    
    def __str__(self) -> str:
        return self.sciol_name
    
    class Meta:
        verbose_name = _('header_conetent sciol')
        verbose_name_plural = _('header conetents sciol')
        db_table = 'sciol'
        
class MobileCode(models.Model):
    mobile_code = models.CharField(_('mobile code'), max_length=5)
    
    def __str__(self) -> str:
        return self.mobile_code
    
    class Meta:
        db_tablespace = 'mobile_code'
        verbose_name = _('mobile code')
        verbose_name_plural = _('mobile code')       

class AboutMeModels(CreateModel):
    image = models.ImageField(blank=True)
    full_name = models.CharField(_('full_name'), max_length=50)
    explain = models.TextField(_('explain'), max_length=255)
    email = models.EmailField(null=True, blank=True)
    mobile_phone = models.CharField(_('mobile phone'), max_length=11, unique=True, null=True, blank=True)
    mobile_code = models.ForeignKey(MobileCode, on_delete=models.PROTECT, verbose_name='code')
    job = models.CharField(_('job'), max_length=50, null=True, blank=True)
    
        
    def __str__(self) -> str:
        return self.full_name
    
    class Meta:
        verbose_name = _('about me')
        verbose_name_plural = _('abouts me')
        db_table = 'about_me'
        
        
class SkillModel(CreateModel):
    skill_name = models.CharField(_('skill_name'), max_length=50)
    image = models.ImageField(_('image'), blank=True)
    
    def __str__(self) -> str:
        return self.skill_name
    
    class Meta:
        verbose_name = _('skill')
        verbose_name_plural = _('skills')
        db_table = 'skill'
        
        
class EducationModel(CreateModel):
    title_education = models.CharField(_('education name'), max_length=100)
    text = models.TextField(_('sayTell me a little bit about it education. '), max_length=255)
    at_education = jmodels.jDateField(_('at time'))
    to_education = jmodels.jDateField(_('to time'), blank=True, null=True)
    busy = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.title_education
            
    class Meta:
        verbose_name = _('education')
        verbose_name_plural = _('educations')
        db_table = 'educations'
        
        
class ExpreiencModel(CreateModel):
    exprense_title = models.CharField(_('exprience title'), max_length=50)
    explain_exprence = models.TextField(_('explain to own project'), max_length=300)
    link_project = models.URLField(_('link to project'), blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    at_date_exprence = jmodels.jDateField(_('at date'), default=timezone.now)
    to_date_exprence = jmodels.jDateField(_('to date'), default=timezone.now)
    
    class StatusProject(models.TextChoices):
        start = 's', _('start'),
        doing = 'd', _('doing'),
        complate = 'c', _('complate'),
    status_project = models.CharField(_('status'),
                                      max_length=1,
                                      default=StatusProject.complate,
                                      choices=StatusProject.choices)
    def __str__(self) -> str:
        return self.exprense_title
    
    class Meta:
        verbose_name = _('exprence')
        verbose_name_plural = _('exprences')
        db_table = 'exprences'
        

class ExprienceProject(CreateModel):
    title = models.CharField(_('title project'), max_length=50)
    project_url = models.URLField(_('project url'))
    image = models.ImageField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = _('project')
        verbose_name_plural = _('projects')
        db_table = 'projects'
            
class ContactUsModel(CreateModel):
    full_name = models.CharField(_('full_name'), max_length=100)
    email = models.CharField(_('email'), max_length=100, unique=True)
    mobile_phone = models.CharField(_('mobile_phone'), max_length=11, unique=True, blank=True)
    body = models.TextField()
    
    def __str__(self) -> str:
        return f'{self.full_name} {self.email}'
    
    class Meta:
        verbose_name = _('content us')
        verbose_name_plural = _('contents us')
        db_table = 'contents'