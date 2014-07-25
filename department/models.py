from django.db import models

# Create your models here.

class Employee(models.Model):
	name = models.CharField(max_length="200")
	email = models.CharField(max_length="200")
	password = models.CharField(max_length="50")
	supervisor = models.ForeignKey('self', related_name='supervisor_to+', null=True, blank=True)
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.name	

class Document(models.Model):
	title = models.CharField(max_length="200")
	instructions = models.CharField(max_length="1240")
	request_date = models.DateTimeField('date published')
	due_date = models.DateTimeField('date due')
	situation = models.IntegerField(default=0) # 0 requested | 1 done
	approved = models.IntegerField(default=0) # 0 not | 1 yes
	pdf = models.FileField(upload_to='pdfs')
	responsible = models.ForeignKey(Employee, related_name='responsible_to+', null=True, blank=True)
	requester = models.ForeignKey(Employee, related_name='requester_to+', null=True, blank=True)
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.title


