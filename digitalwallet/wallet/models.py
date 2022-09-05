
from django.db import models



# from requests import delete

class Customer(models.Model):
    first_name = models.CharField(max_length=15,null=True)
    last_name = models.CharField(max_length=15,null=True)
    GENDER_CHOICES = (
       ("Male","Male"),("Male","Female"),("They","They")
    )
    
    gender = models.CharField(max_length=40, choices=GENDER_CHOICES,null=True)
    address = models.TextField(max_length=40)
    age = models.PositiveIntegerField()
    COUNTRY_CHOICES = (
       ("Kenyan","Kenyan"),("Tanzanian","Tanzanian"),("Rwandees","Rwandees")
    )
    nationality = models.CharField(max_length=15,choices=COUNTRY_CHOICES,null=True)
    id_number = models.CharField(max_length=10,null=True)
    phone_number = models.CharField(max_length=15,null=True)
    email = models.EmailField()
    profile_picture = models.ImageField(default='default.jpg', upload_to='profile_pics')
    MARITAL_CHOICES = (
       ("married","Married"),("Single","Single"),("Engaged","Engaged")
    )
    marital_status=models.CharField(max_length=8,choices=MARITAL_CHOICES,null=True)
    
    employment_status = models.BooleanField(max_length=30,null=True)
    signature=models.ImageField(default='default.jpg',upload_to='profile_pics')

class Currency(models.Model):
    country=models.CharField(max_length=15)
    symbol=models.CharField(max_length=15) 

class Wallet(models.Model):
    balance = models.IntegerField(default="")
    customer_id = models.IntegerField(default="")
    currency=models.ForeignKey(Currency,on_delete=models.CASCADE,null=True)
    time = models.DateTimeField(default="")
    status = models.CharField(max_length=15,default="")
    history = models.DateTimeField(default="")
    pin = models.CharField(max_length=15,default="")
    active=models.BooleanField(null=True)
    datecreated=models.DateTimeField(default="")
    type=models.CharField(max_length=8,null=True)


class Account(models.Model):
    account_number = models.IntegerField()
    account_type = models.CharField(max_length=30)
    balance = models.IntegerField()
    saving=models.IntegerField(null=True)
    name = models.CharField(max_length=30)
    wallet = models.ForeignKey(Wallet, on_delete= models.CASCADE)

class Transaction(models.Model):
    transaction_code = models.CharField(max_length=30,null=True)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    transaction_amount = models.IntegerField()
    transaction_type = models.CharField(max_length=30)
    transaction_charge = models.IntegerField()
    transaction_time = models.DateTimeField()
    reciept = models.CharField(max_length=8,null=True)
    origin_account = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)
    destination_account = models.ForeignKey(Account, on_delete=models.CASCADE,null=True)

class Card(models.Model):
    issue_date = models.DateTimeField()
    card_name = models.CharField(max_length=30)
    card_number = models.IntegerField()
    card_type = models.CharField(max_length=30)
    expiry_date = models.DateTimeField()
    card_status = models.CharField(max_length=30)
    security_code = models.IntegerField()
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    issuer = models.CharField(max_length=30)

class Third_Party(models.Model):
    name = models.CharField(max_length=15)
    id = models.CharField(max_length=8)
    type = models.CharField(max_length=6)
    transaction_account = models.IntegerField()
    account = models.OneToOneField(Account,on_delete=models.CASCADE,primary_key=True)
    currency = models.ForeignKey(Currency,on_delete=models.CASCADE,null=True)

class Notifications(models.Model):
    transaction = models.CharField(max_length=15)
    transaction_id = models.IntegerField()
    transaction_amount = models.BigIntegerField()
    customer_id = models.IntegerField()
    status = models.CharField(max_length=6)
    transaction_number =models.CharField(max_length=7)
    date_time = models.DateTimeField()
    recipient = models.OneToOneField
    transaction_description = models.CharField(max_length=10)

class Receipt(models.Model):
    receipt_type = models.CharField(max_length=15)
    receipt_date = models.DateTimeField()
    bill_number = models.IntegerField()
    total_amount = models.IntegerField()
    transaction = models.ForeignKey(Transaction,on_delete=models.CASCADE,null=True)
    receipt_file = models.FileField()

class Loan(models.Model):
    loan_id = models.BigIntegerField()
    loan_type = models.CharField(max_length=15)
    amount = models.BigIntegerField()
    datetime = models.DateTimeField()
    Wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE)
    intrest_rate = models.IntegerField()
    payment_due_date = models.DateTimeField()
    loan_balance = models.IntegerField()
    guaranter = models.ForeignKey(Third_Party,on_delete=models.CASCADE,null=True) 


class Reward(models.Model):
    name = models.CharField(max_length=15)
    customer_id = models.IntegerField()
    gender = models.CharField(max_length=6)
    points = models.IntegerField()
    date_of_reward = models.DateTimeField()
    recipient = models.OneToOneField(Account,on_delete=models.CASCADE,null=True)



# class Customer(models.Model):
#     first_name =models.CharField(max_length=15)
#     last_name = models.CharField(max_length=15)
#     COUNTRY_CHOICES = (
#         ("Female","Female"),("Male","Female"),("They","They")
#     )
    
#     gender = models.CharField(max_length=1, choices=COUNTRY_CHOICES,null=True)
#     address =models.TextField()
#     age = models.PositiveIntegerField()
#     nationality = models.CharField()
#     id_number = models.CharField()
#     phone_number = models.CharField()
#     email = models.EmailField()
#     profile_picture = models.ImageField()