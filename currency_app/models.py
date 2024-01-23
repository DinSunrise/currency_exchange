from django.db import models


class CurrencyRequest(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    rate = models.DecimalField(max_digits=10, decimal_places=4)

    class Meta:
        ordering = ["-timestamp"]
