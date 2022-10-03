from django.db import models

SPECIES = (('Canine', 'Canine'), ('Feline', 'Feline'))
SEX = (('M', 'M'), ('MN', 'MN'), ('F', 'F'), ('FN', 'FN'))


class Record(models.Model):
    """
    Record model for animals.
    """
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    species = models.CharField(choices=SPECIES, max_length=10)
    breed = models.CharField(max_length=50)
    sex = models.CharField(choices=SEX, max_length=10)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    note = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.name + " " + self.surname

    class Meta:
        """
        Default ordering by alphabetically by surname.
        Add unique_together constraint to hopefully avoid duplicates.
        """
        ordering = ['surname']
        unique_together = ['name', 'surname', 'date_of_birth', 'species', 'breed', 'sex']
