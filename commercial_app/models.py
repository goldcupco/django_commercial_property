# commercial_app/models.py
from django.db import models

class CommercialProperty(models.Model):
    address01 = models.CharField(max_length=255)
    building_type = models.CharField(max_length=255,default='1')
    ownership = models.CharField(max_length=255,default='ABC')
    lot_size = models.PositiveIntegerField(default=0)
    building_size = models.PositiveIntegerField(default=0)
    price_per_square_meter = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    total_asking_price = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    total_price_offered = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    total_price_agreed = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    deal_status = models.CharField(max_length=255,default='FORSALE')
    listing_date = models.DateField()
    listing_agent_name = models.CharField(max_length=255,default='')
    listing_agent_phone = models.CharField(max_length=20,default='000000')
    description = models.TextField(default='')
    deal_comments = models.TextField(default='')

    def __str__(self):
        return f"""
        Address01: {self.address01}
        Building Type: {self.building_type}
        Ownership: {self.ownership}
        Lot Size: {self.lot_size}
        Building Size: {self.building_size}
        Price per Square Meter: {self.price_per_square_meter}
        Total Asking Price: {self.total_asking_price}
        Total Price Offered: {self.total_price_offered}
        Total Price Agreed: {self.total_price_agreed}
        Deal Status: {self.deal_status}
        Listing Date: {self.listing_date}
        Listing Agent Name: {self.listing_agent_name}
        Listing Agent Phone: {self.listing_agent_phone}
        Description: {self.description}
        Deal Comments: {self.deal_comments}
        """
