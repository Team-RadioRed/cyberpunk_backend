from django.contrib import admin
from .models import (
    Source, PriceCategory, ItemType, Weapon, KeyWord, WeaponKeyWord,
    Modification, DefaultWeaponModification, KindAmmo, WeaponAmmo,
    TypeAmmo, TypeKindAmmo, ProgramType, ProgramClass, Demon, Program,
    LossHumanity, InstallationLocation, Implant, Slot, ImplantSlot
)

# Регистрация моделей в админке

@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')

@admin.register(PriceCategory)
class PriceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(ItemType)
class ItemTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    list_display = ('name_rus', 'name_eng', 'type', 'price_category', 'price_low', 'price_middle', 'price_high', 'hidden')
    search_fields = ('name_rus', 'name_eng')
    list_filter = ('type', 'price_category', 'hidden')

@admin.register(KeyWord)
class KeyWordAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(WeaponKeyWord)
class WeaponKeyWordAdmin(admin.ModelAdmin):
    list_display = ('weapon', 'key_word')
    search_fields = ('weapon__name_rus', 'key_word__name')

@admin.register(Modification)
class ModificationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(DefaultWeaponModification)
class DefaultWeaponModificationAdmin(admin.ModelAdmin):
    list_display = ('weapon', 'modification')
    search_fields = ('weapon__name_rus', 'modification__name')

@admin.register(KindAmmo)
class KindAmmoAdmin(admin.ModelAdmin):
    list_display = ('name', 'buy_count')
    search_fields = ('name',)

@admin.register(WeaponAmmo)
class WeaponAmmoAdmin(admin.ModelAdmin):
    list_display = ('weapon', 'kind_ammo')
    search_fields = ('weapon__name_rus', 'kind_ammo__name')

@admin.register(TypeAmmo)
class TypeAmmoAdmin(admin.ModelAdmin):
    list_display = ('price', 'description', 'price_category')
    search_fields = ('description',)

@admin.register(TypeKindAmmo)
class TypeKindAmmoAdmin(admin.ModelAdmin):
    list_display = ('kind_ammo', 'type_ammo')
    search_fields = ('kind_ammo__name', 'type_ammo__description')

@admin.register(ProgramType)
class ProgramTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'takes_up_space')
    search_fields = ('name',)

@admin.register(ProgramClass)
class ProgramClassAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Demon)
class DemonAdmin(admin.ModelAdmin):
    list_display = ('name_rus', 'name_eng', 'health', 'interface', 'combat_number', 'price', 'price_category', 'source')
    search_fields = ('name_rus', 'name_eng')
    list_filter = ('price_category', 'source')

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name_rus', 'name_eng', 'program_type', 'program_class', 'price', 'price_category', 'source')
    search_fields = ('name_rus', 'name_eng')
    list_filter = ('program_type', 'program_class', 'price_category', 'source')

@admin.register(LossHumanity)
class LossHumanityAdmin(admin.ModelAdmin):
    list_display = ('name', 'average_value', 'formula')
    search_fields = ('name',)

@admin.register(InstallationLocation)
class InstallationLocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)

@admin.register(Implant)
class ImplantAdmin(admin.ModelAdmin):
    list_display = ('name_rus', 'name_eng', 'installation_location', 'loss_humanity', 'price', 'price_category', 'source')
    search_fields = ('name_rus', 'name_eng')
    list_filter = ('installation_location', 'loss_humanity', 'price_category', 'source')

@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(ImplantSlot)
class ImplantSlotAdmin(admin.ModelAdmin):
    list_display = ('implant', 'slot')
    search_fields = ('implant__name_rus', 'slot__name')
