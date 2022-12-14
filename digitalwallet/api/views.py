
# Create your views here.
from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from rest_framework import viewsets
from wallet.models import Card, Customer, Loan, Notifications, Receipt, Transaction, Wallet
from .serializers import CardSerializer, CustomerSerializer, LoanSerializer, ReceiptSerializer, TransactionSerializer,WalletSerializer
from django.shortcuts import render
from rest_framework import viewsets
from wallet.models import Account, Card, Customer, Loan, Notifications, Receipt, Transaction, Wallet
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset= Customer.objects.all()
    serializer_class =CustomerSerializer


class WalletViewSet(viewsets.ModelViewSet):
    queryset= Wallet.objects.all()
    serializer_class =WalletSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset= Card.objects.all()
    serializer_class =CardSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset= Transaction.objects.all()
    serializer_class =TransactionSerializer  

class LoanViewSet(viewsets.ModelViewSet):
    queryset= Loan.objects.all()
    serializer_class =LoanSerializer 

class ReceiptViewSet(viewsets.ModelViewSet):
    queryset= Receipt.objects.all()
    serializer_class =Receipt      

class NotificationsViewSet(viewsets.ModelViewSet):
    queryset= Notifications.objects.all()
    serializer_class =Notifications    


class AccountDepositView(views.APIView):
   """
   This class allows deposit of funds to an account.
   Accepts this JSON data
   {
       "account_id": 123,
       "amount": 1000
   }
   This API needs Authentication and Permissions to be added
   """
   def post(self, request, format=None):       
       account_id = request.data["account_id"]
       amount = request.data["amount"]
       try:
           account = Account.objects.get(id=account_id)
       except ObjectDoesNotExist:
           return Response("Account Not Found", status=404)
      
       message, status = account.deposit(amount)
       return Response(message, status=status)  



class AccountTransferView(views.APIView):
  

   def post(self, request, format=None):       
       account_id = request.data["account_id"]
       amount = request.data["amount"]
       try:
           account = Account.objects.get(id=account_id)
       except ObjectDoesNotExist:
           return Response("Account Not Found", status=404)

       message, status = account.transfer(amount)
       return Response(message, status=status)




      
class AccountWithdrawView(views.APIView):

   def post(self, request, format=None):       
       account_id = request.data["account_id"]
       amount = request.data["amount"]
       try:
           account = Account.objects.get(id=account_id)
       except ObjectDoesNotExist:
           return Response("Account Not Found", status=404)

       message, status = account.withdraw(amount)
       return Response(message, status=status)


class AccountRequestLoanView(views.APIView):

   def post(self, request, format=None):       
       account_id = request.data["account_id"]
       amount = request.data["amount"]
       try:
           account = Account.objects.get(id=account_id)
       except ObjectDoesNotExist:
           return Response("Account Not Found", status=404)

       message, status = account.deposit(amount)
       return Response(message, status=status)





class AccountRepayLoanView(views.APIView):



   def post(self, request, format=None):       
       account_id = request.data["account_id"]
       amount = request.data["amount"]
       try:
           account = Account.objects.get(id=account_id)
       except ObjectDoesNotExist:
           return Response("Account Not Found", status=404)

       message, status = account.withdraw(amount)
       return Response(message, status=status)       



class AccountBuyAirtimeView(views.APIView):

   def post(self, request, format=None):       
       account_id = request.data["account_id"]
       amount = request.data["amount"]    




