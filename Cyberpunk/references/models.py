from django.db import models

# Источники
class Source(models.Model):
    name = models.CharField(max_length=50)  # Полное название
    code = models.CharField(max_length=5, blank=True, null=True)  # Аббревиатура

    class Meta:
        db_table = 'source'
        unique_together = (('name', 'code'),)  # Уникальность комбинации полное название + аббревиатура


# Категории цен
class PriceCategory(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'price_category'


# Оружие
class ItemType(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'item_type'


class Weapon(models.Model):
    name_rus = models.CharField(max_length=50)
    name_eng = models.CharField(max_length=50)
    is_exotic = models.BooleanField(default=False)
    type = models.ForeignKey(ItemType, on_delete=models.CASCADE)
    skill_need = models.TextField(blank=True, null=True)
    damage = models.IntegerField(blank=True, null=True)
    magazine = models.IntegerField(blank=True, null=True)
    rate_of_fire = models.IntegerField(default=2)
    grab_type = models.IntegerField(default=1)
    price_category = models.ForeignKey(PriceCategory, on_delete=models.CASCADE)
    price_low = models.IntegerField(blank=True, null=True)
    price_middle = models.IntegerField(blank=True, null=True)
    price_high = models.IntegerField(blank=True, null=True)
    unical_feature = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    modifications_count = models.IntegerField(default=3)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    hidden = models.BooleanField(default=False)

    class Meta:
        db_table = 'weapon'


class KeyWord(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        db_table = 'key_words'


class WeaponKeyWord(models.Model):
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE)
    key_word = models.ForeignKey(KeyWord, on_delete=models.CASCADE)

    class Meta:
        db_table = 'weapon_key_words'
        unique_together = (('weapon', 'key_word'),)


class Modification(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'modification'


class DefaultWeaponModification(models.Model):
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE)
    modification = models.ForeignKey(Modification, on_delete=models.CASCADE)

    class Meta:
        db_table = 'default_weapon_modification'
        unique_together = (('weapon', 'modification'),)


# Патроны
class KindAmmo(models.Model):
    name = models.CharField(max_length=50)
    buy_count = models.IntegerField()

    class Meta:
        db_table = 'kind_ammo'


class WeaponAmmo(models.Model):
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE)
    kind_ammo = models.ForeignKey(KindAmmo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'weapon_ammo'
        unique_together = (('weapon', 'kind_ammo'),)


class TypeAmmo(models.Model):
    price = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    price_category = models.ForeignKey(PriceCategory, on_delete=models.CASCADE)

    class Meta:
        db_table = 'type_ammo'


class TypeKindAmmo(models.Model):
    kind_ammo = models.ForeignKey(KindAmmo, on_delete=models.CASCADE)
    type_ammo = models.ForeignKey(TypeAmmo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'type_kind_ammo'
        unique_together = (('kind_ammo', 'type_ammo'),)


# Программы
class ProgramType(models.Model):
    name = models.CharField(max_length=50)
    takes_up_space = models.IntegerField(default=1)

    class Meta:
        db_table = 'program_type'


class ProgramClass(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'program_class'


class Demon(models.Model):
    name_rus = models.CharField(max_length=50)
    name_eng = models.CharField(max_length=50)
    health = models.IntegerField()
    interface = models.IntegerField()
    network_actions = models.IntegerField()
    combat_number = models.IntegerField()
    price = models.IntegerField()
    price_category = models.ForeignKey(PriceCategory, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)

    class Meta:
        db_table = 'demon'


class Program(models.Model):
    name_rus = models.CharField(max_length=50)
    name_eng = models.CharField(max_length=50)
    program_type = models.ForeignKey(ProgramType, on_delete=models.CASCADE)
    program_class = models.ForeignKey(ProgramClass, on_delete=models.CASCADE)
    perception = models.IntegerField(blank=True, null=True)
    speed = models.IntegerField(blank=True, null=True)
    attack = models.IntegerField()
    defense = models.IntegerField()
    health = models.IntegerField()
    price = models.IntegerField()
    price_category = models.ForeignKey(PriceCategory, on_delete=models.CASCADE)
    effect = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)

    class Meta:
        db_table = 'program'


# Импланты
class LossHumanity(models.Model):
    name = models.CharField(max_length=50)
    average_value = models.IntegerField()
    formula = models.CharField(max_length=10)

    class Meta:
        db_table = 'loss_humanity'


class InstallationLocation(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()

    class Meta:
        db_table = 'installation_location'
        unique_together = (('name', 'price'),)  # Уникальность комбинации названия и цены


class Implant(models.Model):
    name_rus = models.CharField(max_length=50)
    name_eng = models.CharField(max_length=50)
    installation_location = models.ForeignKey(InstallationLocation, on_delete=models.CASCADE)
    loss_humanity = models.ForeignKey(LossHumanity, on_delete=models.CASCADE)
    occupies_slots = models.IntegerField(default=1)
    requirements = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    price_category = models.ForeignKey(PriceCategory, on_delete=models.CASCADE)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)

    class Meta:
        db_table = 'implants'


class Slot(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'slot'


class ImplantSlot(models.Model):
    implant = models.ForeignKey(Implant, on_delete=models.CASCADE)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)

    class Meta:
        db_table = 'implants_slot'
        unique_together = (('implant', 'slot'),)
