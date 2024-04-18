from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField

from apps.models import Product


class ProductTranslatableModelSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Product)

    class Meta:
        model = Product
        fields = 'id', 'price', 'translations'

    # def to_representation(self, instance):
    #     repr = super().to_representation(instance)
    #     lang_code = self.context['request'].LANGUAGE_CODE
    #     translations = repr.pop('translations')
    #     repr.update(translations.get(lang_code, {}))
    #     return repr
