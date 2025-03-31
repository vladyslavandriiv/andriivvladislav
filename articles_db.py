import sqlite3


def create_table():
    """Створення таблиці Articles у базі даних"""
    with sqlite3.connect("articles.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Articles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                author TEXT NOT NULL
            )
        ''')
        conn.commit()


def add_article():
    """Додавання нової статті вручну"""
    title = input("Введіть заголовок статті: ")
    content = input("Введіть вміст статті: ")
    author = input("Введіть автора статті: ")

    with sqlite3.connect("articles.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Articles (title, content, author)
            VALUES (?, ?, ?)
        """, (title, content, author))
        conn.commit()
        print("✅ Статтю додано успішно!")


def delete_article():
    """Видалення статті за ID (введення вручну)"""
    article_id = input("Введіть ID статті, яку хочете видалити: ")

    with sqlite3.connect("articles.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Articles WHERE id = ?", (article_id,))
        if cursor.rowcount > 0:
            conn.commit()
            print(f"✅ Статтю з ID {article_id} видалено!")
        else:
            print("⚠️ Статтю не знайдено!")


def update_article():
    """Оновлення статті за ID (введення вручну)"""
    article_id = input("Введіть ID статті для оновлення: ")
    new_title = input("Введіть новий заголовок: ")
    new_content = input("Введіть новий вміст: ")

    with sqlite3.connect("articles.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Articles 
            SET title = ?, content = ?
            WHERE id = ?
        """, (new_title, new_content, article_id))
        if cursor.rowcount > 0:
            conn.commit()
            print(f"✅ Статтю з ID {article_id} оновлено!")
        else:
            print("⚠️ Статтю не знайдено!")


def view_articles():
    """Перегляд усіх статей"""
    with sqlite3.connect("articles.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Articles")
        articles = cursor.fetchall()
        if not articles:
            print("ℹ️ Немає жодної статті!")
        for article in articles:
            print(f"🆔 ID: {article[0]}, 📝 Назва: {article[1]}, ✍️ Автор: {article[3]}")
            print(f"📜 Вміст: {article[2]}")
            print("-" * 40)


def find_article_by_author():
    """Пошук статей за автором"""
    author = input("Введіть ім'я автора для пошуку: ")

    with sqlite3.connect("articles.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Articles WHERE author = ?", (author,))
        articles = cursor.fetchall()
        if not articles:
            print(f"ℹ️ Статей автора {author} не знайдено!")
        for article in articles:
            print(f"🆔 ID: {article[0]}, 📝 Назва: {article[1]}")
            print(f"📜 Вміст: {article[2]}")
            print("-" * 40)


# Головне меню
def main():
    create_table()
    while True:
        print("\n📌 Меню:")
        print("1️⃣ Додати статтю")
        print("2️⃣ Видалити статтю")
        print("3️⃣ Оновити статтю")
        print("4️⃣ Переглянути всі статті")
        print("5️⃣ Знайти статтю за автором")
        print("0️⃣ Вийти")

        choice = input("Виберіть опцію: ")

        if choice == "1":
            add_article()
        elif choice == "2":
            delete_article()
        elif choice == "3":
            update_article()
        elif choice == "4":
            view_articles()
        elif choice == "5":
            find_article_by_author()
        elif choice == "0":
            print("👋 Вихід із програми...")
            break
        else:
            print("⚠️ Невірний вибір, спробуйте ще раз!")


# Запуск головного меню
if __name__ == "__main__":
    main()