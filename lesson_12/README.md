# Текст лекції

## Принципи SOLID

Принципи SOLID - це набір принципів, що виникли в області об'єктно-орієнтованого програмування і розробки програмного забезпечення. Їх розробив Роберт Мартін (Robert C. Martin), відомий як "Дядько Боб" (Uncle Bob), який є видатним програмістом, автором та консультантом в галузі розробки ПЗ.

Роберт Мартін вперше представив принципи SOLID у своїй книзі "Agile Software Development, Principles, Patterns, and Practices" (Гнучка розробка програмного забезпечення: принципи, шаблони та практики), яка була випущена у 2002 році. Він використав аббревіатуру SOLID для опису цих принципів, де кожна літера відповідає окремому принципу.

Використання принципів SOLID допомагає розробникам створювати код, який є більш розширюваним, змінюваним та тестованим. Вони сприяють зменшенню залежностей, полегшують підтримку та розширення кодової бази.

### Single Responsibility Principle

Single Responsibility Principle (SRP) - Принцип єдиного обов'язку. Кожен клас повинен мати лише одну причину для зміни і повинен бути відповідальним лише за одну справу.

Приклад порушення принципу єдиного обов'язку (Single Responsibility Principle, SRP) в Python можна продемонструвати на наступному коді:

```python
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def save_to_database(self):
        # Код для збереження користувача у базу даних
    
    def send_email(self, message):
        # Код для відправки електронного листа користувачу
```

У цьому прикладі клас `User` виконує дві різні функції: зберігання користувача 
у базу даних та відправку електронного листа. Це порушує SRP, оскільки клас 
має більше однієї причини для зміни. Якщо, наприклад, зміниться механізм 
збереження користувачів у базу даних, це потенційно вплине і на метод 
`send_email()`, який не має прямого відношення до збереження користувача.

Кращим підходом було б розділити ці дві функціональності на окремі класи:

```python
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
class UserRepository:
    def save_to_database(self, user):
        # Код для збереження користувача у базу даних

class EmailService:
    def send_email(self, user, message):
        # Код для відправки електронного листа користувачу
```

В цьому випадку клас `User` відповідає лише за представлення користувача, а 
`UserRepository` та `EmailService` відповідають відповідно за збереження 
користувача у базу даних та відправку електронного листа. Кожен клас має 
свій власний окремий обов'язок, що дозволяє змінювати їх незалежно один від 
одного без впливу на інші частини коду.

### Open-Close Principle

Принцип відкритості/закритості (Open/Closed Principle, OCP): Програмні 
сутності, такі як класи, модулі або функції, повинні бути відкритими для 
розширення, але закритими для модифікації. Це означає, що зміна поведінки 
сутностей повинна здійснюватись через додавання нового коду, а не зміною вже 
існуючого.

Ось приклад порушення та відповідного дотримання принципу відкритості/закритості 
(Open-Closed Principle, OCP) в Python.

```python
class Shape:
    def __init__(self, type):
        self.type = type
    
    def area(self):
        if self.type == "circle":
            radius = self.get_radius()
            return 3.14 * radius ** 2
        elif self.type == "rectangle":
            length = self.get_length()
            width = self.get_width()
            return length * width
        # Багато інших умов для різних типів фігур
    
    def get_radius(self):
        # Логіка отримання радіусу
    
    def get_length(self):
        # Логіка отримання довжини
    
    def get_width(self):
        # Логіка отримання ширини
```

У цьому прикладі клас `Shape` має метод `area()`, який розраховує площу для 
різних типів фігур, таких як коло і прямокутник. Однак, при додаванні нового 
типу фігури, як-от трикутник, потрібно змінювати вже існуючий код класу `Shape`. 
Це порушує OCP, оскільки клас має бути закритим для модифікацій, а 
відкритим для розширення.

Кращим підходом було б використовувати поліморфізм та розділити функціональність на окремі класи:

```python
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
```

