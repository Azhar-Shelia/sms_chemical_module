from django.db import models

# Create your models here.
class ChemicalElement(models.Model):
	id    = models.AutoField(primary_key=True)
	name  = models.CharField(max_length=100)
	# percentage = models.FloatField(max_length=100)

	def __str__(self):
		return self.name

# # Properties of a commodity are:
# class ChmicalPercentage(models.Model):

# 	name = models.CharField(max_length=100)
# 	percentage 				= models.CharField(max_length=100)
# 	chemical_percenatege	 	= models.ForeignKey(ChemicalElement, on_delete=models.CASCADE)
# 	    # tag = models.ManyToManyField(Tag)

# 	def __str__(self):
# 		return self.name

class Commodity(models.Model):
	id    = models.AutoField(primary_key=True)
	name 					= models.CharField(max_length=100)
	inventory				= models.FloatField("Tons")
	price					= models.FloatField("price")
	# chemical_composition 	= models.ForeignKey(ChemicalElement, on_delete=models.CASCADE)
	# chemical_manymany	 	= models.ManyToManyField(ChmicalPercentage)
	# c_map	 	= models.ManyToManyField(EC_MAP)
	    # tag = models.ManyToManyField(Tag)

	def __str__(self):
		return self.name


class EC_MAP(models.Model):

	commodity_id = models.ForeignKey(Commodity, on_delete=models.CASCADE, related_name='mtm')
	element_id = models.ForeignKey(ChemicalElement, on_delete=models.CASCADE, related_name='mtm')
	percentage = models.FloatField()

	def __str__(self):
		return self.commodity_id.name

class Dob(models.Model):
    day = models.IntegerField()
    month = models.CharField(max_length=10)
    year = models.IntegerField()

    def __str__(self):
        return str(self.day)

class User(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    age = models.IntegerField()
    dob = models.ForeignKey(Dob, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name


