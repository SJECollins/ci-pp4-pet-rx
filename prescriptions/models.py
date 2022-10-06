from datetime import timedelta
from django.db import models
from django.utils import timezone
from records.models import Record
from vetprofiles.models import Vet


ROUTES = (('PO', 'PO'), ('IV', 'IV'), ('IM', 'IM'),
          ('SC', 'SC'), ('Topical', 'Topical'))
FREQUENCY = (('No Repeat', 'No Repeat'), ('SID', 'SID'),
             ('BID', 'BID'), ('TID', 'TID'))
MEASURE = (('ml', 'ml'), ('mg', 'mg'))
TYPES = (('Injectable', 'Injectable'), ('Liquid', 'Liquid'), ('Tablet', 'Tablet'))


class Category(models.Model):
    """
    Drug categories for Admin to add to site.
    """
    name = models.CharField(max_length=30)

    def __str__(self):
        """
        Returns name of category.
        """
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Drug(models.Model):
    """
    Drug model.
    Registered with admin. Admin to set details to be used in Prescription
    model by vets.
    __str__ method: Drug name.
    Ordered by name by default.
    """
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=10, choices=TYPES, default='Injectable')
    dose = models.DecimalField(max_digits=4, decimal_places=2)
    high_dose = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    tablet_strength = models.CharField(max_length=100, blank=True)
    measure = models.CharField(max_length=2, choices=MEASURE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    route = models.CharField(max_length=8, choices=ROUTES)
    warnings = models.CharField(max_length=300)

    def __str__(self):
        """
        Returns name of drug.
        """
        return self.name

    class Meta:
        ordering = ['name']


class Prescription(models.Model):
    """
    Prescription model.
    Ordered by date by default.
    __str__ method: animal name, dose, drug and vet name.
    save method: takes weight from Animal FK and dose from Drug FK, multiplies
    saves as dose. Also takes route and measure from Drug FK to populate.
    under_day method: with property decorator, used in prescription templates
    to allow deleting prescriptions under 24 hours old.
    """
    animal = models.ForeignKey(Record, on_delete=models.CASCADE, default=1)
    animal_weight = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    vet = models.ForeignKey(Vet, on_delete=models.CASCADE, default=1)
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE, default=None)
    type = models.CharField(max_length=10, blank=True)
    drug_dose = models.DecimalField(
        max_digits=4, decimal_places=2, blank=True, null=True)
    drug_dose_high = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    dose = models.CharField(max_length=100, blank=True, null=True)
    measure = models.CharField(max_length=2, blank=True)
    frequency = models.CharField(max_length=10, choices=FREQUENCY, blank=True)
    length = models.PositiveIntegerField(default=0, blank=True)
    route = models.CharField(max_length=8, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Default order is date, descending
        """
        ordering = ['-date']

    def __str__(self):
        return self.animal.name + " " + \
            str(self.dose) + " " + str(self.drug) + " " + str(self.vet)

    def save(self, *args, **kwargs):
        """
        Override the save method to populate weight, dose, route and measure
        based on animal and drug.
        Calculates dose by animal weight and drug dose, saves.
        """
        self.type = self.drug.type
        self.drug_dose = self.drug.dose
        self.drug_dose_high = self.drug.high_dose
        self.animal_weight = self.animal.weight
        self.route = self.drug.route
        self.measure = self.drug.measure

        if self.type == 'Injectable' or self.type == 'Liquid':
            self.dose = f"{self.animal_weight * self.drug_dose}"
        elif self.type == 'Tablet':
            strengths = [int(num) for num in self.drug.tablet_strength.split(',') if num.strip().isdigit()]
            quartstrengths = [strength / 4 for strength in strengths]
            low = int(self.drug_dose * self.animal_weight)
            high = int(self.drug_dose_high * self.animal_weight)
            results = {'numtabs': 0, 'strength': 0}
            for num in range(low, high):
                size_list = []
                for quart in quartstrengths:
                    if num % quart == 0:
                        size_list.append(num)
                        smallest = min(size_list) / quart
                        if results['numtabs'] == 0 or smallest < results['numtabs']:
                            results['numtabs'] = smallest
                            results['strength'] = quart
            self.dose = f"{results['numtabs'] / 4}tabs x {int(results['strength'] * 4)}"
        super().save(*args, **kwargs)

    @property
    def under_day(self):
        """
        To identify prescriptions under a day old
        """
        now = timezone.now()
        return now - timedelta(hours=24) < self.date <= now
