from rest_framework import serializers
from .models import dish
from Chef.serializers import ChiefSerializer
from rest_framework import serializers



class DishSerializer(serializers.ModelSerializer):
    Chief_id=serializers.IntegerField(write_only=True)
    # author=AuthorSerializer(read_only=True)
    
    
    class Meta:
        model=dish
        fields=['dishname','rating',"Chief_id"]
        read_only_fields=['id'] 

        read_only_fields=['id']