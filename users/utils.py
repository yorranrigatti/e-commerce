from django.contrib.auth.models import BaseUserManager


class CustomUser(BaseUserManager):
    
    def _create_user(self, email, password, first_name, last_name, birth_date, is_superuser, is_staff, **extra_fields):
        user = self.model(
            email = email,
            first_name   = first_name,
            last_name    = last_name,
            birth_date   = birth_date,
            is_active    = True,
            is_superuser = is_superuser,
            is_staff     = is_staff,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, password, first_name, last_name, birth_date, **extra_fields):
        return self._create_user(email, password, first_name, last_name, birth_date, False, False, **extra_fields)

    def create_staff(self, email, password, first_name, last_name, birth_date, **extra_fields):
        return self._create_user(email, password, first_name, last_name, birth_date, False, True, **extra_fields)
    
    def create_superuser(self, email, password, first_name, last_name, birth_date, **extra_fields):
        return self._create_user(email, password, first_name, last_name, birth_date, True, True, **extra_fields)
