from .models import WeightLog
from decimal import Decimal


def convert(profile):
    if profile.weight is not None:
        weights = WeightLog.objects.all()

        for weight in weights:
            if profile.metric == 'kg':
                weight.weight = weight.weight / Decimal(2.20462)
            elif profile.metric == 'lbs':
                weight.weight = weight.weight * Decimal(2.20462)
            weight.save()
