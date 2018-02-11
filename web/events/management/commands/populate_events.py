from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.core.files import File
from django.core.management.base import BaseCommand
from django.utils import timezone
from os.path import abspath
from os.path import dirname
from os.path import join
import pytz

from events.models import Event
from events.models import event_directory_path

EST = pytz.timezone('US/Eastern')
EVENT_FILES_PATH = join(dirname(abspath(__file__)), 'event_files')


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
        # based on suggestion in comments of
        # https://stackoverflow.com/a/3090342/2680824
        existing_info_session_1 = (
            Event.objects.filter(title=info_session_1.title).first()
        )
        if existing_info_session_1 is None:
            print("Adding Spring 2017 Info Session")
            info_session_1.save()
        else:
            print("Spring 2017 Info Session already added.")
            info_session_1 = existing_info_session_1
        image_path = join(
            EVENT_FILES_PATH, '2017-01-26-info-session', 'image.png'
        )
        # Modified from https://stackoverflow.com/a/1993971/2680824
        with open(image_path, 'rb') as f:
            image_file = File(f)
            new_path = event_directory_path(info_session_1, image_path)
            info_session_1.image.save(new_path, image_file)
        print("Uploading image for Spring 2017 Info Session")
        info_session_1.save()

    def handle(self, *args, **options):
        self._create_events()
