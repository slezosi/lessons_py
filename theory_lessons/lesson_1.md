<h1>Lesson.1 Знакомство с Python</h1>
<h2>Краткая историческая справка</h2>
<p>Язык программирования Python был создан к 1991 году голландцем Гвидо ван Россумом.
  
Свое имя – Пайтон (или Питон) – получил от названия телесериала, а не пресмыкающегося.
После того, как Россум разработал язык, он выложил его в Интернет, где сообщество программистов присоединилось к его улучшению.

Python активно развивается в настоящее время. Часто выходят новые версии. Существуют две поддерживаемые ветки: Python 2.x и Python 3.x. Здесь английской буквой "x" обозначается конкретный релиз. Между вторым и третьим Питоном есть небольшая разница. В данном курсе за основу берется Python 3.x.

Официальный сайт поддержки языка 
<https://www.python.org>

**Основные особенности языка**

Python – интерпретируемый язык программирования. Это значит, что исходный код частями преобразуется в машинный в процессе его чтения специальной программой – интерпретатором.

Python характеризуется ясным синтаксисом. Читать код на нем легче, чем на других языках программирования, т. к. в Питоне мало используются такие вспомогательные синтаксические элементы как скобки, точки с запятыми. С другой стороны, **правила языка заставляют программистов делать отступы** для обозначения вложенных конструкций. Понятно, что хорошо оформленный текст с малым количеством отвлекающих элементов читать и понимать легче.

Python – это полноценный во многом универсальный язык программирования, используемый в различных сферах. Основная, но не единственная, поддерживаемая им парадигма, – объектно-ориентированное программирование. Однако в данном курсе мы только упомянем об объектах, а будем изучать структурное программирование, так как оно является базой. Без знания основных типов данных, ветвлений, циклов, функций нет смысла изучать более сложные парадигмы, т. к. в них все это используется.
Интерпретаторы Python распространяется свободно на основании лицензии подобной GNU General Public License.

**Дзен Питона**

Если интерпретатору Питона дать команду import this ("импортируй это" здесь видимо следует понимать как "импортируй самого себя"), то выведется так называемый "Дзен Питона", иллюстрирующий идеологию и особенности данного языка. Понимание смысла этих постулатов в приложении к программированию придет тогда, когда вы освоите язык в полной мере и приобретете опыт практического программирования.

**Как писать программы на Python**

Необходимо установить последнюю версию python, а так же удобную для вас среду разработки(PyCharm, sublime text, visual studio code и т.п.)

**Типы данных. Переменные**

При знакомстве с языком программирования Python мы столкнемся с тремя типами данных:
•	целые числа (тип int) – положительные и отрицательные целые числа, а также 0 (например, 4, 687, -45, 0).

•	числа с плавающей точкой (тип float) – дробные, они же вещественные, числа (например, 1.45, -3.789654, 0.00453). Примечание: для разделения целой и дробной частей здесь используется точка, а не запятая.

•	строки (тип str) — набор символов, заключенных в кавычки (например, "ball", "What is your name?", 'dkfjUUv', '6589'). Примечание: кавычки в Python могут быть одинарными или двойными; одиночный символ в кавычках также является строкой, отдельного символьного типа в Питоне нет.

**Операции в программировании**

*Операция* – это выполнение каких-либо действий над данными, которые в данном случае именуют операндами. Само действие выполняет оператор – специальный инструмент. Если бы вы выполняли операцию постройки стола, то вашими операндами были бы доска и гвоздь, а оператором – молоток.

Так в математике и программировании символ плюса является оператором операции сложения по отношению к числам. В случае строк этот же оператор выполняет операцию *конкатенации*, т. е. соединения.

<code>>> 10.25 + 98.36
108.61</code>

*конкатенация*

<code>>>> 'Hello' + 'World'
'HelloWorld'
</code>

Здесь следует для себя отметить, что то, что делает оператор в операции, зависит не только от него, но и от типов данных, которыми он оперирует. Молоток в случае нападения на вас крокодила перестанет играть роль строительного инструмента. Однако в большинстве случаев операторы не универсальны. Например, знак плюса неприменим, если операндами являются, с одной стороны, число, а с другой – строка.

<code>>>> 1 + 'a'
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 
'int' and 'str'
</code>

Здесь в строке <code>TypeError: unsupported operand type(s) for +: 'int' and 'str'</code> интерпретатор сообщает, что произошла ошибка типа – неподдерживаемый операнд для типов int и str.

**Изменение типов данных**

