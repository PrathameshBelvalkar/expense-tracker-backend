from django.db import models


class ExpenseCategory(models.TextChoices):
    FOOD = "FOOD", "Food"
    TRAVEL = "TRAVEL", "Travel"
    RENT = "RENT", "Rent"
    UTILITIES = "UTILITIES", "Utilities"
    ENTERTAINMENT = "ENTERTAINMENT", "Entertainment"
    OTHER = "OTHER", "Other"


class Expense(models.Model):
    title = models.CharField(max_length=255)

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    category = models.CharField(
        max_length=20,
        choices=ExpenseCategory.choices,
        default=ExpenseCategory.OTHER,
        db_index=True,
    )

    expense_date = models.DateField(db_index=True)

    description = models.TextField(blank=True)

    is_deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-expense_date", "-created_at"]
        indexes = [
            models.Index(fields=["category", "expense_date"]),
            models.Index(fields=["is_deleted"]),
        ]

    def __str__(self) -> str:
        return f"{self.title} - {self.amount}"
