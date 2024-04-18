from django.db.models import Model, FloatField, TextField, CharField, ForeignKey, CASCADE
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields


class TgUser(Model):
    username = CharField(unique=True, max_length=255, null=True, blank=True)
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255, null=True, blank=True)


class Category(Model):
    name = CharField(_("name"), max_length=255)


class Product(TranslatableModel):
    translations = TranslatedFields(
        name=CharField(verbose_name=_('name'), max_length=255),
        description=TextField(verbose_name=_('description'), null=True, blank=True)
    )
    price = FloatField(verbose_name=_('price'), default=0)
    category = ForeignKey('apps.Category', verbose_name=_('category'), on_delete=CASCADE)

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')
