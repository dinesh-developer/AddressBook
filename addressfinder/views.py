from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import View
import csv
from .models import Address

# Create your views here.

class Home(View):
	"""
	Home or base class to land user on home page.
	Here we also read csv to show matching result.
	"""
	def get(self, request, *args, **kwargs):
		found_addresses = []
		context = {'found_addresses': found_addresses}
		if 'address' in request.GET and request.GET['address'].strip() != '':
			address_to_find = request.GET['address'].strip().split(' ')
			csv_file = csv.reader(open('address.csv', "r"), delimiter=",")
			for row in csv_file:
				updated_row = list(map(lambda x:x.lower(), row))
				for address in address_to_find:
					if address.lower() in updated_row and row not in found_addresses:
						found_addresses.append(row)
			if found_addresses:
				context.update({"all_addresses":found_addresses})
		return render(request, 'home.html', context)


def save_address_csv_to_db(request):
	"""
	To save all csv data in database.
	"""
	csv_file = csv.reader(open('address.csv', "r"), delimiter=",")
	for row in csv_file:
		Address.objects.create(first_name=row[0], last_name=row[1], street=row[2], city=row[3], state=row[4])
	return HttpResponseRedirect("/")
