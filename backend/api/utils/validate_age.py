from datetime import date

from django.core.exceptions import ValidationError


# Validate that the user is at least 18 year old
def validate_age(value):
    today = date.today()
    age = (
        today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    )

    if age < 18:
        raise ValidationError("User must be at least 18 years old.")
