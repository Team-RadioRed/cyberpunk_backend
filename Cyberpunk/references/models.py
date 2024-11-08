from django.db import models


class PriceCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'price_category'


class Source(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'source'
        unique_together = (('name', 'code'),)


class ItemType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'item_type'


class KeyWords(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'key_words'


class Modification(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'modification'


class TypeAmmo(models.Model):
    price = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    price_category = models.ForeignKey(PriceCategory, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'type_ammo'


class KindAmmo(models.Model):
    name = models.CharField(max_length=50)
    buy_count = models.IntegerField()  # NOT NULL, обязательное поле

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'kind_ammo'


class TypeKindAmmo(models.Model):
    kind_ammo = models.ForeignKey(KindAmmo, on_delete=models.DO_NOTHING)
    type_ammo = models.ForeignKey(TypeAmmo, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'type_kind_ammo'


class Weapon(models.Model):
    name_rus = models.CharField(max_length=50)
    name_eng = models.CharField(max_length=50)
    is_exotic = models.BooleanField(default=False)
    type = models.ForeignKey(ItemType, on_delete=models.DO_NOTHING)
    skill_need = models.TextField()
    damage = models.IntegerField()
    magazine = models.IntegerField()
    rate_of_fire = models.IntegerField(default=2)
    grab_type = models.IntegerField(default=1)
    price_category = models.ForeignKey(PriceCategory, on_delete=models.DO_NOTHING)
    price_low = models.IntegerField(blank=True, null=True)
    price_middle = models.IntegerField(blank=True, null=True)
    price_high = models.IntegerField(blank=True, null=True)
    unical_feature = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    modifications_count = models.IntegerField()
    source = models.ForeignKey(Source, on_delete=models.DO_NOTHING)
    hidden = models.BooleanField(default=False)


    def __str__(self):
        return self.name_rus

    class Meta:
        db_table = 'weapon'


class WeaponKeyWords(models.Model):
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE)
    key_words = models.ForeignKey(KeyWords, on_delete=models.CASCADE)

    class Meta:
        db_table = 'weapon_key_words'


class WeaponAmmo(models.Model):
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE)
    kind_ammo = models.ForeignKey(KindAmmo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'weapon_ammo'