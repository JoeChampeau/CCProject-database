from django.db import models

class AccessionNumber(models.Model):
    year = models.IntegerField()
    collection = models.IntegerField()
    index = models.IntegerField()
    subindex = models.CharField(blank=True)
    def __str__(self):
        return f'{self.year}.{self.collection}.{self.index}{("." + self.subindex) if self.subindex != "" else ""}'

class DateRange(models.Model):
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    include_day = models.BooleanField(default=True)
    include_month = models.BooleanField(default=True)
    def __str__(self):
        format_s = f'{"%d " if self.include_day else ""}{"%b " if self.include_month else ""}%Y'
        start_s = self.date_start.strftime(format_s) if self.date_start else ""
        end_s = self.date_end.strftime(format_s) if self.date_end else ""
        return start_s if not end_s else start_s + " - " + end_s


class Item(models.Model):
    accession = models.ForeignKey(AccessionNumber, on_delete=models.CASCADE)
    description = models.TextField()
    notes = models.TextField()
    date_range = models.ForeignKey(DateRange, on_delete=models.CASCADE)