from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, User

class Command(BaseCommand):
    help = "Create Admin group and add an admin user (if not already created)"

    def handle(self, *args, **kwargs):
        # Create the Admin group if it doesn't exist
        admin_group, created = Group.objects.get_or_create(name="Admin")
        if created:
            self.stdout.write(self.style.SUCCESS("Admin group created successfully"))
        else:
            self.stdout.write(self.style.WARNING("Admin group already exists"))

        # Check if the user already exists before creating
        username = "admin_user"
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, password="secure_pass123")
            user.groups.add(admin_group)
            self.stdout.write(self.style.SUCCESS(f"User '{username}' created and added to Admin group"))
        else:
            self.stdout.write(self.style.WARNING(f"User '{username}' already exists, skipping creation."))
