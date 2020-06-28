from django.db import models
from django.core.exceptions import ValidationError
from constance import config
import datetime

# Create your models here.

class fichas(models.Model):
	ci = models.IntegerField(
		null=False,
		blank=False,
	)
	nombre_apellidos = models.CharField(
		max_length=300,
		null=False,
		blank=False
	)
	fecha = models.DateField(
		null=False,
		blank=False,
		auto_now_add=True
	)
	atendido = models.BooleanField(
		default=False,
		blank=False,
		null=False
	)
	def clean(self):
		can = fichas.objects.filter(fecha=datetime.date.today())
		if len(can)>=config.FICHAS_DIA:
			raise ValidationError("Ya no se pueden reservar mas!!! el cupo maximo por dias es de "+str(config.FICHAS_DIA))

		can = fichas.objects.filter(fecha=datetime.date.today(),ci=self.ci)
		if(len(can)!=0):
			raise ValidationError("Ya iso su reserva solo se permite una por dia!!!")
	class Meta:
		unique_together = (('ci','fecha'),)
	def __str__(self):
		return str(self.id)