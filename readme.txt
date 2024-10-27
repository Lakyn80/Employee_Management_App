@app.route('/')
def index():
    employees = load_employees()
    return render_template('index.html', employees=employees)


1. Dekorátor @app.route('/')
Dekorátor @app.route('/') v Flasku říká aplikaci, že následující funkce index má být spuštěna pokaždé, když uživatel navštíví hlavní stránku aplikace (cesta /).
V případě této aplikace znamená hlavní stránka například http://localhost:5000/, pokud aplikaci spustíme lokálně.
Dekorátor @app.route('/') tedy propojuje URL (cestu) / s funkcí index, která se pak stará o to, co bude zobrazeno uživateli.


2. Definice funkce index


def index():
    employees = load_employees()
    return render_template('index.html', employees=employees)

Co se děje uvnitř funkce index:
Načítání dat zaměstnanců pomocí load_employees()

employees = load_employees()
Tato řádka volá funkci load_employees() (definovanou dříve v kódu), která načte seznam zaměstnanců uložený v JSON souboru employees.json.
Funkce load_employees() vrátí buď seznam se všemi zaměstnanci (pokud JSON soubor existuje a obsahuje data), nebo prázdný seznam, pokud žádní zaměstnanci nejsou uloženi.
Výsledek načtení (seznam zaměstnanců) se uloží do proměnné employees.
Vykreslení šablony pomocí render_template

return render_template('index.html', employees=employees)
Tato řádka říká aplikaci, aby načetla a vykreslila HTML šablonu index.html, která se nachází ve složce templates.
render_template je funkce Flasku, která umožňuje vykreslování šablon s dynamickým obsahem.
Předání proměnné do šablony:
employees=employees předává proměnnou employees do šablony index.html.
V HTML šabloně index.html tedy bude možné použít proměnnou employees k zobrazení seznamu zaměstnanců.
Díky tomu lze ve šabloně pomocí {{ employees }} nebo v cyklu for přistupovat k datům každého zaměstnance a dynamicky je zobrazit uživateli na webové stránce.
Co se děje, když uživatel navštíví /?
Aplikace volá funkci index, protože dekorátor @app.route('/') je nastaven pro tuto URL cestu.

Načítají se data zaměstnanců pomocí load_employees(), která je načte ze souboru employees.json (nebo vrátí prázdný seznam, pokud žádní zaměstnanci nejsou).

Šablona index.html se vykreslí a je předána proměnná employees s daty zaměstnanců.

Díky render_template('index.html', employees=employees) je seznam zaměstnanců k dispozici přímo v šabloně, což umožňuje dynamicky generovat obsah stránky.
Výsledek se zobrazí v prohlížeči uživatele:

Flask aplikace odešle vygenerovanou HTML stránku s obsahem (tedy s údaji o zaměstnancích) do prohlížeče uživatele.
Uživatel uvidí seznam zaměstnanců, který je dynamicky načten z JSON souboru a zobrazen pomocí HTML šablony index.html.
Tímto způsobem Flask aplikace umožňuje zobrazit aktuální seznam zaměstnanců na hlavní stránce (/), přičemž data jsou načítána ze serveru dynamicky pokaždé, když uživatel tuto stránku navštíví.
