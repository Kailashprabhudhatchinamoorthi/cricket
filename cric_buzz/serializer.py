from rest_framework import serializers
from .models import cric_profile,cric_board
class cric_profile_serializer(serializers.ModelSerializer):
    class Meta:
        model = cric_profile
        fields = '__all__'


class cric_board_serializer(serializers.Serializer):
    
    # id=models.AutoField(primary_key=True)
    # board_name=models.CharField(max_length=100)
    # board_orgin=models.CharField(max_length=100)

    id=serializers.IntegerField(read_only=True)
    board_name=serializers.CharField(max_length=100)
    board_orgin=serializers.CharField(max_length=100)

    class meta:
        fields=['id','board_name',board_orgin]

    pass    


