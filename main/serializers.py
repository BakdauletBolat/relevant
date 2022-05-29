from rest_framework.serializers import ModelSerializer
from .models import TelegramUser
class TelegramBotSerializer(ModelSerializer):


    class Meta:
        model = TelegramUser
        fields = ('id','chat_id','user_name')
        