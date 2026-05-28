# pyrefly: ignore [missing-import]
from django import template

register = template.Library()

@register.filter
def rupiah_format(value):
    try:
        # Convert to integer to avoid decimals if they exist
        value = int(float(value))
        # Format with dot as thousands separator
        return f"{value:,}".replace(",", ".")
    except (ValueError, TypeError):
        return value
