from django.contrib import admin
from cars.models import Car
# Register your models here.

# Define the admin class
# Customizing for admin user
class CarAdmin(admin.ModelAdmin):
  fieldsets = (
    ('Car Information', {
      'fields': [
        'brand',  # CharField
      ]
    }),
    ('Production Details', {
      'fields': [
        'country',  # CharField
      ]
    }),
    ('Manufacture Date', {
      'fields': ['year']
          # DateField or DateTimeField
    }),
  )

  list_display = ('brand', 'country', 'year')
  search_fields = ('brand', 'country', 'year')
  readonly_fields = ('year',)  # Example of readonly field
  ordering = ('-year',)  # Example of default ordering

# Register the Car model with the admin site
admin.site.register(Car, CarAdmin)