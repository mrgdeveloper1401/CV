from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import CreateModel
from django_jalali.db import models as jmodels
from accounts.models import User
from jdatetime import date


class SciolModel(CreateModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='sciol')
    sciol_name = models.CharField(_('sciol name'), max_length=20, blank=True)
    sciol_url = models.CharField(_('sciol url'), max_length=255, blank=True)
     
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
        help_text='Write something about yourself', blank=True)
    job = models.CharField(_('job'), max_length=50, null=True, blank=True,
        help_text='What is your current job?')
    class MeritalStatus(models.TextChoices):
        single = 's', _('single'),
        married = 'm', _('married'),
    marital_status = models.CharField(_('marital status'), max_length=1,
                                      choices=MeritalStatus.choices,
                                      default=MeritalStatus.single,
                                      blank=True)
    
    class Gender(models.TextChoices):
        male = 'm', _('male'),
        female = 'f', _('female'),
        
    gender_choose = models.CharField(_('gender'), max_length=1,
                                     default=Gender.male,
                                     choices=Gender.choices,
                                     blank=True)
    address = models.TextField(blank=True, max_length=500)
    birth_day = jmodels.jDateField(_('birth day'), blank=True)
    
    @property
    def age(self):
        today = date.today()
        age = today.year - self.birth_day.year - ((today.month, today.day) < (self.birth_day.month, self.birth_day.day))
        return age
    
    def __str__(self) -> str:
        return self.user.email
    
    class Meta:
        verbose_name = _('about me')
        verbose_name_plural = _('abouts me')
        db_table = 'about_me'
        
        
class SkillModel(CreateModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='skill')
    skill_name = models.CharField(_('skill_name'), max_length=50, blank=True)

    
    def __str__(self) -> str:
        return self.skill_name
    
    class Meta:
        verbose_name = _('skill')
        verbose_name_plural = _('skills')
        db_table = 'skill'
        
        
class EducationModel(CreateModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='education')
    fields_of_study = models.CharField(_('field of study'), max_length=100, blank=True)
    university = models.CharField(_('university'), max_length=100, blank=True)
    score = models.DecimalField(_('score'), max_digits=4, decimal_places=2, blank=True)
    explain_education = models.TextField(_('explain education'), max_length=500,
        help_text='Describe where you were trained and educated', blank=True)
    at_education = jmodels.jDateField(_('at time'), blank=True)
    to_education = jmodels.jDateField(_('to time'), blank=True, null=True)
    status_education = models.BooleanField(_('studying'), default=False, blank=True)
    
    def __str__(self) -> str:
        return self.user.email
            
    class Meta:
        verbose_name = _('education')
        verbose_name_plural = _('educations')
        db_table = 'educations'
        
        
class ExpreienceWorkModel(CreateModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='experience')
    job_title = models.CharField(_('job title'), max_length=50, blank=True)
    organization_name = models.CharField(_('organization name'), max_length=50, blank=True)
    explain_your_duties = models.TextField(_('explain your duties'), max_length=500,
        help_text='Tell me something about your work experience.', blank=True)
    link_company = models.URLField(_('link to company'), blank=True, null=True)
    at_date_exprence = jmodels.jDateField(_('at date'), blank=True)
    to_date_exprence = jmodels.jDateField(_('to date'), blank=True)
    
    class StatusWorkOraginaztion(models.TextChoices):
        busy = "b", _("I am busy now"),
        done = 'd', _("I dont work here")
        found = 'f', _('looking for work')
    status_work = models.CharField(_('status work'), max_length=1,
                                   default=StatusWorkOraginaztion.done,
                                   choices=StatusWorkOraginaztion.choices)    
    
    
    def __str__(self) -> str:
        return self.user.email
    
    class Meta:
        verbose_name = _('exprence')
        verbose_name_plural = _('exprences')
        db_table = 'exprences'
        

class ProjectModel(CreateModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='project')
    title = models.CharField(_('title project'), max_length=50, blank=True)
    project_url = models.URLField(_('project url'), blank=True)
    image = models.ImageField(blank=True, null=True)
    from_date = jmodels.jDateField(_('from date'), blank=True)
    up_to_date = jmodels.jDateField(_('up to date'), blank=True)
    
    
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
    awards_name = models.CharField(_('awards_name'), max_length=50, blank=True)
    explain_awards = models.TextField(_('explain awards'), max_length=500, blank=True)
    year_awards = jmodels.jDateField(_('year'), blank=True)
    
    class Meta:
        verbose_name = _('awards')
        verbose_name_plural = _('awards')
        db_table = 'awards'
        
        
class AuthoreModel(CreateModel):
    auther = models.CharField(_('auther'), max_length=100, blank=True)
    
    def __str__(self) -> str:
        return self.auther
    class Meta:
        verbose_name = _('authore')
        verbose_name_plural = _('authore')
        db_table = 'authore'
        
class BoookArticleModel(CreateModel):
    title = models.CharField(_('title'), max_length=50, blank=True)
    publisher = models.ManyToManyField(AuthoreModel, related_name='authors')
    year = jmodels.jDateField(_('year'), blank=True)

    def __str__(self) -> str:
        return self.title    
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