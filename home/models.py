from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from core.models import CreateModel, UpdateModel



class NvbarModel(CreateModel, UpdateModel):
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
        ordering = ('-navbar_name',)
        
        
class HeaderConetent(CreateModel, UpdateModel):
    text = models.CharField(_('text'), max_length=50)
    
    def __str__(self) -> str:
        return self.text
    
    class Meta:
        verbose_name = _('header_conetent')
        verbose_name_plural = _('header_conetents')
        db_table = 'header_conetent'
        
        
class HeaderConetentSciol(CreateModel, UpdateModel):
    sciol_name = models.CharField(_('sciol name'), max_length=20)
    sciol_url = models.URLField(_('sciol url'))    
    
    def __str__(self) -> str:
        return self.sciol_name
    
    class Meta:
        verbose_name = _('header_conetent sciol')
        verbose_name_plural = _('header conetents sciol')
        db_table = 'sciol'
        
        
class AboutMeModels(CreateModel, UpdateModel):
    image = models.ImageField()
    full_name = models.CharField(_('full_name'), max_length=50)
    explain = models.TextField(_('explain'), max_length=255)
    
    def __str__(self) -> str:
        return self.full_name
    
    class Meta:
        verbose_name = _('about_me')
        verbose_name_plural = _('abouts_me')
        db_table = 'about_me'
        
        
class SkillModel(CreateModel, UpdateModel):
    skill_name = models.CharField(_('skill_name'), max_length=50)
    image = models.ImageField(_('image'), blank=True)
    
    def __str__(self) -> str:
        return self.skill_name
    
    class Meta:
        verbose_name = _('skill_mode')
        verbose_name_plural = _('skill_modes')
        db_table = 'skill'
        
        
class EducationModel(CreateModel, UpdateModel):
    title_education = models.CharField(_('education'), max_length=100)
    text = models.CharField(_('text'), max_length=255)
    
    def __str__(self) -> str:
        return self.title_education
    
    class Meta:
        verbose_name = _('education')
        verbose_name_plural = _('educations')
        db_table = 'educations'
        
        
class ExpreiencModel(CreateModel, UpdateModel):
    exprense_title = models.CharField(_('exprience'), max_length=50)
    explain_exprence = models.CharField(_('explain'), max_length=255)
    at_date_exprence = models.DateField(_('at date'), default=timezone.now)
    to_date_exprence = models.DateField(_('to date'), default=timezone.now)
    
    
    def __str__(self) -> str:
        return self.exprence_title
    
    class Meta:
        verbose_name = _('exprence')
        verbose_name_plural = _('exprences')
        db_table = 'exprences'
        
        
        
class AboutMeModel(CreateModel, UpdateModel):
    full_name = models.CharField(_('full_name'), max_length=100)
    image = models.ImageField(blank=True)
    explain_to_me = models.TextField(_('explain to me'))
    
    def __str__(self) -> str:
        return self.full_name
    
    class Meta:
        verbose_name = _('about_me')
        verbose_name_plural = _('abouts_me')
        db_table = 'about_mee'
        
        
class ContactUsModel(CreateModel, UpdateModel):
    full_name = models.CharField(_('full_name'), max_length=100)
    email = models.CharField(_('email'), max_length=100, unique=True)
    mobile_phone = models.CharField(_('mobile_phone'), max_length=11, unique=True, blank=True)
    body = models.TextField()
    
    def __str__(self) -> str:
        return f'{self.full_name} {self.email}'
    
    class Meta:
        verbose_name = _('content us')
        verbose_name_plural = _('contents_us')
        db_table = 'contents'
        

class ContentInfoModel(models.Model):
    full_name = models.CharField(_('full_name'), max_length=100, null=True, blank=True)
    mobile_phone = models.CharField(_('mobile_phone'), max_length=11, blank=True, unique=True, null=True)
    email = models.CharField(_('email'), max_length=100, unique=True, blank=True, null=True)
    explane_me = models.TextField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.full_name
    
    class Meta:
        verbose_name = _('contact_info')
        verbose_name_plural = _('contacts_info')
        db_table = 'contact_info'