В цьому випадку ми маємо базовий клас `Shape`, який має метод `area()`. Класи 
`Circle` та `Rectangle` успадковують від `Shape` та перевизначають метод `area()` 
відповідно для розрахунку площі конкретних фігур. Тепер, для додавання нового 
типу фігури, просто створюється новий клас, який успадковує від `Shape` і 
перевизначає метод `area()`, не змінюючи вже існуючий код.

### Liskov Substitution Principle

Принцип підстановки Барбари Лісков (Liskov Substitution Principle, LSP): Об'єкти в програмі повинні бути замінювані на екземпляри своїх підтипів без зміни правильності програми. Це означає, що класи-спадкоємці повинні мати можливість замінити базовий клас без порушення контрактів та очікуваної поведінки.

Ось приклад порушення та відповідного дотримання принципу підстановки Барбари Лісков (Liskov Substitution Principle, LSP) в Python.

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height

class Square(Rectangle):
    def set_width(self, width):
        self.width = width
        self.height = width
    
    def set_height(self, height):
        self.width = height
        self.height = height
```

У цьому прикладі клас `Square` успадковує від класу `Rectangle`, оскільки 
квадрат є особливим випадком прямокутника, де ширина і висота однакові. 
Проте, в перевизначених методах `set_width()` та `set_height()` в класі `Square` 
змінюється і поведінка базового класу `Rectangle`. Внаслідок цього, код, 
який очікує роботи з об'єктами класу `Rectangle`, може вести себе неочікувано, 
коли використовується об'єкт класу `Square`.

Приклад слідування LSP:

```python
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def get_area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length
    
    def get_area(self):
        return self.side_length ** 2
```

У цьому випадку базовий клас `Shape` має метод `get_area()`, який є спільним 
для всіх підкласів. Класи `Rectangle` та `Square` успадковують від `Shape` і 
перевизначають метод `get_area()` відповідно для розрахунку площі. 
Таким чином, клас Square не порушує LSP, оскільки може замінити клас `Rectangle`
в будь-якому контексті, де очікується об'єкт типу `Shape`, не порушуючи 
контрактів та очікуваної поведінки.

### Interface Segregation Principle

Принцип розділення інтерфейсу (Interface Segregation Principle, ISP): Клієнти не повинні залежати від інтерфейсів, які вони не використовують. Це означає, що клієнтам слід надавати тільки необхідний функціонал через спеціалізовані інтерфейси, а не через великі загальні інтерфейси.

Ось приклад порушення та відповідного дотримання принципу розділення інтерфейсу (Interface Segregation Principle, ISP) в Python.

```python
from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass
   
    @abstractmethod 
    def scan(self, document):
        pass
   
    @abstractmethod 
    def fax(self, document):
        pass
```

У цьому прикладі клас `Printer` визначає загальний інтерфейс для друку, 
сканування та факсування документів. Однак, не всі пристрої для друку можуть 
підтримувати функції сканування та факсування. Таке розширення інтерфейсу 
створює непотрібну залежність для класів, які використовують інтерфейс `Printer`. 
Крім того, якщо додавати нові функціональності до інтерфейсу, всі класи, що 
його реалізують, також будуть змушені реалізовувати ці функції, навіть якщо 
вони не потрібні.

Приклад слідування ISP:

```python
from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass

class FaxMachine(ABC):
    @abstractmethod
    def fax(self, document):
        pass
```

У цьому прикладі функції друку, сканування та факсування розділені на окремі 
інтерфейси: `Printer`, `Scanner` та `FaxMachine`. Класи, що використовують ці 
функціональності, можуть залежно від потреби реалізувати лише необхідні 
інтерфейси. Наприклад, якщо пристрій підтримує тільки друкування та сканування, 
клас може реалізувати інтерфейси `Printer` і `Scanner`, залишивши без уваги 
інтерфейс `FaxMachine`. Це дозволяє зберігати інтерфейси маленькими, 
спрощує розробку, зменшує залежності і полегшує тестування коду.

### Dependency Inversion Principle

Принцип інверсії залежностей (Dependency Inversion Principle, DIP): Класи повинні залежати від абстракцій, а не від конкретних реалізацій. Це означає, що взаємозв'язки між класами повинні базуватись на абстракціях (інтерфейсах або абстрактних класах), а не на конкретних реалізаціях.

Ось приклад порушення та відповідного дотримання принципу інверсії залежностей (Dependency Inversion Principle, DIP) в Python.

```python

