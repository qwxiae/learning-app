from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    help = "Test data for all apps in project"

    def handle(self, *args, **kwargs):
        call_command("seed_roles")
        call_command("seed_categories")
        call_command("seed_courses")
        call_command("seed_lessons")
