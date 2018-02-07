from django.db import models
from django.contrib.auth.models import User

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
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    full_name = models.CharField(max_length=100, null=True, blank=False)
    schools = models.ManyToManyField(School, blank=False)
    degrees = models.ManyToManyField(Degree, blank=False)
    program = models.CharField(max_length=100, null=True, blank=False)
    grad_year = models.IntegerField(null=True, blank=False)
    resume = models.FileField(
        upload_to=user_directory_path, null=True, blank=True
    )
    viewable = models.BooleanField(default=False)

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

    class Meta:
        ordering = ('user',)
