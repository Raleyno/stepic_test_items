# 1. Запуск теста:
Тест должен запускаться следующей командой:

pytest --language=es test_items.py

# 2. После первого запуска теста и получения его результата необходимо внести следующие изменения:

- Добавьте в файл с тестом команду <b>time.sleep(30)</b> сразу после открытия ссылки <b>(раскоментируйте данную строку в коде)</b>.

- Запустите тест с параметром <b>--language=fr</b> и визуально проверьте, что фраза на кнопке добавления в корзину выглядит так: "Ajouter au panier".
