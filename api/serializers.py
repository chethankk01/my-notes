from statistics import mode
from rest_framework.serializers import ModelSerializer
from .models import Note,Login
class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

class LoginSerializer(ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'