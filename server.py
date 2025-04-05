from livereload import Server

server = Server()

# Следим за нужными файлами
server.watch('index.html')
server.watch('style.css')
server.watch('player.js')
server.watch('movie.mp4')  # вдруг поменяешь ролик

# Запускаем сервер на 5500 порту
server.serve(root='.', port=5500)
