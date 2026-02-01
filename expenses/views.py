from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Expense
from .serializers import ExpenseSerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        return Expense.objects.filter(is_deleted=False)

    def destroy(self, request, *args, **kwargs):
        expense = self.get_object()
        expense.is_deleted = True
        expense.save(update_fields=["is_deleted"])

        return Response(
            {"detail": "Expense deleted successfully."},
            status=status.HTTP_204_NO_CONTENT,
        )
