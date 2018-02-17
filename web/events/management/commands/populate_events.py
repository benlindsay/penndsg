from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.core.files import File
from django.core.management.base import BaseCommand
from django.utils import timezone
from glob import glob
from os.path import abspath
from os.path import basename
from os.path import dirname
from os.path import join
import pytz
import yaml

from events.models import Event
from events.models import event_directory_path

EST = pytz.timezone('US/Eastern')
EVENT_FILES_PATH = join(dirname(abspath(__file__)), 'event_files')


class Command(BaseCommand):
    args = ''
    help = 'Adds previous events'

    def _create_event(self, event_dir):
        content_file = join(event_dir, 'content.md')
        event_slug = basename(event_dir)
        year, month, day = map(int, event_slug.split('-')[:3])
        with open(content_file, 'r') as f:
            content = f.read()
        # yaml header is wrappedn in '---' in content.md files
        _, yaml_content, md_content = content.split('---')
        data_dict = yaml.safe_load(yaml_content)
        md_content = md_content.strip()
        # https://stackoverflow.com/a/1759485/2680824
        time = datetime.strptime(data_dict['start_time'], '%I:%M %p')
        # https://stackoverflow.com/a/12352624/2680824
        duration_time = datetime.strptime(data_dict['duration'], '%H:%M')
        duration = timedelta(
            hours=duration_time.hour, minutes=duration_time.minute
        )
        # based on suggestion in comments of
        # https://stackoverflow.com/a/3090342/2680824
        event = Event.objects.filter(title=data_dict['title']).first()
        if event is None:
            # create event if it doesn't exist yet
            print('Creating {} event'.format(data_dict['title']))
            event = Event(
                title=data_dict['title'],
                start_time=datetime(
                    year=year,
                    month=month,
                    day=day,
                    hour=time.hour,
                    minute=time.minute,
                    tzinfo=EST,
                ),
                duration=duration,
                pub_date=timezone.now(),
                location=data_dict['location'],
                details_markdown=md_content,
            )
            event.save()
        else:
            print("{} already exists.".format(data_dict['title']))
        # Find event image (image.<extension>) in event folder
        image_glob = glob(join(event_dir, 'image.*'))
        if len(image_glob) == 0:
            print("No images found in {}".format(event_dir))
        elif len(image_glob) > 1:
            msg = "Multiple images found in {}. Delete unwanted ones."
            print(msg.format(event_dir))
        else:
            image_path = image_glob[0]
            # Modified from https://stackoverflow.com/a/1993971/2680824
            with open(image_path, 'rb') as f:
                image_file = File(f)
                new_path = event_directory_path(event, image_path)
                event.image.save(new_path, image_file)
            print("Uploading image for {}".format(data_dict['title']))
            event.save()

    def handle(self, *args, **options):
        event_dirs = sorted(glob(join(EVENT_FILES_PATH, '*')))
        for d in event_dirs:
            self._create_event(d)
