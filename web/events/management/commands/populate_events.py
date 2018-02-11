from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils import timezone
import pytz

from events.models import Event

EST = pytz.timezone('US/Eastern')

class Command(BaseCommand):
    args = ''
    help = 'Adds previous events'

    def _create_events(self):
        info_session_1 = Event(
            title="Spring 2017 Info Session",
            start_time=datetime(
                year=2017, month=1, day=26, hour=18, tzinfo=EST
            ),
            duration=timedelta(hours=1),
            pub_date=timezone.now(),
            location="Berger Auditorium, Skirkanich Hall",
            details_markdown="""
If you're interested in data science and/or pizza, bring your appetite to the
Penn Data Science Group info session! We'll talk about our plans for the
semester and help you find a team to work on a data science project with. RSVP
here.

The slides presented at this event can be downloaded as a PDF or PowerPoint
file.

- [PowerPoint Slides](http://penndsg.com/slides/2017-01-26-info-session-slides.pptx)
- [PDF File](http://penndsg.com/slides/2017-01-26-info-session-slides.pdf)
            """
        )
        if not Event.objects.filter(title=info_session_1.title).exists():
            info_session_1.save()

    def handle(self, *args, **options):
        self._create_events()
