from django.db import models
from django.db.models import Q


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)



class ProfileComplete(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(Q(first_name__isnull=False) & Q(last_name__isnull=False)& Q(address__isnull=False))



class InActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=True)



        
