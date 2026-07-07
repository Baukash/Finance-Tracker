from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes


from .models import Expense, Wallet
from .serializers import ExpenseSerializer, WalletSerializer

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def expense_api(request):
    expenses = Expense.objects.filter(owner=request.user)
    serializer = ExpenseSerializer(expenses, many=True)
    return Response(serializer.data)

class WalletAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        wallets = Wallet.objects.filter(owner=request.user)
        serializer = WalletSerializer(wallets, many=True)
        return Response(serializer.data)