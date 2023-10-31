from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from core.models import CreateModel
from django_jalali.db import models as jmodels
from accounts.models import User


class SciolModel(CreateModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='sciol')
    sciol_name = models.CharField(_('sciol name'), max_length=20)
    sciol_url = models.CharField(_('sciol url'), max_length=255)
     
    def __str__(self) -> str:
        return self.sciol_name
    
    class Meta:
        verbose_name = _('sciol')
        verbose_name_plural = _('sciols')
        db_table = 'sciol'
        
        
class AboutMeModels(CreateModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='about')
    image = models.ImageField(blank=True, help_text='Post a picture of yourself')
    explain = models.TextField(_('explain'), max_length=500,
        help_text='Write something about yourself')
    job = models.CharField(_('job'), max_length=50, null=True, blank=True,
        help_text='What is your current job?')
    
        
    def __str__(self) -> str:
        return self.full_name
    
    class Meta:
        verbose_name = _('about me')
        verbose_name_plural = _('abouts me')
        db_table = 'about_me'
        
        
class SkillModel(CreateModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='skill')
    skill_name = models.CharField(_('skill_name'), max_length=50)
    image = models.ImageField(_('image'), blank=True)
    
    def __str__(self) -> str:
        return self.skill_name
    
    class Meta:
        verbose_name = _('skill')
        verbose_name_plural = _('skills')
        db_table = 'skill'
        
        
class EducationModel(CreateModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='education')
    title_education = models.CharField(_('education name'), max_length=100)
    explain_education = models.TextField(_('explain education'), max_length=500,
        help_text='Describe where you were trained and educated')
    at_education = jmodels.jDateField(_('at time'))
    to_education = jmodels.jDateField(_('to time'), blank=True, null=True)
    status_education = models.BooleanField(_('status education'), default=False)
    
    def __str__(self) -> str:
        return self.title_education
            
    class Meta:
        verbose_name = _('education')
        verbose_name_plural = _('educations')
        db_table = 'educations'
        
        
class ExpreienceWorkModel(CreateModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='experience')
    exprience_title = models.CharField(_('experience title'), max_length=50,
                                      help_text='')
    explain_exprence = models.TextField(_('explain to own experience'), max_length=500,
        help_text='Tell me something about your work experience.')
    link_company = models.URLField(_('link to company'), blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    at_date_exprence = jmodels.jDateField(_('at date'), default=timezone.now)
    to_date_exprence = jmodels.jDateField(_('to date'), default=timezone.now)
    
    
    def __str__(self) -> str:
        return self.exprense_title
    
    class Meta:
        verbose_name = _('exprence')
        verbose_name_plural = _('exprences')
        db_table = 'exprences'
        

class ProjectModel(CreateModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='project')
    title = models.CharField(_('title project'), max_length=50)
    project_url = models.URLField(_('project url'))
    image = models.ImageField(blank=True, null=True)
    
    
    class StatusProject(models.TextChoices):
        start = 's', _('start'),
        doing = 'd', _('doing'),
        complate = 'c', _('complate'),
    status_project = models.CharField(_('status'),
                                      max_length=1,
                                      default=StatusProject.complate,
                                      choices=StatusProject.choices)
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