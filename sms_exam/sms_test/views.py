from django.shortcuts import render
from rest_framework import status
from django.shortcuts import render,redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from . serializers import CommoditySerializer, ChemicalElementSerializer , ChemicalConcentrationSerializer
from sms_test import models
# import datetime



ChemicalElement = models.ChemicalElement.objects.all()

class chemicaldetails(APIView):

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
		if unknown_element:
			ec_map_id = models.EC_MAP.objects.filter(element_id=unknown_id)
			serializer = ChemicalConcentrationSerializer(ec_map_id[0], data={'percentage': unknown_percent}, partial=True)
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
		ec_map_id.delete()
		self.update_unknown(commodity_id)
		return Response(status=status.HTTP_204_NO_CONTENT)