Приведенную выше операцию все-таки можно выполнить, если превратить число 1 в строку "1". Для изменения одних типов данных в другие в языке Python предусмотрен ряд встроенных в него функций (что такое функция в принципе, вы узнаете в других уроках). Поскольку мы пока работаем только с тремя типами (int, float и str), то рассмотрим только соответствующие им функции: int(), float(), str().

<code>
>>> str(1) + 'a'
'1a'
>>> int('3') + 4
7
>>> float('3.2') + int('2')
5.2
>>> str(4) + str(1.2)
'41.2'
</code>

Эти функции преобразуют то, что помещается в их скобки соответственно в целое число, вещественное число или строку. Однако надо понимать, что преобразовать можно не все:

<code>
>>> int('hi')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with 
base 10: 'hi'
</code>

Здесь возникла ошибка значения (ValueError), так как передан литерал (в данном случае строка с буквенными символами), который нельзя преобразовать к числу с основанием 10. Однако функция int() не такая простая:

<code>
>>> int('101', 2)
5
>>> int('F', 16)
15
</code>

Если вы знаете о различных системах счисления, то поймете, что здесь произошло.

Обратите внимание еще на одно. Данные могут называться значениями, а также *литералами*. Эти три понятия ("данные", "значение", "литерал") не обозначают одно и то же, но близки и нередко употребляются как синонимы. Чтобы понять различие между ними, места их употребления, надо изучить программирование глубже.

**Переменные**

Данные хранятся в ячейках памяти компьютера. Когда мы вводим число, оно помещается в какую-то ячейку памяти. Но как потом узнать, куда именно? Как впоследствии обращаться к этим данными? Нужно как-то запомнить, пометить соответствующую ячейку.
Раньше, при написании программ на машинном языке, обращение к ячейкам памяти осуществляли с помощью указания их регистров, т. е. конкретно сообщали, куда положить данные и откуда их взять. Однако с появлением ассемблеров при обращении к данным стали использовать словесные переменные, что куда удобней для человека.

Механизм связи между переменными и данными может различаться в зависимости от языка программирования и типов данных. Пока достаточно запомнить, что в программе данные связываются с каким-либо именем и в дальнейшем обращение к ним возможно по этому имени-переменной.

Слово "переменная" обозначает, что сущность может меняться, она непостоянна. Действительно, вы увидите это в дальнейшем, одна и та же переменная может быть связана сначала с одними данными, а потом – с другими. То есть ее значение может меняться, она переменчива.

В программе на языке Python, как и на большинстве других языков, связь между данными и переменными устанавливается с помощью знака =. Такая операция называется присваивание (также говорят "присвоение"). Например, выражение sq = 4 означает, что на объект, представляющий собой число 4, находящееся в определенной области памяти, теперь ссылается переменная sq, и обращаться к этому объекту следует по имени sq.

*Имена переменных могут быть любыми. Однако есть несколько общих **правил** их написания:*

1.	Желательно давать переменным осмысленные имена, говорящие о назначении данных, на которые они ссылаются.
2.	Имя переменной не должно совпадать с командами языка (зарезервированными ключевыми словами).
3.	Имя переменной должно начинаться с буквы или символа подчеркивания (_), но не с цифры.
4.	Имя переменной не должно содержать пробелы.

Чтобы узнать значение, на которое ссылается переменная, находясь в режиме интерпретатора, достаточно ее вызвать, т. е. написать имя и нажать Enter.

<code>
>>> sq = 4
>>> sq
4
</code>

Вот более сложный пример работы с переменными в интерактивном режиме:

<code>
>>> apples = 100
>>> eat_day = 5
>>> day = 7
>>> apples = apples - eat_day * day
>>> apples
65
</code>

Здесь фигурируют три переменные: apples, eat_day и day. Каждой из них присваивается свое значение. Выражение <code>apples = apples - eat_day * day</code> сложное. Сначала выполняется подвыражение, стоящее справа от знака равенства. После этого его результат присваивается переменной apples, в результате чего ее старое значение (100) теряется. В подвыражении <code>apples - eat_day * day </code> вместо имен переменных на самом деле используются их значения, т. е. числа 100, 5 и 7.

