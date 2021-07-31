from .models import Favourite

ingredients = Favourite.objects.all()
print(ingredients)
# shop_list = open('../media/file/shop_list.txt', 'w+')
# shop_list.write('Привет, список покупок!')
# shop_list.close()
