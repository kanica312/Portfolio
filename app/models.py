from django.db import models

class contactform(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=100)
    phone_number=models.CharField(max_length=15)
    message=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=['created_at']
    def __str__(self):
        return  f'{self.name}-{self.created_at.strftime("%y-%m-%d")}' 
