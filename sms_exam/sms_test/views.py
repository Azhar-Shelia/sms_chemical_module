from django.shortcuts import render

# Create your views here.
from rest_framework import status

from django.shortcuts import render,redirect




from rest_framework.views import APIView

from rest_framework.response import Response

from . serializers import CommoditySerializer, ChemicalElementSerializer, UserSerializer , ChemicalConcentrationSerializer
from sms_test import models
# import datetime



# Commodity = Commodity.objects.all()
ChemicalElement = models.ChemicalElement.objects.all()

class chemicaldetails(APIView):

	# Commodity = Commodity.objects.all()


	def get_data(self, db_id):
		ec_map_list = []
		ec_map_id = models.EC_MAP.objects.filter(commodity_id=db_id)
		for each_id in ec_map_id:
			ec_map_list.append(
							{
								"element" : {"id": each_id.element_id.id, "name": each_id.element_id.name},
								"percentage": each_id.percentage
							}
			)
		return ec_map_list

	def get(self,request, pk):
		
		Commodity = models.Commodity.objects.get(id=pk)
		
		dict_data = {'id': Commodity.id,
					"name":Commodity.name,
					"price":Commodity.price,
					"inventory":Commodity.inventory,
					"chemical_composition":self.get_data(Commodity.id),
					}
		return Response(dict_data)


	def post(self, pk):
		print("----pk----",pk)
		pass

	def put(self, request, pk):
		pk = self.kwargs.get('pk')
		Commodity = models.Commodity.objects.get(id=pk)
		print(request.data.update({'inventory': Commodity.inventory}))
		serializer = CommoditySerializer(Commodity, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	# def put(self, request, *args, **kwargs):
	# 	pk = self.kwargs.get('pk')
	# 	Commodity = models.Commodity.objects.get(id=pk)
	# 	print("co----------",kwargs,args,request.data )
	# 	# klklkl
	# 	new_data = {}
	# 	if pk ==  request.data.get('id'):
	# 		new_data = {
	# 					'id': pk,
	# 					'name':request.data.get('name'),
	# 					'price':request.data.get('price'),
	# 					"inventory":Commodity.inventory,
	# 					"chemical_composition":self.get_data(Commodity.id),

	# 						}
	# 		# print(new_data)

	# 	record = CommoditySerializer(data=new_data)
	# 	print("---mkmk-----",record.is_valid(),record.errors)
	# 	if record.is_valid():
	# 		# jjjjjjjjjjj
	# 		record.save()
	# 		return Response(record.data, status=status.HTTP_202_ACCEPTED)
	# 	return Response(record.errors, status=status.HTTP_400_BAD_REQUEST)

# {
# "id": 3,
# "name": "new commodity name",
# "price": 1000
# }

class chemicalelementdetails(APIView):

	def get(self,request):
		ChemicalElement = models.ChemicalElement.objects.all()
		serializers = ChemicalElementSerializer(ChemicalElement,many=True)
		return Response(serializers.data)


	def post(self):
		pass




class ChemicalConcentration(APIView):

	def update_unknown(self, id):
		ec_map_data = { }
		ch_percentage = 0.0
		unknown_element = ''
		ec_map_id = models.EC_MAP.objects.filter(commodity_id=id)
		unknown_id = models.ChemicalElement.objects.get(name='unknown')
		for i in ec_map_id:
			if i.element_id.name == 'unknown':
				unknown_element = i.element_id
			else:
				ch_percentage += i.percentage

		print(ch_percentage)

		unknown_percent = 100 - ch_percentage
		print(">>>>>>.",unknown_percent)
		if unknown_element:
			ec_map_id = models.EC_MAP.objects.filter(element_id=unknown_id)
			# llllllll
			serializer = ChemicalConcentrationSerializer(ec_map_id[0], data={'percentage': unknown_percent}, partial=True)
			# print(serializer.is_valid(), serializer.errors,serializer.data )
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
		else:

			ec_map_data = {
							'commodity_id': id,
							'element_id' : unknown_id.id,
							'percentage': unknown_percent
			}
			serializer = ChemicalConcentrationSerializer(data=ec_map_data)
			if serializer.is_valid():
				serializer.save()
				return True

	def get(self, request, pk):
		print(pk)
		if pk:
			ec_map_id = models.EC_MAP.objects.filter(id=pk)
			serializer = ChemicalConcentrationSerializer(ec_map_id, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def post(self, request, pk=None):
		serializer = ChemicalConcentrationSerializer(data=request.data)
		print(request.data)
		
		if serializer.is_valid():
			serializer.save()
			self.update_unknown(request.data.get('commodity_id'))
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		ec_map_id = models.EC_MAP.objects.get(id=pk)
		print(ec_map_id)
		commodity_id = ec_map_id.commodity_id.id
		
		
		
		# kkk
		ec_map_id.delete()
		self.update_unknown(commodity_id)
		
		return Response(status=status.HTTP_204_NO_CONTENT)


