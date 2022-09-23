from datetime import timedelta
from django.db import models
from django.utils import timezone
from records.models import Record
from vetprofiles.models import Vet


ROUTES = (('IV', 'IV'), ('IM', 'IM'), ('SC', 'SC'), ('TOPICAL', 'Topical'))
CATEGORIES = (('NSAID', 'NSAID'), ('ANTIBIOTIC', 'Antibiotic'), ('SEDATIVE', 'Sedative'), ('OPIOID', 'Opioid'))
REPEAT = (('NO', 'No'), ('SID', 'SID'), ('BID', 'BID'), ('TID', 'TID'), ('TOPICAL', 'Topical'))
MEASURE = (('ML', 'ml'), ('MG', 'mg'))


class Drugs(models.Model):
    name = models.CharField(max_length=50)
    dose = models.DecimalField(max_digits=4, decimal_places=2)
    measure = models.CharField(max_length=2, choices=MEASURE)
    category = models.CharField(max_length=20, choices=CATEGORIES)
    route = models.CharField(max_length=8, choices=ROUTES)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Drugs'


class Prescription(models.Model):
    animal = models.ForeignKey(Record, on_delete=models.CASCADE, default=1)
    animal_weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    vet = models.ForeignKey(Vet, on_delete=models.CASCADE, default=1)
    drug = models.ForeignKey(Drugs, on_delete=models.PROTECT, default=None)
    drug_dose = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    dose = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    measure = models.CharField(max_length=2, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    route = models.CharField(max_length=8, blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.animal.name + " " + str(self.dose) + " " + str(self.drug) + " " + str(self.vet)

    def save(self, *args, **kwargs):
        self.animal_weight = self.animal.weight
        self.drug_dose = self.drug.dose
        self.dose = self.animal_weight * self.drug_dose
        self.route = self.drug.route
        self.measure = self.drug.measure
        super().save(*args, **kwargs)

    @property
    def under_day(self):
        now = timezone.now()
        return now-timedelta(hours=12) < self.date <= now