<!-- LOGIN

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Авторизация</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f0f2f5; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .card { background: #fff; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); width: 320px; }
        h2 { text-align: center; color: #333; }
        input { width: 100%; padding: 10px; margin: 8px 0; border: 1px solid #ccc; border-radius: 5px; box-sizing: border-box; }
        button { width: 100%; padding: 10px; background: #4a90e2; color: #fff; border: none; border-radius: 5px; cursor: pointer; margin-top: 10px; }
        button:hover { background: #357ab8; }
        .link { text-align: center; margin-top: 15px; font-size: 14px; }
        .link a { color: #4a90e2; text-decoration: none; }
    </style>
</head>
<body>
    <div class="card">
        <h2>Вход в систему</h2>
        <form action="requests.html" method="get">
            <input type="text" placeholder="Логин" required>
            <input type="password" placeholder="Пароль" required>
            <button type="submit">Войти</button>
        </form>
        <div class="link">Нет аккаунта? <a href="register.html">Зарегистрироваться</a></div>
    </div>
</body>
</html> 

SIGNUP

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Регистрация</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f0f2f5; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }
        .card { background: #fff; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); width: 340px; }
        h2 { text-align: center; color: #333; }
        input { width: 100%; padding: 10px; margin: 8px 0; border: 1px solid #ccc; border-radius: 5px; box-sizing: border-box; }
        button { width: 100%; padding: 10px; background: #4a90e2; color: #fff; border: none; border-radius: 5px; cursor: pointer; margin-top: 10px; }
        button:hover { background: #357ab8; }
        .link { text-align: center; margin-top: 15px; font-size: 14px; }
        .link a { color: #4a90e2; text-decoration: none; }
    </style>
</head>
<body>
    <div class="card">
        <h2>Регистрация</h2>
        <form action="login.html" method="get">
            <input type="text" placeholder="ФИО" required>
            <input type="text" placeholder="Логин" required>
            <input type="email" placeholder="Email" required>
            <input type="tel" placeholder="Телефон" required>
            <input type="password" placeholder="Пароль" required>
            <input type="password" placeholder="Повторите пароль" required>
            <button type="submit">Создать профиль</button>
        </form>
        <div class="link">Уже есть аккаунт? <a href="login.html">Войти</a></div>
    </div>
</body>
</html>

APPLICATIONS

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Мои заявки</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f0f2f5; margin: 0; padding: 20px; }
        .header { max-width: 900px; margin: 0 auto 20px; display: flex; justify-content: space-between; align-items: center; background: #fff; padding: 15px 25px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        .header h1 { font-size: 20px; margin: 0; color: #333; }
        nav a { margin-left: 15px; color: #4a90e2; text-decoration: none; font-size: 14px; }
        nav a:hover { text-decoration: underline; }
        .container { max-width: 900px; margin: 0 auto; }
        .request { background: #fff; padding: 20px; border-radius: 10px; margin-bottom: 15px; box-shadow: 0 2px 10px rgba(0,0,0,0.08); }
        .request h3 { margin-top: 0; color: #333; }
        .status { display: inline-block; padding: 4px 10px; border-radius: 12px; font-size: 12px; color: #fff; }
        .status.new { background: #f39c12; }
        .status.done { background: #27ae60; }
        .status.rejected { background: #e74c3c; }
        textarea { width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 5px; box-sizing: border-box; margin-top: 10px; font-family: inherit; }
        button { padding: 8px 16px; background: #4a90e2; color: #fff; border: none; border-radius: 5px; cursor: pointer; margin-top: 10px; }
        button:hover { background: #357ab8; }
    </style>
</head>
<body>
    <div class="header">
        <h1>Мои заявки</h1>
        <nav>
            <a href="create-request.html">Создать заявку</a>
            <a href="login.html">Выйти</a>
        </nav>
    </div>

    <div class="container">
        <div class="request">
            <h3>Заявка №1 — Организация конференции</h3>
            <p>Дата: 15.05.2024</p>
            <p>Статус: <span class="status done">Проведено</span></p>
            <label><b>Оставить отзыв:</b></label>
            <textarea rows="3" placeholder="Ваш отзыв о мероприятии..."></textarea>
            <button>Отправить отзыв</button>
        </div>

        <div class="request">
            <h3>Заявка №2 — Проведение семинара</h3>
            <p>Дата: 20.06.2024</p>
            <p>Статус: <span class="status new">В обработке</span></p>
        </div>

        <div class="request">
            <h3>Заявка №3 — Круглый стол</h3>
            <p>Дата: 10.04.2024</p>
            <p>Статус: <span class="status rejected">Отклонено</span></p>
        </div>
    </div>
</body>
</html>

CREATE APPL

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Создание заявки</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f0f2f5; margin: 0; padding: 20px; }
        .header { max-width: 700px; margin: 0 auto 20px; display: flex; justify-content: space-between; align-items: center; background: #fff; padding: 15px 25px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        .header h1 { font-size: 20px; margin: 0; color: #333; }
        nav a { margin-left: 15px; color: #4a90e2; text-decoration: none; font-size: 14px; }
        .card { max-width: 700px; margin: 0 auto; background: #fff; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        label { display: block; margin-top: 15px; color: #555; font-weight: bold; }
        input, select, textarea { width: 100%; padding: 10px; margin-top: 5px; border: 1px solid #ccc; border-radius: 5px; box-sizing: border-box; font-family: inherit; }
        button { margin-top: 20px; padding: 12px 25px; background: #27ae60; color: #fff; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; }
        button:hover { background: #1e8449; }
    </style>
</head>
<body>
    <div class="header">
        <h1>Создание заявки</h1>
        <nav>
            <a href="requests.html">Мои заявки</a>
            <a href="login.html">Выйти</a>
        </nav>
    </div>

    <div class="card">
        <form action="requests.html" method="get">
            <label>Название мероприятия</label>
            <input type="text" placeholder="Например: Научная конференция" required>

            <label>Тип мероприятия</label>
            <select required>
                <option value="">-- Выберите --</option>
                <option>Конференция</option>
                <option>Семинар</option>
                <option>Круглый стол</option>
                <option>Тренинг</option>
                <option>Другое</option>
            </select>

            <label>Дата проведения</label>
            <input type="date" required>

            <label>Место проведения</label>
            <input type="text" placeholder="Аудитория / адрес" required>

            <label>Оплата</label>
            <select required>
                <option value="">-- Выберите --</option>
                <option>Очно</option>
                <option>СБП</option>
                <option>Карта</option>
            </select>

            <button type="submit">Отправить заявку</button>
        </form>
    </div>
</body>
</html>

ADMIN

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Панель администратора</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f0f2f5; margin: 0; padding: 20px; }
        .header { max-width: 1000px; margin: 0 auto 20px; display: flex; justify-content: space-between; align-items: center; background: #2c3e50; padding: 15px 25px; border-radius: 10px; color: #fff; }
        .header h1 { font-size: 20px; margin: 0; }
        nav a { margin-left: 15px; color: #ecf0f1; text-decoration: none; font-size: 14px; }
        nav a:hover { text-decoration: underline; }
        .container { max-width: 1000px; margin: 0 auto; }
        .stats { display: flex; gap: 15px; margin-bottom: 20px; flex-wrap: wrap; }
        .stat { flex: 1; min-width: 180px; background: #fff; padding: 20px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.08); text-align: center; }
        .stat h3 { margin: 0; font-size: 28px; color: #4a90e2; }
        .stat p { margin: 5px 0 0; color: #777; font-size: 14px; }
        table { width: 100%; border-collapse: collapse; background: #fff; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 10px rgba(0,0,0,0.08); }
        th, td { padding: 12px 15px; text-align: left; border-bottom: 1px solid #eee; font-size: 14px; }
        th { background: #f8f9fa; color: #333; }
        .btn { padding: 6px 12px; border: none; border-radius: 5px; cursor: pointer; font-size: 12px; margin-right: 5px; color: #fff; }
        .btn.approve { background: #27ae60; }
        .btn.reject { background: #e74c3c; }
        .btn.delete { background: #95a5a6; }
        .btn:hover { opacity: 0.85; }
    </style>
</head>
<body>
    <div class="header">
        <h1>Панель администратора</h1>
        <nav>
            <a href="login.html">Выйти</a>
        </nav>
    </div>

    <div class="container">
        <div class="stats">
            <div class="stat"><h3>12</h3><p>Всего заявок</p></div>
            <div class="stat"><h3>5</h3><p>Новая</p></div>
            <div class="stat"><h3>6</h3><p>Мероприятие завершено</p></div>
            <div class="stat"><h3>1</h3><p>Мероприятие назначено</p></div>
        </div>

        <table>
            <thead>
                <tr>
                    <th>№</th>
                    <th>Пользователь</th>
                    <th>Мероприятие</th>
                    <th>Дата</th>
                    <th>Статус</th>
                    <th>Действия</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>1</td>
                    <td>Иванов И.И.</td>
                    <td>Конференция</td>
                    <td>15.05.2024</td>
                    <td>В обработке</td>
                    <td>
                        <button class="btn approve">Принять</button>
                        <button class="btn reject">Отклонить</button>
                    </td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>Петрова А.С.</td>
                    <td>Семинар</td>
                    <td>20.06.2024</td>
                    <td>Проведено</td>
                    <td>
                        <button class="btn delete">Удалить</button>
                    </td>
                </tr>
                <tr>
                    <td>3</td>
                    <td>Сидоров П.П.</td>
                    <td>Круглый стол</td>
                    <td>10.04.2024</td>
                    <td>Отклонено</td>
                    <td>
                        <button class="btn approve">Принять</button>
                        <button class="btn delete">Удалить</button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</body>
</html>


-->
