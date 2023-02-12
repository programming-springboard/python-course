# Домашне завдання

Результатом виконання домашнього завдання є написаний Python-скрипт.

## Завдання 1

Написати програму, що раз за разом буде запитувати в користувача ввести число,
строку або припинити введення значень. Кожне значення, що вводить користвач з
клавіатури повинно зберігатись в списку. Після того, як користувач обрав
опцію припинення вводу значень, необхідно вивести на екран суму всіх числових
значень, що він їх ввів, а також всі строкові значення однією строкою,
розмежовуючи їх пробілом.

Приклад консольного виводу програми наведено нижче (тут `>` - консольний вивід,
`<` - консольний ввод):

```
> What type of value do you want to input (1 - integer, 2 - string, 3 - stop input):
< 1
> Please, give me an integer value:
< 42

> What type of value do you want to input (1 - integer, 2 - string, 3 - stop input):
< 2
> Please, give me a string value:
< Hello,

> What type of value do you want to input (1 - integer, 2 - string, 3 - stop input):
< 2
> Plese, give me a stirng value:
< world!

> What type of value do you want to input (1 - integer, 2 - string, 3 - stop input):
< 1
> Please, give me an integer value:
< 4


> What type of value do you want to input (1 - integer, 2 - string, 3 - stop input):
< 3
> The sum of all integer values in list is: 46
> The join of all string values is: Hello, world!
```