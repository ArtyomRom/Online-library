from jinja2 import Environment, FileSystemLoader
import json
import os

# Загружаем данные
with open('meta_data.json', encoding='utf-8') as f:
    books = json.load(f)

# Инициализируем Jinja2, указывая путь к шаблонам
env = Environment(loader=FileSystemLoader('dist'))

# Загружаем шаблон index.html (который наследуется от template.html)
template = env.get_template('index.html')

# Рендерим с данными
html_output = template.render(books=books)

# Сохраняем результат как output.html
os.makedirs('dist', exist_ok=True)
with open('dist/output.html', 'w', encoding='utf-8') as f:
    f.write(html_output)