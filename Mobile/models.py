from django.db import models

# Create your models here.


class Mobile_Company(models.Model):
    company_id = models.AutoField(primary_key=True, unique=True)
    company_name = models.CharField(max_length=32)
    is_indian = models.BooleanField(default=False)

    def __str__(self):
        return self.company_name


class Mobile_Model(models.Model):
    company = models.ForeignKey(Mobile_Company, on_delete=models.CASCADE)

    def number():
        no = Mobile_Model.objects.count()
        comapnyName = Mobile_Company.objects.filter(company_id=1)
        if no == None:
            return comapnyName[0].company_name[0] + str(1)
        else:
            return comapnyName[0].company_name[0] + str(no + 1)

    model_id = models.AutoField(
        primary_key=True, unique=True)
    model_name = models.CharField(max_length=32)

    internal_id = models.CharField(
        max_length=32, default=number)

    def __str__(self):
        return self.model_name
