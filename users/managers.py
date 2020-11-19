from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
  
  def create_user(self, email, password, phone, **kwargs):
    if not email:
      raise ValueError('Enter email')
    email = self.normalize_email(email) 
    user = self.model(email=email, phone=phone, **kwargs)
    user.set_password(password)
    user.save()
    return user

  def create_superuser(self, email, password, phone, **kwargs):
    
    user = self.create_user(email=email, password=password, phone=phone, **kwargs)
    user.is_superuser = True
    user.is_staff = True
    user.is_active = True
    user.save()
    return user
