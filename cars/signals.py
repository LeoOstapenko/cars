from django.db.models.signals import pre_save, post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car, CarInventory
from openai_api.client import get_car_ai_bio

def cars_inventory_update():
    cars_count = Car.objects.all().count() # Query no banco de dados atráves do ORM do Django.
    cars_value = Car.objects.aggregate(
        total_value=Sum('value')
    )['total_value']
    CarInventory.objects.create(
        cars_count=cars_count,
        cars_value=cars_value
    )

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        instance.bio = 'Sem informações.' # Caso não tenha mais bio gerada pela IA.
        # ai_bio = get_car_ai_bio( # Gerar bio do veículo por IA.
        #     instance.model, instance.brand, instance.model_year
        # )
        # instance.bio = ai_bio

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    cars_inventory_update()    

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    cars_inventory_update()