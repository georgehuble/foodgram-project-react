from django.http import HttpResponse
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes

from .models import IngredientInRecipe, Shopping


@permission_classes([permissions.IsAuthenticated])
@api_view(['GET'])
def download_shopping_cart(request):
    user = request.user
    shopping_cart = Shopping.objects.filter(user=user)
    buying_list = {}
    for record in shopping_cart:
        recipe = record.name
        ingredients = IngredientInRecipe.objects.filter(recipe=recipe)
        for ingredient in ingredients:
            amount = ingredient.amount
            name = ingredient.ingredient.name
            measurement_unit = ingredient.ingredient.measurement_unit
            if name not in buying_list:
                buying_list[name] = {
                    'measurement_unit': measurement_unit,
                    'amount': amount
                }
            else:
                buying_list[name]['amount'] = (buying_list[name]['amount']
                                               + amount)
    wishlist = []
    for name, data in buying_list.items():
        wishlist.append(
            f"{name} - {data['amount']} {data['measurement_unit']}. \n")
    response = HttpResponse(wishlist, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="wishlist.txt"'
    return response
