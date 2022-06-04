from rest_framework import serializers
from .models import Register


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ['first_name', 'last_name', 'date_of_birth', 'email', 'address',
                  'type_of_housing', 'country', 'department', 'city', 'comments', 'created_date']
        extra_kwargs = {'id': {'required': False}}
