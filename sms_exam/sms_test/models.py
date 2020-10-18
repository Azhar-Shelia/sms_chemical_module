from django.db import models

# Create your models here.
class ChemicalElement(models.Model):
	id    = models.AutoField(primary_key=True)
	name  = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class Commodity(models.Model):
	id    = models.AutoField(primary_key=True)
	name 					= models.CharField(max_length=100)
	inventory				= models.FloatField("Tons")
	price					= models.FloatField("price")
	# chemical_composition 	= models.ForeignKey(ChemicalElement, on_delete=models.CASCADE)
	# chemical_manymany	 	= models.ManyToManyField(ChmicalPercentage)
	# c_map	 	= models.ManyToManyField(EC_MAP)

	def __str__(self):
		return self.name


class EC_MAP(models.Model):

	commodity_id = models.ForeignKey(Commodity, on_delete=models.CASCADE, related_name='mtm')
	element_id = models.ForeignKey(ChemicalElement, on_delete=models.CASCADE, related_name='mtm')
	percentage = models.FloatField()

	def __str__(self):
		return self.commodity_id.name
