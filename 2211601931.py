import csv
import matplotlib.pyplot as plt

def read_csv_file(file_path):
    data = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            data.append(row)
    return data

def display_menu():
    print("+------------------------------------------------+")
    print("| Hello, Selamat Datang di Dashboard IMDB by.    |")
    print("| > NIM  : 2211601931                            |")
    print("| > Nama : Deni Sumarno                          |")
    print("+------------------------------------------------+")
    print("| \t\t\tMENU                     |")                             
    print("+------------------------------------------------+")
    print("[1] Genre                                        |")
    print("[2] Color                                        |")
    print("[3] Bahasa|Language                              |")
    print("[4] Negara|Country                               |")
    print("[5] Total Film|Total Movie                       |")
    print("[6] Bar Chart Rating                             |")
    print("[7] Resume Gross dan Duration                    |")
    print("[8] Query (Language dan Genre)                   |")
    print("[0] Exit|Quit                                    |")
    print("+------------------------------------------------+")

def sub_menu_genre(data):
    print("Input Pilihan: 1")
    print("Jenis Genre terbagi ke dalam 17 Genre, yaitu:")
    genres = set(movie['Genre'] for movie in data)
    for idx, genre in enumerate(genres, start=1):
        print(f"{idx}. {genre}")

def sub_menu_color(data):
    print("Input Pilihan: 2")
    print("Jenis Warna terbagi ke dalam 2 Jenis Warna, yaitu:")
    colors = set(movie['Color/B&W'] for movie in data)
    for idx, color in enumerate(colors, start=1):
        print(f"{idx}. {color}")

def sub_menu_bahasa(data):
    print("Input Pilihan: 3")
    print(f"Dataset IMDB saat ini terdiri dari {len(set(movie['Language'] for movie in data))} Bahasa")

def sub_menu_negara(data):
    print("Input Pilihan: 4")
    print(f"Terdapat {len(set(movie['Country'] for movie in data))} Negara dalam Dataset IMDB")

def sub_menu_total_film(data):
    print("Input Pilihan: 5")
    print(f"Dataset IMDB saat ini memiliki {len(data)} Film")

def sub_menu_bar_chart(data):
    print("Input Pilihan: 6")
    ratings = [movie['Rating'] for movie in data]

    rating_counts = {}
    for rating in ratings:
        if rating not in rating_counts:
            rating_counts[rating] = 1
        else:
            rating_counts[rating] += 1

    rating_values = list(rating_counts.keys())
    film_counts = list(rating_counts.values())

    plt.figure(figsize=(10, 6))
    plt.bar(rating_values, film_counts, color='skyblue', alpha=0.7)
    plt.xlabel('Rating')
    plt.ylabel('Title')
    plt.title('Film berdasarkan Rating')
    plt.show()

    print("\n> Kembali ke Menu Utama")

def sub_menu_resume(data):
    print("Input Pilihan: 7")
    # Implementasi Resume Gross dan Duration
    gross_values = [float(movie['Gross Revenue']) for movie in data if movie['Gross Revenue'].strip()]
    
    duration_values = [float(movie['Duration (min)']) for movie in data if movie['Duration (min)'].strip()]

    gross_resume = {
        'Total': sum(gross_values),
        'Rata-rata': sum(gross_values) / len(gross_values),
        'Terendah': min(gross_values),
        'Tertinggi': max(gross_values)
    }

    duration_resume = {
        'Total': sum(duration_values),
        'Rata-rata': sum(duration_values) / len(duration_values),
        'Terendah': min(duration_values),
        'Tertinggi': max(duration_values)
    }

    print("Gross Revenue Resume:")
    print("=====================")
    for key, value in gross_resume.items():
        print(f"{key} : ${value:.2f}")

    print("\nDuration Resume:")
    print("================")
    for key, value in duration_resume.items():
        print(f"{key} : {value:.2f} Menit")

def sub_menu_query(data):
    print("Input Pilihan: 8")
    print(">> Input Bahasa yang dicari: (Spasi untuk Kembali ke Menu)")
    language = input().strip()

    if not language:
        return

    print(f">> Genre?")
    genre = input().strip()

    filtered_movies = [movie for movie in data if movie['Language'].lower() == language.lower() and movie['Genre'].lower() == genre.lower()]

    print("\nList 5 Film")
    for idx, movie in enumerate(filtered_movies[:5], start=1):
        print(f"{idx}. Title: {movie['Title']}, Release Date: {movie['Release Date']}, Gross Revenue: ${movie['Gross Revenue']}, Budget: ${movie['Budget']}")


    df_filtered = pd.DataFrame(filtered_movies)

    print("\nTotal Film Genre", genre, "dan", language, "adalah:", len(filtered_movies), "Film")

    total_duration = df_filtered['Duration (min)'].astype(float).sum()
    average_duration = df_filtered['Duration (min)'].astype(float).mean()

    print(f"\nTotal Durasi : {total_duration} Menit")
    print(f"Rata-rata Durasi: {average_duration} Menit")

    min_duration_movie = df_filtered.loc[df_filtered['Duration (min)'].astype(float).idxmin()]
    max_duration_movie = df_filtered.loc[df_filtered['Duration (min)'].astype(float).idxmax()]

    print(f"Durasi Terendah: {min_duration_movie['Duration (min)']} Menit, Lead Actor: {min_duration_movie['Lead Actor']}")
    print(f"Durasi Tertinggi: {max_duration_movie['Duration (min)']} Menit, Lead Actor: {max_duration_movie['Lead Actor']}")

    total_gross = df_filtered['Gross Revenue'].astype(float).sum()
    average_gross = df_filtered['Gross Revenue'].astype(float).mean()

    print(f"\nTotal Gross Revenue :$ {total_gross}")
    print(f"Rata-rata Gross Revenue: $ {average_gross}")

    min_gross_movie = df_filtered.loc[df_filtered['Gross Revenue'].astype(float).idxmin()]
    max_gross_movie = df_filtered.loc[df_filtered['Gross Revenue'].astype(float).idxmax()]

    print(f"Gross Revenue Terendah : $ {min_gross_movie['Gross Revenue']}, Lead Actor: {min_gross_movie['Lead Actor']}, Title: {min_gross_movie['Title']}")
    print(f"Gross Revenue Tertinggi: $ {max_gross_movie['Gross Revenue']}, Lead Actor: {max_gross_movie['Lead Actor']}, Title: {max_gross_movie['Title']}")

    print(f"\n> Input Bahasa yang dicari: (Spasi untuk Kembali ke Menu)")

def main_menu(data):
    while True:
        display_menu()
        choice = input("Input Pilihan: ")

        if choice == '1':
            sub_menu_genre(data)
        elif choice == '2':
            sub_menu_color(data)
        elif choice == '3':
            sub_menu_bahasa(data)
        elif choice == '4':
            sub_menu_negara(data)
        elif choice == '5':
            sub_menu_total_film(data)
        elif choice == '6':
            sub_menu_bar_chart(data)
        elif choice == '7':
            sub_menu_resume(data)
        elif choice == '8':
            sub_menu_query(data)
        elif choice == '0':
            print("Terima kasih! Exit.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    # Tambahan import pandas
    import pandas as pd

    csv_file_path = "imdb.csv"  # Ganti dengan path sesuai lokasi file CSV Anda
    movie_data = read_csv_file(csv_file_path)

    # Jalankan menu utama
    main_menu(movie_data)
