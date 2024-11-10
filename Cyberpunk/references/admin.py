from django.contrib import admin
from .models import PriceCategory, Source, ItemType, KeyWords, Modification, TypeAmmo, KindAmmo, TypeKindAmmo, Weapon, WeaponKeyWords, WeaponAmmo


admin.site.register(PriceCategory)
admin.site.register(Source)
admin.site.register(ItemType)
admin.site.register(KeyWords)
admin.site.register(Modification)
admin.site.register(TypeAmmo)
admin.site.register(KindAmmo)
admin.site.register(TypeKindAmmo)
admin.site.register(Weapon)
admin.site.register(WeaponKeyWords)
admin.site.register(WeaponAmmo)


