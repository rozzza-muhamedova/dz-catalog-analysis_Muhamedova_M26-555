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
    for movie in movies:
        summa += movie['rating']
    return round(summa / len(movies), 1)

def catalog_age_stats(movies, current_year=2026):
    """Возвращает (самый старый фильм в годах, самый новый фильм в годах, среднее)."""
    min_age = float("inf")
    max_age = 0
    summa = 0
    for movie in movies:
        age = current_year - movie['year']
        summa += age
        if age >= max_age:
            max_age = age
        if age <= min_age:
            min_age = age
    return max_age, min_age, math.ceil(summa / len(movies))

def duration_in_hours(minutes):
    """Переводит минуты в часы в формате "Nч Mм"."""
    return str(minutes // 60) + 'ч' + ' ' + str(minutes % 60) + 'м'

def rating_tier(rating):
    """Возвращает по оценке категорию."""
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    else:
        return "средне" if rating >= 5 else "слабо"

def decade_label(year):
    """Возвращает по году метку."""
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"

def count_long_movies(movies, threshold=120):
    """Cчитает количество фильмов длиннее threshold."""
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count

def normalize_title(title):
    """Приводит строку к формату Title Case."""
    new_word_list = []
    for word in title.split():
        new_word_list.append(word[0].upper() + word[1:])
    return " ".join(new_word_list)

def make_slug(title):
    """Превращает нормализованное название в «слаг»."""
    return title.lower().replace(" ", "-")

def format_report_line(movie):
    """Возвращающую единую строку с описанием фильма"""
    return (
        f'"{movie["title"]}" ({movie["year"]}) — {movie["rating"]}/10, '
        f'{duration_in_hours(movie["duration_min"])}, '
        f'жанры: {", ".join(sorted(movie["genres"]))}'
    )

def get_rating(movie):
    """Вспомогательная функия возвращает рейтинг фильма."""
    return movie["rating"]

def titles_sorted_by_rating(movies):
    """Возвращает список названий фильмов, отсортированных по убыванию рейтинга."""
    movies_sorted = sorted(movies, key=get_rating, reverse=True)
    list_movies_sorted = []
    for movie in movies_sorted:
        list_movies_sorted.append(movie["title"])
    return list_movies_sorted

def top_n_by_rating(movies, n=3):
    """Возвращает список из n кортежей (title, rating) — топ по рейтингу."""
    movies_sorted = sorted(movies, key=get_rating, reverse=True)
    lst_movies_top_n = []
    for i in range(n):
        lst_movies_top_n.append((movies_sorted[i]["title"], movies_sorted[i]["rating"]))
    return lst_movies_top_n

if __name__ == "__main__":

    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])

    i = 0
    while i < len(movies):
        if movies[i]["rating"] > 9:
            print(movies[i]["title"])
            break
        i += 1
    else:
        print("Шедевров не найдено")

    minutes = 120
    rating = 4
    year = 2019
    title = "silent hours"
    print(average_rating(movies))
    print(catalog_age_stats(movies, current_year=2026))
    print(duration_in_hours(minutes))
    print(rating_tier(rating))
    print(decade_label(year))
    print(count_long_movies(movies, threshold=120))
    print(normalize_title(title))
    title = normalize_title(title)
    print(make_slug(title))
    movie = movies[7]
    print(format_report_line(movie))
    print()
    print(titles_sorted_by_rating(movies))
    print()
    print(movies)
    print()
    print(top_n_by_rating(movies, n=3))


