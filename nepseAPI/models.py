from django.db import models
class Trade(models.Model):
    symbol=models.CharField(max_length=50)
    ltp=models.FloatField()
    change=models.FloatField()
    high=models.FloatField()
    low=models.FloatField()
    open=models.FloatField()
    qty=models.IntegerField()

    def __str__(self):
        return str(self.symbol)



class Company(models.Model):
    trade=models.OneToOneField(Trade,on_delete=models.CASCADE)
    name=models.CharField(max_length=250)
    sector=models.CharField(max_length=250)
    shares_outstanding= models.FloatField()
    market_price=models.FloatField()
    change=models.FloatField()
    last_trade_on=models.CharField(max_length=250,)
    weeks_52_high=models.FloatField()
    weeks_52_low=models.FloatField()
    day_120_average= models.FloatField()
    year_1_yeild=models.FloatField()
    eps=models.CharField(max_length=250,)
    pe_ratio=models.FloatField()
    book_value=models.FloatField()
    pbv=models.FloatField()
    dividend=models.CharField(max_length=250,)
    bonus=models.CharField(max_length=250,)
    right_share=models.CharField(max_length=250,)
    day_30_avg_volume=models.FloatField()
    market_capitalization=models.FloatField()


    
    
