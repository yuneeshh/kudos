from django.utils.timezone import now
from datetime import timedelta
from django.core.exceptions import ValidationError
from core.models import Kudos


class KudoService:

    @staticmethod
    def kudos_given_this_week(user):
        """Returns the count of kudos given by the user in the current week."""
        start_of_week = now().date() - timedelta(days=now().weekday())  # Monday of this week
        return Kudos.objects.filter(giver=user, timestamp__date__gte=start_of_week).count()

    @staticmethod
    def can_give_kudos(user):
        """Checks if the user has remaining kudos to give this week."""
        return KudoService.kudos_given_this_week(user) < 3

    @staticmethod
    def give_kudos(giver, receiver, message):
        """Handles giving kudos while enforcing constraints."""
        if not KudoService.can_give_kudos(giver):
            raise ValidationError("You have reached your kudos limit for this week.")

        return Kudos.objects.create(giver=giver, receiver=receiver, message=message)
