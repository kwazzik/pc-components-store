from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Employee(AbstractUser):
    brand = models.ForeignKey(
        Brand,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="employees"
    )
    employee_number = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "employee"
        verbose_name_plural = "employees"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("catalog:employee-detail", kwargs={"pk": self.pk})


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="products")
    price = models.DecimalField(decimal_places=2, max_digits=10)
    in_stock = models.BooleanField(default=False)
    amount = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    managers = models.ManyToManyField(Employee, related_name="products")

    def __str__(self):
        return self.name

