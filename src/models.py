from django.db import models

# Create your models here.
class User(models.Model):
    User_Id = models.CharField(null=False, max_length=20, primary_key=True)
    User_Name = models.CharField(null=False, max_length=20)
    User_Password = models.CharField(null=False, max_length=20)

    def __str__(self):
        return self.User_Name

class Problem(models.Model):
    Problem_Id = models.IntegerField(null=False, max_length=10, primary_key=True, auto_created=True)
    Problem_Title = models.CharField(null=False, max_length=200)
    Problem_Description = models.TextField(default='')
    Problem_Input = models.TextField(default='')
    Problem_Output = models.TextField(default='')
    Problem_Simple_Input = models.TextField(default='')
    Problem_Simple_Output = models.TextField(default='')
    Problem_Spj = models.IntegerField(default=0)
    Problem_Hint = models.TextField(default='')
    Problem_Source = models.CharField(default='', max_length=100)
    Problem_Sample_Program = models.CharField(default='', max_length=255)

    def __str__(self):
        return self.Problem_Title
