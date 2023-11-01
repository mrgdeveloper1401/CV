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
    class MeritalStatus(models.TextChoices):
        single = 's', _('single'),
        married = 'm', _('married'),
    marital_status = models.CharField(_('marital status'), max_length=1,
                                      choices=MeritalStatus.choices,
                                      default=MeritalStatus.single)
    
    class Gender(models.TextChoices):
        male = 'm', _('male'),
        female = 'f', _('female'),
        
    gender_choose = models.CharField(_('gender'), max_length=1,
                                     default=Gender.male,
                                     choices=Gender.choices)
    address = models.TextField()
    birth_day = jmodels.jDateField(_('birth day'), default=timezone.now())
    def __str__(self) -> str:
        return self.user.email
    
    class Meta:
        verbose_name = _('about me')
        verbose_name_plural = _('abouts me')
        db_table = 'about_me'
        
        
class SkillModel(CreateModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='skill')
    skill_name = models.CharField(_('skill_name'), max_length=50)

    
    def __str__(self) -> str:
        return self.skill_name
    
    class Meta:
        verbose_name = _('skill')
        verbose_name_plural = _('skills')
        db_table = 'skill'
        
        
class EducationModel(CreateModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='education')
    fields_of_study = models.CharField(_('field of study'), max_length=100)
    university = models.CharField(_('university'), max_length=100)
    score = models.DecimalField(_('score'), max_digits=2, decimal_places=2)
    explain_education = models.TextField(_('explain education'), max_length=500,
        help_text='Describe where you were trained and educated')
    at_education = jmodels.jDateField(_('at time'))
    to_education = jmodels.jDateField(_('to time'), blank=True, null=True)
    status_education = models.BooleanField(_('studying'), default=False)
    
    def __str__(self) -> str:
        return self.title_education
            
    class Meta:
        verbose_name = _('education')
        verbose_name_plural = _('educations')
        db_table = 'educations'
        
        
class ExpreienceWorkModel(CreateModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='experience')
    job_title = models.CharField(_('job title'), max_length=50)
    organization_name = models.CharField(_('organization name'), max_length=50)
    explain_your_duties = models.TextField(_('explain your duties'), max_length=500,
        help_text='Tell me something about your work experience.')
    link_company = models.URLField(_('link to company'), blank=True, null=True)
    at_date_exprence = jmodels.jDateField(_('at date'), default=timezone.now)
    to_date_exprence = jmodels.jDateField(_('to date'), default=timezone.now)
    status_work = models.BooleanField(_('status work'), default=False)
    
    
    def __str__(self) -> str:
        return self.user.email
    
    class Meta:
        verbose_name = _('exprence')
        verbose_name_plural = _('exprences')
        db_table = 'exprences'
        

class ProjectModel(CreateModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='project')
    title = models.CharField(_('title project'), max_length=50)
    project_url = models.URLField(_('project url'))
    image = models.ImageField(blank=True, null=True)
    from_date = jmodels.jDateField(_('from date'), default=timezone.now())
    up_to_date = jmodels.jDateField(_('up to date'), default=timezone.now())
    
    
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
            
            
class AwardsModel(CreateModel):
    awards_name = models.CharField(_('awards_name'), max_length=50)
    explain_awards = models.TextField(_('explain awards'), max_length=500)
    year_awards = jmodels.jDateField(_('year'), default=timezone.now())
    
    class Meta:
        verbose_name = _('awards')
        verbose_name_plural = _('awards')
        db_table = 'awards'
        
        
class BoookArticleModel(CreateModel):
    title = models.CharField(_('title'), max_length=50)
    publisher = models.ManyToManyField('self')
    year = jmodels.jDateField(_('year'), blank=True, default=timezone.now())
    
    class Meta:
        verbose_name = _('book artiles')
        verbose_name_plural = _('book artiles')
        db_tablespace = 'book_article'
        
    
    
class ContactUsModel(CreateModel):
    full_name = models.CharField(_('full_name'), max_length=100)
    email = models.CharField(_('email'), max_length=100)
    mobile_phone = models.CharField(_('mobile_phone'), max_length=11, blank=True)
    body = models.TextField()
    
    def __str__(self) -> str:
        return f'{self.full_name} {self.email}'
    
    class Meta:
        verbose_name = _('content us')
        verbose_name_plural = _('contents us')
        db_table = 'contents'