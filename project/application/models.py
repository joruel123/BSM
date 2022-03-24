from django.db import models

class Province(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=250)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Barangay(models.Model):
    name = models.CharField(max_length=250)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Survey(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    contact = models.CharField(max_length=250)
    age = models.IntegerField(default=0)
    precinct = models.CharField(max_length=250)

    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    barangay = models.ForeignKey(Barangay, on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name + ', ' + self.first_name

