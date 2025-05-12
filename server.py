from livereload import Server
import os

def build():
    os.system('python render_website.py')

server = Server()

# Следим за шаблоном и данными
server.watch('template.html', build)
server.watch('meta_data.json', build)
server.watch('docs/index.html')


# Запускаем сервер и открываем output.html
server.serve(root='docs', open_url_delay=1, default_filename='index.html')