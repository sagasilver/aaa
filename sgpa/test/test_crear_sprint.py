
from django.test import TestCase
from sgpa.models import Sprint



class SGPATestCase(TestCase):
	def test_crear_sprint(self):

         print('\n------Ejecutando test para crear sprint...-------')
         s = Sprint(duracion = 1, fechaInicio= '01-12-2016', fechaFin='12-12-2016', nombre='sprint')
         s.save()
         self.assertTrue(Sprint.objects.exists())
