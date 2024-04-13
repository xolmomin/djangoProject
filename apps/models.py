from django.db.models import Model, FloatField, TextField, CharField
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields


class Product(TranslatableModel):
    translations = TranslatedFields(
        name=CharField(verbose_name=_('name'), max_length=255),
        description=TextField(verbose_name=_('description'), null=True, blank=True)
    )
    price = FloatField(verbose_name=_('price'), default=0)

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')
