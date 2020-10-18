from django.contrib.auth.models import User, Group
from rest_framework import serializers
from sms_test.models import ChemicalElement, Commodity, EC_MAP

class ChemicalElementSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = ChemicalElement
        fields = '__all__'



class CommoditySerializer(serializers.ModelSerializer):

	class Meta:
		model = Commodity
		fields = ['id','name', 'price', 'inventory']

	def get_projects_data(self, obj):
		Commodity = Commodity.projects.all()
		return NestedProjectSerializer(Commodity, many=True).data


class ChemicalConcentrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = EC_MAP
        fields = ['commodity_id','element_id', 'percentage']

