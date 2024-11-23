""" from django.db import models
from django.urls import reverse
from parler.models import TranslatableModel, TranslatedFields


class Category(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=200),
        slug=models.SlugField(max_length=200, unique=True),
    )

    class Meta:
        # ordering = ['name']
        # indexes = [
        #     models.Index(fields=['name']),
        # ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'shop:product_list_by_category', args=[self.slug]
        )


class Product(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=200),
        slug=models.SlugField(max_length=200),
        description=models.TextField(blank=True),
    )
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to='products/%Y/%m/%d',
        blank=True
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        # ordering = ['name']
        indexes = [
            # models.Index(fields=['id', 'slug']),
            # models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
 """

from django.db import models
from django.urls import reverse
from parler.models import TranslatableModel, TranslatedFields



class Category(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=200, verbose_name="Название"),
        slug=models.SlugField(max_length=200, unique=True, verbose_name="Слаг"),
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        # Возвращаем имя на текущем языке
        return self.safe_translation_getter('name', any_language=True)

    def get_absolute_url(self):
        # Генерация URL с использованием переведенного slug
        return reverse(
            'shop:product_list_by_category', args=[self.safe_translation_getter('slug', any_language=True)]
        )


class Product(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=200, verbose_name="Название"),
        slug=models.SlugField(max_length=200, verbose_name="Слаг"),
        description=models.TextField(blank=True, verbose_name="Описание"),
    )
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE,
        verbose_name="Категория"
    )
    image = models.ImageField(
        upload_to='products/%Y/%m/%d',
        blank=True,
        verbose_name="Изображение"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    available = models.BooleanField(default=True, verbose_name="Доступен")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated = models.DateTimeField(auto_now=True, verbose_name="Обновлен")

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        indexes = [
            models.Index(fields=['-created']),  # Индекс по дате создания
        ]

    def __str__(self):
        # Возвращаем имя на текущем языке
        return self.safe_translation_getter('name', any_language=True)

    def get_absolute_url(self):
        # Генерация URL с использованием переведенного slug
        return reverse('shop:product_detail', args=[self.id, self.safe_translation_getter('slug', any_language=True)])
