from django.contrib.auth.models import User, Group
from rest_framework import serializers
from sms_test.models import ChemicalElement, Commodity, Dob, User, EC_MAP

class ChemicalElementSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = ChemicalElement
        fields = '__all__'


# class ChmicalPercentageSerializer(serializers.ModelSerializer):

# 	chemical_percenatege = ChemicalElementSerializer(many=True)

# 	class Meta:
# 		model = ChmicalPercentage
# 		fields = ['id', 'percentage', 'chemical_percenatege']

class CommoditySerializer(serializers.ModelSerializer):

	# chemical_manymany = ChemicalElementSerializer(many=True)

	class Meta:
		model = Commodity
		# fields = '__all__'
		fields = ['id','name', 'price', 'inventory']


    # class Meta:
    #     model = Network
    #     fields = (
    #         'id',
    #         'name',
    #         'projects',
    #         'projects_data',
    #         'creation_date',
    #     )

	def get_projects_data(self, obj):
		Commodity = Commodity.projects.all()
		return NestedProjectSerializer(Commodity, many=True).data


class ChemicalConcentrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = EC_MAP
        # fields = '__all__'
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
