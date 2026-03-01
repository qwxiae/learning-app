from django.core.management import BaseCommand, call_command
from apps.users.models import Role, User, UserRole

class Command(BaseCommand):
    help = "Create default users"

    def handle(self, *args, **kwargs):
        call_command("seed_roles")



        instructor_role = Role.objects.get(name="instructor")
        user_data = [
            ("test@test.com", "hr2htBeTryYQ", True),
            ("janedoe@test.com", "43uqjK3vTyAq", True),
            ("johndoe@test.com", "HAz6ghNn97u4", False),
            ("annabelle@test.com", "PXQENDSEDTkr", False),
            ("nadinerami@test.com", "NWyhpcVtF6rp", False)
        ]

        for email, password, is_instructor in user_data:
            user, create = User.objects.get_or_create(
                email=email,
                defaults={"password": password}
            )

            if create and is_instructor:
                user_role = UserRole.objects.create(user=user, role=instructor_role)
                user_role.save()
                self.stdout.write(f"Created user: {email}")
            else:
                self.stdout.write(f"User '{email}' already exists")
        
        self.stdout.write(self.style.SUCCESS("Done creating users."))
