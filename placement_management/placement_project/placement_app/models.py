from django.db import models


class Student(models.Model):

    student_id = models.CharField(
        max_length=20,
        primary_key=True
    )

    name = models.CharField(max_length=100)

    email = models.EmailField()

    password = models.CharField(max_length=100)

    branch = models.CharField(max_length=50)

    cgpa = models.FloatField()

    def __str__(self):

        return self.name


class Company(models.Model):

    company_id = models.CharField(
        max_length=20,
        primary_key=True
    )

    company_name = models.CharField(max_length=100)

    role = models.CharField(max_length=100)

    package = models.FloatField()

    def __str__(self):

        return self.company_name


class Application(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )

    status = models.CharField(max_length=20)

    resume = models.FileField(
        upload_to='resumes/',
        null=True,
        blank=True
    )