from datetime import timedelta
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
import markdown2


class Event(models.Model):
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField('start time')
    duration = models.DurationField('duration', default=timedelta(hours=1))
    pub_date = models.DateTimeField('date published')
    location = models.CharField(max_length=200)
    details_markdown = models.TextField('markdown details')
    details_html = models.TextField('html details', editable=False)

    def clean(self, *args, **kwargs):
        """
        Override default clean() function to add additional model constrains.
        These will be checked at every full_clean() call, which is called at
        every save() call. Setup is similar to
        https://stackoverflow.com/q/12945339/2680824
        """
        if self.duration < timedelta(hours=0):
            raise ValidationError(_('Event duration must be positive'))
        super(Event, self).clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        """
        Overide save() function to create details_html from details_markdown
        and run full_clean(), which also runs clean()
        """
        self.details_html = markdown2.markdown(self.details_markdown)
        self.full_clean()
        return super(Event, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Rsvp(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rsvp_date = models.DateTimeField('rsvp date', default=timezone.now)

    class Meta:
        unique_together = (('event', 'user'),)

    def __str__(self):
        return '{}, {}'.format(self.event, self.user)


class Signin(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    signin_date = models.DateTimeField('signin date')

    class Meta:
        unique_together = (('event', 'user'),)

    def __str__(self):
        return '{}, {}'.format(self.event, self.user)
