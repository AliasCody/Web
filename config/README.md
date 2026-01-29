<span style='font-size:24px;'>File structure</span>
```bash
config/
├── __pycache__ /
│
├── __init__.py
├── asgi.py
├── settings.py
├── urls.py 
└── wsgi.py
```
- <span style='font-size:24px;'>[pycache](#about-__pycache__)</span>
- <span style='font-size:24px;'>[__init__.py](#about-__init__py)</span>
- <span style='font-size:24px;'>[asgi.py](#about-asgipy)</span>
- <span style='font-size:24px;'>[settings.py](#about-settingspy)</span>
- <span style='font-size:24px;'>[urls.py](#about-urlspy)</span>
- <span style='font-size:24px;'>[wsgi.py](#about-wsgipy)</span>

# About `__pycache__` 
<span style='font-size:24px;font-family:Segoe Print'>電腦不能識別高級語言，需要有一個翻譯機幫我們把高級語言轉變成電腦所能識別的機器語言，以前會將這個**過程**就分成 2 種類型:</span>

<span style='font-size:24px;font-family:Segoe Print'>1.(編譯型) Compiler 把你寫的程式轉為 machine code，接著機器直接執行它。(範例: `C`)</span>

<span style='font-size:24px;font-family:Segoe Print'>2.(解釋型) 透過 Translater ，我們直接一行一行解釋 code 讓機器執行。(範例: `Ruby`、`Python`)</span>

<span style='font-size:24px;font-family:Segoe Print'>但現在很多解釋型語言其實會進行一步`預編譯` :</span>

<span style='font-size:24px;font-family:Segoe Print'>1. Python: 會先將 `.py` 轉成 `.pyc` 檔案(bytecode)。這不是 machine code，而是給 python 虛擬機看的</span>

<span style='font-size:24px;font-family:Segoe Print'>2. Java: 先編譯成 `.class`(bytecode)，再交給 `JVM` 解釋和執行</span>

<span style='font-size:24px;font-family:Segoe Print'>As a programmer, you can largely just ignore it.
All it does is make your program start a little faster.</span> 




# About `__init__.py`

<span style='font-size:24px;font-family:Segoe Print'>Python defines two types of packages: </span>

<span style='font-size:24px;font-family:Segoe Print'>1. Regular packages</span>

- <span style='font-size:24px;'>A regular package is typically implemented as a `directory` containing an `__init__.py` file.</span>
- <span style='font-size:24px;'>When a regular package is imported,this `__init__.py` file is `implicitly` executed,and the objects it defines are bound to names in the package's namespace.</span>
- <span style='font-size:24px;'>Variables write in the `__init.py` can give you a chance using the form of `{package_name}.{variable's name}` to access the variable.(ex. `print(pandas.version)`)</span>

<span style='font-size:24px;font-family:Segoe Print'>2. Namespace packages</span>

- <span style='font-size:24px;'>In my opinion,this type of packages means **It will contain many different module,and so the behavior of the programmer should be selecting the needed module in this file.Not just import this package.**</span>

- <span style='font-size:24px;'>Basically you can treat it as **a big package that contains lots of `Regular package`s.**</span>


# About `asgi.py`
<span style='font-size:24px;'>ASGI is abbraviate of **Asynchronous Server Gateway Interface**.</span>

<span style='font-size:24px;'>This is a file generate automatically by django.In this project,we don't need this file.(2026/1/28)</span>


# About `settings.py`

# About `urls.py`


# About `wsgi.py`
<span style='font-size:24px;font-family:Segoe Print'>WSGI means **Web Server Gateway Interface**</span>



# Reference

- [Day8 Python 基礎 - pyc 是什麼](https://ithelp.ithome.com.tw/articles/10185442Java)
- [What is __pycache__?](https://stackoverflow.com/questions/16869024/what-is-pycache)
- [What is __init__.py for?](https://stackoverflow.com/questions/448271/what-is-init-py-for)
- [5.2. Packages (ref from ch5.2.1 to ch5.2.2)](https://docs.python.org/3/reference/import.html#regular-packages)
- [PEP 3333 – Python Web Server Gateway Interface v1.0.1 (Description about wsgi.py)](https://peps.python.org/pep-3333/)