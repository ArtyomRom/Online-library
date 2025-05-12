from jinja2 import Environment, FileSystemLoader
import json
import os
import urllib.parse
from more_itertools import chunked

BOOKS_PER_PAGE = 20

# Загружаем данные
with open('meta_data.json', encoding='utf-8') as f:
    books = json.load(f)
    for book in books:
        book['book_path'] = urllib.parse.quote(book['book_path'])

# Инициализируем Jinja2, указывая путь к шаблонам
env = Environment(loader=FileSystemLoader('docs'))

# Загружаем шаблон index.html (который наследуется от template.html)
template = env.get_template('index.html')

pages = list(chunked(books, BOOKS_PER_PAGE))
total_pages = len(pages)

os.makedirs('docs', exist_ok=True)

# ✅ Рендерим и сохраняем КАЖДУЮ страницу
for page_num, books_chunk in enumerate(pages, start=1):
    output_filename = f'output{page_num}.html' if page_num > 1 else 'output.html'
    output_path = os.path.join('docs', output_filename)

    html_output = template.render(
        books=books_chunk,
        page_num=page_num,
        total_pages=total_pages
    )

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_output)