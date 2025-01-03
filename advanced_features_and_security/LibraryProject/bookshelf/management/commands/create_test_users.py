from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group

class Command(BaseCommand):
    help = "Create test users and assign them to groups"

    def handle(self, *args, **kwargs):
        # Create Groups if they don't exist
        editors_group, _ = Group.objects.get_or_create(name='Editors')
        viewers_group, _ = Group.objects.get_or_create(name='Viewers')
        admins_group, _ = Group.objects.get_or_create(name='Admins')

        # Create Users
        editor_user, created = User.objects.get_or_create(username='editor_user')
        if created:
            editor_user.set_password('password123')
            editor_user.groups.add(editors_group)
            editor_user.save()

        viewer_user, created = User.objects.get_or_create(username='viewer_user')
        if created:
            viewer_user.set_password('password123')
            viewer_user.groups.add(viewers_group)
            viewer_user.save()

        admin_user, created = User.objects.get_or_create(username='admin_user')
        if created:
            admin_user.set_password('password123')
            admin_user.groups.add(admins_group)
            admin_user.save()

        self.stdout.write(self.style.SUCCESS("Test users created and assigned to groups."))