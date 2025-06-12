from rest_framework.serializers import ModelSerializer
from .models import systemAdmin

class SystemAdminSerializer(ModelSerializer):
    class Meta:
        model = systemAdmin
        fields = ['idAdmin', 'namesAdmin', 'lastNameAdmin', 'phoneAdmin', 'Username']