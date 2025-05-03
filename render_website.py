from jinja2 import Environment, FileSystemLoader
import json



# Данные для подстановки
with open('meta_data.json', encoding='utf-8') as f:
    books = json.load(f)
# Настройка шаблонизатора
env = Environment(loader=FileSystemLoader('.'))  # <-- . значит "ищи рядом с этим скриптом"


template = env.get_template('index.html')

# Рендеринг
html_output = template.render(books=books)

# Сохраняем результат
with open('output.html', 'w', encoding='utf-8') as f:
    f.write(html_output)