class MySQLDatabase:
    def connect(self):
    # Логіка підключення до MySQL бази даних

    def execute_query(self, query):
# Логіка виконання SQL-запиту

class UserDAO:
    def __init__(self):
        self.db = MySQLDatabase()

    def save_user(self, user):
# Логіка збереження користувача в базу даних
```

У цьому прикладі клас `UserDAO` прямо залежить від класу `MySQLDatabase`, який 
використовується для збереження користувачів у базі даних. Такий підхід 
порушує DIP, оскільки високорівневий модуль (`UserDAO`) залежить від низькорівневого 
модуля (`MySQLDatabase`). Зміна бази даних на іншу систему вимагатиме змін в коді `UserDAO`.

Приклад слідування DIP:

```python
from abc import ABc, abstractmethod


class DatabaseInterface(ABC):
    @abstractmethod
    def connect(self):
        pass
   
    @abstractmethod 
    def execute_query(self, query):
        pass

class MySQLDatabase(DatabaseInterface):
    def connect(self):
        # Логіка підключення до MySQL бази даних

    def execute_query(self, query):
        # Логіка виконання SQL-запиту

class UserDAO:
    def __init__(self, db):
        self.db = db
    
    def save_user(self, user):
        # Логіка збереження користувача в базу даних
```

У цьому прикладі ми визначаємо інтерфейс `DatabaseInterface`, який описує методи 
`connect()` та `execute_query()`. Клас `MySQLDatabase` реалізує цей інтерфейс. 
Клас `UserDAO` приймає залежність `DatabaseInterface` через конструктор, а не 
створює об'єкт `MySQLDatabase` в середині свого коду. Це дозволяє використовувати 
будь-яку реалізацію `DatabaseInterface` (наприклад, `SQLite` або `PostgreSQL`) 
без впливу на `UserDAO`. Залежність від інтерфейсу дозволяє легко виконувати 
заміну реалізацій, розширювати функціональність та полегшує тестування.

## Домашнє завдання

Напиши програму для управління бібліотекою з використанням принципів SOLID. В системі повинні бути книги, користувачі, а також можливість видачі та повернення книг.

Твоє завдання полягає в наступному:

1. Розглянь, які класи можуть бути необхідні для втілення системи управління бібліотекою.
2. Застосуй принципи SOLID (SRP, OCP, LSP, ISP та DIP) при проектуванні цих класів та їх взаємодії.
3. Пам'ятай про правильну організацію відповідальностей між класами та інтерфейсами, так щоб кожен клас був відповідальний лише за одну справу і був залежним від абстракцій, а не від конкретних реалізацій.
4. Напиши код програми, використовуючи обрані тобою принципи SOLID. Забезпеч перевірку та демонстрацію функціональності управління книгами та користувачами, включаючи видачу та повернення книг.

Ось список операцій, які система управління бібліотекою повинна підтримувати:

1. Додавання нової книги до бібліотеки.
2. Видалення книги з бібліотеки.
3. Видача книги користувачу.
4. Повернення книги користувачем.
5. Перегляд списку всіх книг в бібліотеці.
6. Перегляд доступних книг.
7. Перегляд списку користувачів бібліотеки.
8. Перегляд списку книг, вище встановленого ліміту на видачу.
9. Пошук книги за назвою, автором або іншими критеріями.
10. Перегляд історії видач та повернень книг.
11. Блокування користувача за несплату штрафів або інші порушення правил бібліотеки.
