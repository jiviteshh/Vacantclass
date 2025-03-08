from django.core.management.base import BaseCommand
from datetime import timedelta
from django.utils.timezone import now
from finder.models import Room  # Replace 'finder' with your actual app name

class Command(BaseCommand):
    help = 'Deletes room data older than 12 hours'

    def handle(self, *args, **kwargs):
        expired_time = now() - timedelta(hours=12)  # Ensure this is in UTC

        # Debugging: Print the times for verification
        print(f"Expired Time (UTC): {expired_time}")

        # Check oldest room in database
        sample_room = Room.objects.order_by('uploaded_on').first()
        if sample_room:
            print(f"Oldest Room Uploaded Time (UTC): {sample_room.uploaded_on}")

        # Delete expired rooms
        deleted_count, _ = Room.objects.filter(uploaded_on__lt=expired_time).delete()
        self.stdout.write(self.style.SUCCESS(f'Successfully deleted {deleted_count} expired room(s)'))
