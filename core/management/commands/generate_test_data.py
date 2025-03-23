import random
from django.core.management.base import BaseCommand
from django.utils.timezone import now, timedelta
from django.contrib.auth import get_user_model
from core.models import Kudos, Organization, OrganizationMembership

User = get_user_model()  # Use the default or custom user model

# Sample messages for kudos
KUDOS_MESSAGES = [
    "Great teamwork on the project!",
    "Thanks for helping me out last week!",
    "Awesome presentation in the meeting!",
    "Really appreciate your effort on this task!",
    "You're always bringing positive energy to the team!",
    "Fantastic job handling that issue!",
    "Your leadership has been inspiring!",
]

class Command(BaseCommand):
    help = "Generates test data for Kudos system"

    def handle(self, *args, **kwargs):
        # Create organizations
        org1, _ = Organization.objects.get_or_create(name="Org Alpha")
        org2, _ = Organization.objects.get_or_create(name="Org Beta")

        # Create users and their organization memberships
        users = []
        for i in range(1, 6):  # Create 5 users per organization

            user_alpha = User.objects.create(username=f"user{i}_alpha")
            user_beta = User.objects.create(username=f"user{i}_beta")
            import pdb; pdb.set_trace()
            OrganizationMembership.objects.create(user=user_alpha, organization=org1)
            OrganizationMembership.objects.create(user=user_beta, organization=org2)

            users.extend([user_alpha, user_beta])

        # Create kudos
        for user in users:
            # Get the user's organization
            membership = OrganizationMembership.objects.filter(user=user).first()
            if not membership:
                continue  # Skip if the user has no organization

            same_org_users = OrganizationMembership.objects.filter(organization=membership.organization).exclude(user=user)
            receivers = random.sample(list(same_org_users), min(3, same_org_users.count()))  # Pick up to 3 random users

            for receiver_membership in receivers:
                message = random.choice(KUDOS_MESSAGES)  # Select a random message
                Kudos.objects.create(
                    giver=user,
                    receiver=receiver_membership.user,
                    message=message,
                    timestamp=now() - timedelta(days=random.randint(0, 6))
                )

        self.stdout.write(self.style.SUCCESS("Test data generated successfully!"))
