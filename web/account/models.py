from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _

# References for creating custom user model. Do this!
# https://medium.com/@ramykhuffash/django-authentication-with-just-an-email-and-password-no-username-required-33e47976b517
# https://docs.djangoproject.com/en/2.0/topics/auth/customizing/#substituting-a-custom-user-model


# https://www.fomfus.com/articles/
# how-to-use-email-as-username-for-django-authentication-removing-the-username
class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


# https://www.fomfus.com/articles/how-to-use-email-as-username-for-django-authentication-removing-the-username
class User(AbstractUser):
    """User model"""

    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


class School(models.Model):
    name = models.CharField(max_length=50)
    abbrev = models.CharField(max_length=20)

    def __str__(self):
        return self.abbrev


class Degree(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/resume.<filename_ext>
    if filename.count('.') > 0:
        ext = filename.split('.')[-1]
    else:
        raise ValueError('filename {} has no extension!'.format(filename))
    new_filename = '.'.join(['resume', ext])
    try:
        user_id = instance.user.id
    except:
        raise ValueError('No profile found ')
    return 'user_{0}/{1}'.format(instance.user.id, new_filename)


class Profile(models.Model):
    """Information connected to each User

    A signal in .signals ensures that a blank Profile object is created for
    each new User after the first save of that User
    """
    user = models.OneToOneField(
        User, primary_key=True, on_delete=models.CASCADE
    )
    email_confirmed = models.BooleanField(default=False)
    schools = models.ManyToManyField(School, blank=False)
    degrees = models.ManyToManyField(Degree, blank=False)
    program = models.CharField(max_length=100, null=True, blank=False)
    grad_year = models.IntegerField(null=True, blank=False)
    resume = models.FileField(
        upload_to=user_directory_path, null=True, blank=True
    )
    searchable = models.BooleanField(default=False)

    def full_name(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)

    # https://stackoverflow.com/a/3411411/2680824
    def email(self):
        return self.user.email

    def resume_basename(self):
        return os.path.basename(self.resume.name)

    def __str__(self):
        try:
            if self.full_name is not None:
                return "{}'s profile".format(self.full_name)
            else:
                return "{}'s profile".format(self.user.username)
        except:
            return "{}'s profile".format(self.user.username)
