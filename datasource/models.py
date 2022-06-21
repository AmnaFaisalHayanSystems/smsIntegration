from django.db import models



class formatedData(models.Model):
    DATA_SOURCE = (
        ("P", "Partners"),
        ('O', "Other")
    )
    
    name = models.CharField(max_length=300)
    cnic = models.CharField(max_length=300)
    contactNumber = models.CharField(max_length=300)
    dataSource = models.CharField(max_length=300, choices=DATA_SOURCE, default="O")
    notes = models.TextField(blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name
    
    