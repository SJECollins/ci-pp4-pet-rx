from django.db import models


ROUTES = (('IV', 'IV'), ('IM', 'IM'), ('SC', 'SC'), ('TOPICAL', 'Topical'))
CATEGORIES = (('NSAID', 'NSAID'), ('ANTIBIOTIC', 'Antibiotic'), ('SEDATIVE', 'Sedative'), ('OPIOID', 'Opioid'))
REPEAT = (('NO', 'No'), ('SID', 'SID'), ('BID', 'BID'), ('TID', 'TID'), ('TOPICAL', 'Topical'))


class Drugs(models.Model):
    name = models.CharField(max_length=50)
    dose = models.DecimalField(max_digits=4, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORIES)
    route = models.CharField(max_length=8, choices=ROUTES)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Drugs'
