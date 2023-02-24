## Итоговый проект по курсу "Методы сбора и обработки данных из сети Интернет"
### Задание:
1. Написать приложение, которое будет проходиться по вакансиям аналитики на сайте  [superjob.ru](https://www.superjob.ru/).
2. По каждой вакансии извлечь информацию о компании, назавании вакансии, зарплате и фото компании, если есть.
3. Собранные данные необходимо сложить в базу данных.
4. Написать два запроса к базе данных (1 - кол-во вакансий определенной компании, 2 - вывести вакансии **либо** по названию компании, **либо** по названию вакансии).

Навигация:
1. Запросы к базе данных находятся здесь: [query](https://github.com/dunklenichts/Parsing-Internet/blob/main/Project/Scrapy-MongoDB/Запросы%20к%20БД.pdf)
2. Файл с пауками: [spiders](https://github.com/dunklenichts/Parsing-Internet/tree/main/Project/Scrapy-MongoDB/job_parser/spiders)
3. Файл с загрузкой в БД: [pipelines](https://github.com/dunklenichts/Parsing-Internet/blob/main/Project/Scrapy-MongoDB/job_parser/pipelines.py)
