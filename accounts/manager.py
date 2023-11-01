from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError


class UsersManager(BaseUserManager):
    def create_user(self, email, full_name, mobile_phone, password=None):
        if not email:
            raise ValidationError('Email must be set')
        
        if not mobile_phone:
            raise ValidationError('Mobile phone must be set')
        
        if not full_name:
            raise ValidationError('Full name must be set')
        
        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
            mobile_phone=mobile_phone,
        )
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, mobile_phone, full_name, password=None):
        user = self.create_user(email=email,
        mobile_phone=mobile_phone, 
        full_name=full_name,
        password=password)
        
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user