import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, 
     "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

def average_rating(movies):
    """Считает среднюю оценку по каталогу."""
    summa = 0
    for i in movies:
        summa += i['rating']
    return round(summa / len(movies), 1)

def catalog_age_stats(movies, current_year=2026):
    """Возвращает (самый старый фильм в годах, самый новый фильм в годах, среднее)."""
    min_age = 10000
    max_age = 0
    summa = 0
    for i in movies:
        age = current_year - i['year']
        summa += age
        if age >= max_age:
            max_age = age
        if age <= min_age:
            min_age = age
    return max_age, min_age, math.ceil(summa / len(movies))

def duration_in_hours(minutes):
    """Переводит минуты в часы в формате "Nч Mм"."""
    return str(minutes // 60) + 'ч' + ' ' + str(minutes % 60) + 'м'
    
minutes = 120
print(average_rating(movies))
print(catalog_age_stats(movies, current_year=2026))
print(duration_in_hours(minutes))
