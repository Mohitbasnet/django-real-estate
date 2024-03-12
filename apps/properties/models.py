import random 
import string
from autoslug import AutoSlugField
from django.contrib.auth import get_user_model

from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries import CountryField

from apps.common.models import TimeStampedUUIDModel

User = get_user_model()

class PropertyPublishManager(models.Manager):

    def get_queryset(self):
        return(
            super(PropertyPublishManager, self)
            .get_queryset()
            .filter(published_status = True)
        )
class Property(TimeStampedUUIDModel):
    class AdveerType(models.TextChoices):
        FOR_SALE = "For Sale", _("For Sale")
        FOR_RENT = "For Rent", _("For Rent")
        AUCTION = "Auction", _("Auction")

    class PropertyType(models.TextChoices):
        HOUSE = "House", _("House")
        APARTMENT = "Apartment", _("Apartment")
        OFFICE = "Office", _("Office")
        WAREHOUSE = "Warehouse", _("Warehouse")
        COMMERCIAL = "Commercial", _("Commercial")
        OTHER = "Other", _("Other")
    
    user = model.ForeignKey(User, verbose_name = _("Agent,Seller or Buyer"),
    related_name = "agent_buyer", on_delete = models.DO_NOTHING)
    title = models

