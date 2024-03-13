from rest_framework import serializers

from . models import Enquiry

class EnquirySerializer(serializers,ModelSerializers):
    
    class Meta:

        model = Enquiry
        fields = "__all__"
    


