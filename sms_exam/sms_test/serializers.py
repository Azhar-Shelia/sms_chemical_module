from django.contrib.auth.models import User, Group
from rest_framework import serializers
from sms_test.models import ChemicalElement, Commodity, Dob, User, EC_MAP

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

class DobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dob 
        fields = ('day', 'month', 'year')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    dob = DobSerializer(many=False, read_only=True);

    class Meta:
        model = User
        fields = ('name', 'age', 'dob');
