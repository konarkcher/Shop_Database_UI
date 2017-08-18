from db.exception import DbErrorType as Dbt
from db.exception import ConstraintErrorType as Cet

APP_NAME = 'Shop UI'

# menubar labels
HELP = 'Помощь'

# menubar item labels
ABOUT_ITEM = 'О {}'.format(APP_NAME)

# toolbar item labels
SETTINGS = 'Настройки'
REFRESH = 'Обновить'

# dialog messages
ABOUT_DIAL = 'Программа для учёта товаров сферического магазина в вакууме'

# tab labels
SHOP_TAB = 'Магазин'
CART_TAB = 'Корзина'

# products column labels
PRODUCT_SOURCE = {'id': 'ID', 'name': 'Название товара', 'count': 'Количество',
                  'price': 'Цена', 'reserved': 'Зарезервировано'}

# customers column labels
CUSTOMER_SOURCE = {'id': 'ID', 'surname': 'Фамилия', 'name': 'Имя',
                   'phone': 'Телефон', 'address': 'Адрес'}

# deals column labels
DEALS_SOURCE = {'id': 'ID', 'customer_id': 'ID покупателя',
                'dttm': 'Дата и время'}

CUSTOMER_NOT_CHOSEN = 'Покупатель не выбран'

# button labels
ADD_PRODUCT = 'Добавить наименование'
DELETE_BUTTON = 'Удалить'
TO_CART_BUTTON = 'Добавить в корзину'
ADD_CUSTOMER = 'Добавить покупателя'
REMOVE_PRODUCT = 'Убрать товар'

CHOOSE_CUSTOMER_BTN = 'Выбрать покупателя'
CHANGE_CUSTOMER_BTN = 'Сменить покупателя'
PLACE_ORDER_BTN = 'Оформить заказ'
CLEAR_ORDER_BTN = 'Сбросить заказ'

# set db labels
SET_DB = 'Выбор базы данных'

SQLITE_DB = 'Sqlite3'
FILE = 'Файл:'

# .buttons
ACCEPT = 'Принять'
CANCEL = 'Отмена'

# customer choice
CHOOSE_CUSTOMER_TITLE = 'Выбор покупателя'
CHOOSE = 'Выбрать'

SUM = 'Сумма: '

# check stuff
CUSTOMER_TITLE = 'Покупатель'

# empty ObjectListView labels
PRODUCT_LC = 'Товаров нет'
CUSTOMER_LC = 'Покупателей пока нет'
ORDER_LC = 'Корзина пуста'

# info messages
ERROR = 'Ошибка'
LACK = 'Недостаточно единиц товара'
NO_PRODUCTS = 'Товары не выбраны'

# add dialog titles
NEW_PRODUCT = 'Новый товар'
NEW_CUSTOMER = 'Новый покупатель'

# dialog button
OK = 'ОК'

# Exception messages
DE = {Dbt.UNDEFINED_ERROR: 'Неизвестная ошибка',
      Dbt.ALREADY_EXISTS: 'Таблица уже создана',
      Dbt.NO_SUCH_TABLE: 'Таблица не существует'}

CE = {Cet.INCORRECT_VALUE: 'Некорректное значение',
      Cet.TOO_LONG: 'Превышено ограничение по длине',
      Cet.NOT_UNIQUE: 'Такое значение уже существует'}

UPDATE_RESERVED = 'Невозможно изменить зарезервированный товар'

#validation regulars

PRODUCT_REGX = { 
    'name': '[a-zA-Zа-яА-Я]{1,30}$',
    'price': '[0-9]{1,12}$',
    'count': '[0-9]{1,12}$'
}

CUSTOMER_REGX = { 
    'surname': '[a-zA-Zа-яА-Я]{1,30}$',
    'name': '[a-zA-Zа-яА-Я]{1,30}$',
    'phone': '[0-9]{1,12}$',
    'address': '[a-zA-Zа-яА-Я0-9\,\.\'\"\: *@]{1,300}$'
}