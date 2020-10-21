from hashlib import md5

from django.db import models
from django.contrib import admin
from django.db.models import F
from django.utils.safestring import mark_safe
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager


class UsersManager(BaseUserManager):
    """ Менеджер пользователя """
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Создает и сохраняет пользователя с введенным им email и паролем.
        """
        if not email:
            raise ValueError('email должен быть указан')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.reset = str(md5(f"{email}{password}".encode()).hexdigest())
        temp = Users.objects.filter(email=email).values('email')
        if temp:
            return None
        else:
            user.save(using=self._db)
            return user

    def create_user(self, email, password=None, **extra_fields):
        """ Создает обычного пользователя"""
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """ Создает суперпользователя"""
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        return self._create_user(email, password, **extra_fields)


class Users(AbstractBaseUser, PermissionsMixin):
    """ Модель пользователя """
    password = models.TextField('Пароль')
    email = models.EmailField('Почта', unique=True)
    phone = models.TextField('Телефон', default=None, null=True, max_length=10)
    reset = models.TextField('Ссылка восстановления', default=None)
    ref = models.IntegerField('Referral', default=0)
    vk = models.TextField('ВКонтакте ID', default=None, null=True)
    inst = models.TextField('Instagram ID', default=None, null=True)
    is_staff = models.BooleanField('is_staff', default=False)

    objects = UsersManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Items(models.Model):
    """ Электрокары """
    name = models.TextField('Наименование', default=None)
    age = models.TextField('Возраст', default='')
    tech = models.TextField('Тех.характеристики', default=None)
    weight = models.IntegerField('Вес', default=0)

    def __str__(self):
        return self.name

    def image(self):
        img = self.item_img.all()
        if len(img) == 0:
            return '-'
        else:
            return self.item_img.all()[0].image.url

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


def content_file_name(instance, filename):
    return f'{instance.name}'.join(['items/img/', f'/{filename}'])


class Images(models.Model):
    """ Изображения электрокаров """
    name = models.ForeignKey(Items, related_name='item_img', on_delete=models.CASCADE, verbose_name='Наименование')
    image = models.ImageField('Картинка', upload_to=content_file_name)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class City(models.Model):
    """ Города, в которых происходят продажи """
    name = models.CharField('Город', max_length=200, default=None)
    phone = models.TextField('Телефон', default=None, null=True)
    address = models.TextField('Адрес', default=None, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class CityPrice(models.Model):
    """ Наличие электрокаров по городам с указнием цены, количества, скидки """
    city = models.ForeignKey(City, related_name='town', on_delete=models.CASCADE, verbose_name='Город заказа')
    item = models.ForeignKey(Items, related_name='city_items', on_delete=models.CASCADE, verbose_name='Товар')
    count = models.IntegerField('Количество', default=0)
    price = models.FloatField('Цена', default=0)
    sale = models.IntegerField('Скидка', default=0)

    def __str__(self):
        return self.item.name

    def get_sale_price(self):
        return self.price - (self.price * self.sale / 100)

    class Meta:
        verbose_name = 'Товар по городам'
        verbose_name_plural = 'Товары по городам'


class Orders(models.Model):
    """ Заказы """
    phone = models.TextField('Телефон', default=None)
    email = models.EmailField('E-mail', default=None)
    pay = models.TextField('Оплата', choices=[('online', 'Онлайн'), ('offline', 'При получении')], default='Онлайн')
    city = models.CharField('Город', max_length=200, default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    status = models.TextField('Статус',
                              choices=[('В работе', 'В работе'), ('Ждем оплаты', 'Ждем оплаты'), ('Оплачен', 'Оплачен'),
                                       ('Завершен', 'Завершен')], default='В работе')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ №{}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    get_total_cost.short_description = 'Сумма Заказа'


class OrderItem(models.Model):
    """ Товары в заказе """
    order = models.ForeignKey(Orders, related_name='items', on_delete=models.CASCADE, verbose_name='Номер заказа')
    items = models.ForeignKey(CityPrice, related_name='order_items', on_delete=models.CASCADE, verbose_name='Товар')

    def __str__(self):
        return '{}'.format(self.id)

    def image(self):
        img = self.items.item.item_img.all()
        if len(img) == 0:
            return '-'
        else:
            return mark_safe(f'<img src={self.items.item.item_img.all()[0].image.url} width="100" height="80">')

    image.short_description = 'Изображение'

    def get_cost(self):
        return self.items.price

    get_cost.short_description = 'Цена'

    class Meta:
        verbose_name = 'Товар в Заказе'
        verbose_name_plural = 'Товары в Заказе'


class Call(models.Model):
    """ Обратный звонок от покупателя """
    item = models.TextField('Товар', default=None)
    phone = models.TextField('Телефон', default=None)
    date = models.DateTimeField('Дата', auto_now=True)
    status = models.TextField('Статус', choices=[('Получен', 'Получен'), ('Просмотрен', 'Просмотрен'),
                                                 ('Обработан', 'Обработан')], default='Получен')

    class Meta:
        verbose_name = 'Звонок'
        verbose_name_plural = 'Звонки'


class ImagesinLine(admin.StackedInline):
    """ Добавление изображения """
    model = Images
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="80"')

    get_image.short_description = 'Изображение'


class OrderItemInline(admin.TabularInline):
    """ Отображение содердимого заказа """
    model = OrderItem
    extra = 1
    readonly_fields = ("image", "get_cost",)


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('email', 'password', 'reset', 'ref', 'vk', 'inst', 'is_staff')


@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'tech', 'weight')
    inlines = [ImagesinLine]


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'get_image')
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="80"')

    get_image.short_description = 'Изображение'


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'address')


@admin.register(CityPrice)
class CityPriceAdmin(admin.ModelAdmin):
    list_display = ('city', 'item', 'count', 'price', 'sale', 'get_sale_price')


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):

    def cancel_order(self, request, queryset):
        order_number = int(str(queryset[0])[str(queryset[0]).index('№')+1:])
        order_obj = Orders.objects.filter(id=order_number)
        orders = OrderItem.objects.filter(order_id=order_number).values('items__item__name', 'items__city__name')
        for order in orders:
            print(order)
            CityPrice.objects.filter(city__name=order['items__city__name'],
                                     item__name=order['items__item__name']).values('count').update(count=F('count') + 1)
        order_obj.delete()

    cancel_order.short_description = "Отменить заказ"

    ordering = ['id']
    list_display = ('__str__', 'city', 'phone', 'email', 'created', 'updated', 'get_total_cost', 'pay', 'paid')
    inlines = [OrderItemInline]
    actions = [cancel_order]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'items', 'get_cost')


@admin.register(Call)
class CallAdmin(admin.ModelAdmin):
    list_display = ('item', 'phone', 'date', 'status')


admin.site.site_header = "Happy Family"
admin.site.site_title = "Happy Family Admin"
admin.site.index_title = "Welcome to Happy Family Admin Tools"
