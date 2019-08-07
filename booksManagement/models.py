from django.db import models
import datetime
from django.utils.translation import gettext as _
from django.contrib.auth.models import User

# Create your models here.
class BookLists(models.Model):
	book_name = models.CharField(max_length = 250)
	author = models.CharField(max_length = 250)
	publication = models.CharField(max_length = 250)
	year_of_publication = models.CharField(max_length=250)
	summary = models.CharField(max_length=250)
	# year_of_publication = models.DateField(_("Date"), default = datetime.date.today)
	year_of_publication = models.CharField(max_length=250)
	status = models.IntegerField()
	user = models.ForeignKey(User, on_delete=models.CASCADE,) 

	class Meta:
		db_table = "book_list"