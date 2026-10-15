import math

#Исходные данные
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

def print_non_comedy_titles(movies):
    """Печатает названия всех некомедийных фильмов."""
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])

def find_first_masterpiece(movies):
    """Находит и печатает название первого шедевра из списка."""
    i = 0
    while i < len(movies):
        if movies[i]["rating"] > 9:
            print(movies[i]["title"])
            break
        i += 1
    else:
        print("Шедевров не найдено")

def count_long_movies(movies, threshold=120):
    """Считает количество фильмов длиннее threshold."""
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
    """Возвращащает единую строку с описанием фильма."""
    return (
        f'"{normalize_title(movie["title"])}" ({movie["year"]}) — {movie["rating"]}/10,'
        f' {duration_in_hours(movie["duration_min"])}, '
        f'жанры: {", ".join(sorted(movie["genres"]))}'
    )


def titles_sorted_by_rating(movies):
    """Возвращает список названий фильмов, отсортированных по убыванию рейтинга."""
    movies_sorted = sorted(movies, key=lambda m: m["rating"], reverse=True)
    list_movies_sorted = []
    for movie in movies_sorted:
        list_movies_sorted.append(movie["title"])
    return list_movies_sorted

def top_n_by_rating(movies, n=3):
    """Возвращает список из n кортежей (title, rating) — топ по рейтингу."""
    movies_sorted = sorted(movies, key=lambda m: m["rating"], reverse=True)
    lst_movies_top_n = []
    for i in range(n):
        lst_movies_top_n.append((movies_sorted[i]["title"], movies_sorted[i]["rating"]))
    return lst_movies_top_n

def count_by_genre(movies):
    """Возвращает словарь {жанр: количество фильмов}."""
    genres_stat = {}
    for movie in movies:
        for genre in movie["genres"]:
            genres_stat[genre] = genres_stat.get(genre, 0) + 1
    return genres_stat

def actor_filmography(movies):
    """Возвращает словарь {актер: [список названий фильмов]}."""
    actor_filmography = {}
    for movie in movies:
        for actor in movie["actors"]:
            actor_filmography.setdefault(actor, []).append(movie["title"])
    return actor_filmography

def generate_dict(movies):
    """Генерирует словарь с фильмами с рейтингом выше среднего."""
    avg = average_rating(movies)
    return {movie["title"]: movie["rating"]
            for movie in movies
            if movie["rating"] > avg
    }

def all_genres(movies):
    """Возвращает множество всех уникальных жанров каталога."""
    all_genres = set()
    for movie in movies:
        all_genres |= movie["genres"]
    return all_genres

def common_actors(movie1, movie2):
    """Возвращает множество актеров, снимавшихся в обоих фильмах."""
    return set(movie1["actors"]) & set(movie2["actors"])

def genres_only_in_one(movies_a, movies_b):
    """Возвращает жанры, встречающиеся в movies_a, но не встречающиеся в movies_b."""
    return all_genres(movies_a) - all_genres(movies_b)

def iter_high_rated(movies, min_rating=8.0):
    """Функция-генератор отдает фильмы с рейтингом не ниже min_rating."""
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie

def print_high_rated_movies(movies, min_rating=8.0):
    """Напечатать фильмы с рейтингом не ниже min_rating."""
    for movie in iter_high_rated(movies, min_rating=min_rating):
        print(format_report_line(movie))

def count_total_duration(movies, min_r=7.0):
    """Считает суммарную длительность всех фильмов с рейтингом > min_r."""
    return sum(movie["duration_min"] for movie in movies if movie["rating"] > min_r)

def build_report(movies):
    """Объединяет результаты всех предыдущих этапов в единый отчет."""
    print()
    print("ОТЧеТ ПО КАТАЛОГУ")
    print(f'Средний рейтинг: {average_rating(movies)}')
    print(f'Средний возраст фильмов: {catalog_age_stats(movies)[2]} лет')
    print()
    print('Топ-3 фильма:')
    for top_movie in top_n_by_rating(movies):
        for movie in movies:
            if top_movie[0] == movie["title"]:
                print(f'  {format_report_line(movie)}')
    print()
    print('Фильмов по жанрам:')
    count_by_genre_sorted = dict(
        sorted(
            count_by_genre(movies).items(),
            key=lambda m: m[1],
            reverse=True,
        )
    )
    for key, value in count_by_genre_sorted.items():
        print(f"  {key} — {value}")
    print()
    print(f'Все жанры каталога: {", ".join(sorted(all_genres(movies)))}')

if __name__ == "__main__":
    build_report(movies)
