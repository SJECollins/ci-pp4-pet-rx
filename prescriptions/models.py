from django.db import models
from records.models import Record
from vetprofiles.models import Vet


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


class Prescription(models.Model):
    animal = models.ForeignKey(Record, on_delete=models.CASCADE, default=1)
    animal_weight = models.DecimalField(max_digits=5, decimal_places=2)
    vet = models.ForeignKey(Vet, on_delete=models.CASCADE, default=1)
    drug = models.ForeignKey(Drugs, on_delete=models.PROTECT, default=None)
    drug_dose = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    route = models.CharField(max_length=8, blank=True)

    def __str__(self):
        return self.animal.name + " " + str(self.drug.dose) + " " + str(self.animal_weight) + " " + str(self.vet)

    def save(self, *args, **kwargs):
        self.animal_weight = self.animal.weight
        self.drug_dose = self.drug.dose
        super().save(*args, **kwargs)
