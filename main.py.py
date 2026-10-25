import csv
import time

# ==========================================
# 1. MODEL INPUT & OUTPUT
# ==========================================

class Book:
    """Kelas untuk merepresentasikan data buku dari dataset."""
    def __init__(self, title: str, author: str, category: str):
        self.title = title
        self.author = author
        self.category = category

class SearchResult:
    """Kelas untuk merepresentasikan hasil keluaran dari pencarian."""
    def __init__(self, found: bool, book: Book | None, comparisons: int, execution_time: float):
        self.found = found
        self.book = book
        self.comparisons = comparisons
        self.execution_time = execution_time


# ==========================================
# 2. IMPLEMENTASI ALGORITMA PENCARIAN
# ==========================================

def linear_search(books: list[Book], target_title: str) -> SearchResult:
    """
    Mengimplementasikan Linear Search secara manual tanpa fungsi bawaan Python.
    """
    start_time = time.perf_counter()
    comparisons = 0

    for book in books:
        comparisons += 1
        # Membandingkan judul buku satu per satu secara sekuensial
        if book.title == target_title:
            end_time = time.perf_counter()
            return SearchResult(True, book, comparisons, end_time - start_time)

    end_time = time.perf_counter()
    return SearchResult(False, None, comparisons, end_time - start_time)


def binary_search(sorted_books: list[Book], target_title: str) -> SearchResult:
    """
    Mengimplementasikan Binary Search secara manual pada list yang sudah terurut.
    """
    start_time = time.perf_counter()
    comparisons = 0
    low = 0
    high = len(sorted_books) - 1

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1

        # Membandingkan dengan data di posisi tengah
        if sorted_books[mid].title == target_title:
            end_time = time.perf_counter()
            return SearchResult(True, sorted_books[mid], comparisons, end_time - start_time)
        elif sorted_books[mid].title < target_title:
            low = mid + 1
        else:
            high = mid - 1

    end_time = time.perf_counter()
    return SearchResult(False, None, comparisons, end_time - start_time)


# ==========================================
# 3. FUNGSI PEMBACA DATASET
# ==========================================

def load_dataset(file_path: str, limit: int = None) -> list[Book]:
    """Membaca file CSV dataset dan mengembalikannya dalam bentuk list of Book."""
    books = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Menyesuaikan nama kolom sesuai dataset Kaggle
                title = row.get('title', row.get('Title', ''))
                author = row.get('author', row.get('authors', ''))
                category = row.get('category', row.get('categories', ''))
                
                books.append(Book(title, author, category))
                
                if limit and len(books) >= limit:
                    break
    except FileNotFoundError:
        print(f"Error: File '{file_path}' tidak ditemukan. Pastikan file CSV ada di folder yang sama.")
    return books


# ==========================================
# 4. EKSEKUSI PENGUJIAN & SIMULASI SKENARIO
# ==========================================

def main():
    # Ganti nama file sesuai file CSV dataset Kaggle yang kamu unduh
    csv_file = "books.csv" 
    
    print("=== MENGAMBIL DATA DARI DATASET ===")
    full_dataset = load_dataset(csv_file, limit=10000)
    
    if not full_dataset:
        print("Dataset kosong atau gagal dimuat.")
        return

    # Pengujian pada beberapa ukuran input n = 100, 1.000, 10.000
    sample_sizes = [100, 1000, min(10000, len(full_dataset))]
    
    print("\n" + "="*60)
    print(" PENGUJIAN UKURAN INPUT (N = 100, 1.000, 10.000) ")
    print("="*60)

    for n in sample_sizes:
        data_sample = full_dataset[:n]
        # Data disorting untuk keperluan Binary Search
        sorted_sample = sorted(data_sample, key=lambda x: x.title)
        
        # Ambil contoh target dari data
        target_exist = data_sample[n // 2].title
        
        ls_res = linear_search(data_sample, target_exist)
        bs_res = binary_search(sorted_sample, target_exist)

        print(f"\n--- Ukuran Input n = {n} ---")
        print(f"Linear Search  -> Perbandingan: {ls_res.comparisons:<6} | Waktu: {ls_res.execution_time:.6f} detik")
        print(f"Binary Search  -> Perbandingan: {bs_res.comparisons:<6} | Waktu: {bs_res.execution_time:.6f} detik")

    # Pengujian 4 Skenario Pencarian pada n = 10.000
    n = sample_sizes[-1]
    data_sample = full_dataset[:n]
    sorted_sample = sorted(data_sample, key=lambda x: x.title)

    print("\n" + "="*60)
    print(f" SIMULASI 4 SKENARIO PENCARIAN (n = {n}) ")
    print("="*60)

    scenarios = [
        ("Awal Dataset", data_sample[0].title),
        ("Tengah Dataset", data_sample[n // 2].title),
        ("Akhir Dataset", data_sample[-1].title),
        ("Tidak Ditemukan", "Buku_X_Yang_Tidak_Pernah_Ada_12345")
    ]

    for label, target in scenarios:
        ls_res = linear_search(data_sample, target)
        bs_res = binary_search(sorted_sample, target)
        
        print(f"\nSkenario: Data Ditemukan di [{label}]")
        print(f"  [Linear Search] Perbandingan: {ls_res.comparisons:<6} | Waktu: {ls_res.execution_time:.6f} s")
        print(f"  [Binary Search] Perbandingan: {bs_res.comparisons:<6} | Waktu: {bs_res.execution_time:.6f} s")

if __name__ == "__main__":
    main()