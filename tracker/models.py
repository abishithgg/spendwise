from django.db import models
from django.contrib.auth.models import User


class Expense(models.Model):

    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Transport', 'Transport'),
        ('Shopping', 'Shopping'),
        ('Education', 'Education'),
        ('Entertainment', 'Entertainment'),
        ('Bills', 'Bills'),
        ('Other', 'Other'),
    ]

    PAYMENT_CHOICES = [
        ('Cash', 'Cash'),
        ('UPI', 'UPI'),
        ('Card', 'Card'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=100)

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES
    )

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_CHOICES
    )

    date = models.DateField()

    description = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class Income(models.Model):

    SOURCE_CHOICES = [
        ('Salary', 'Salary'),
        ('Pocket Money', 'Pocket Money'),
        ('Freelance', 'Freelance'),
        ('Business', 'Business'),
        ('Gift', 'Gift'),
        ('Other', 'Other'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=100)

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    source = models.CharField(
        max_length=30,
        choices=SOURCE_CHOICES
    )

    date = models.DateField()

    description = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class Budget(models.Model):

    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Transport', 'Transport'),
        ('Shopping', 'Shopping'),
        ('Education', 'Education'),
        ('Entertainment', 'Entertainment'),
        ('Bills', 'Bills'),
        ('Other', 'Other'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    month = models.DateField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = ('user', 'category', 'month')

    def __str__(self):
        return f"{self.category} - {self.amount}"