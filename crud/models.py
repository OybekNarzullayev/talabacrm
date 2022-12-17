from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField('Ism',max_length=255,help_text='Ali')
    l_name = models.CharField('Familiya',max_length=255,help_text='Aliyev')
    age = models.IntegerField('Yosh',help_text='25')
    country = models.CharField('Vatani',max_length=255,help_text='Marokash',blank=True,null=True)
    region = models.CharField('Viloyat',max_length=255,help_text='Samarqand')
    group = models.IntegerField('Guruh')

    def __str__(self):
        return f'{self.name}  {self.l_name}'