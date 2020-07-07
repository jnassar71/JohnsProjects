from django.contrib import admin
from MiniCaseApp.models import Person
from MiniCaseApp.models import Case
from MiniCaseApp.models import Contract
from MiniCaseApp.models import ContractDetails
from MiniCaseApp.models import Location 

admin.site.register(Person)
admin.site.register(Case)
admin.site.register(Contract)
admin.site.register(ContractDetails)
admin.site.register(Location)