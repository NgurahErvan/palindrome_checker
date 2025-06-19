# Contributors

| Nama | NRP |
|------|-----|
| Al-Ferro Yudisthira Putra | 5025211176 |
| I Gusti Ngurah Ervan Juli Ardana | 5025211205 |
| Beauty Valen Fajri | 5025211227 |

# Palindrome Checker Flask Application

Aplikasi web sederhana yang dibuat dengan Flask untuk memeriksa apakah sebuah teks merupakan palindrom menggunakan berbagai algoritma dan pendekatan yang berbeda.

## 📋 Deskripsi

Palindrom adalah kata, frasa, angka, atau urutan karakter lain yang dibaca sama dari depan maupun belakang. Aplikasi ini menyediakan lima metode berbeda untuk memeriksa palindrom:

1. **Basic Check** - Pemeriksaan dasar tanpa preprocessing
2. **Clean Check** - Pemeriksaan dengan pembersihan karakter (case-insensitive, alphanumeric only)
3. **Iterative Check** - Menggunakan pendekatan iteratif dengan two pointers
4. **Recursive Check** - Menggunakan pendekatan rekursif
5. **Automata Check** - Menggunakan konsep finite state automata dengan stack

## 📁 Struktur Proyek

```
palindrome-checker/
│
├── app.py              # File utama Flask application
├── templates/
│   └── index.html      # Template HTML untuk interface
└── README.md           # Dokumentasi proyek
```

## 🛠️ Instalasi dan Setup

### Prasyarat
- Python 3.6+
- Flask

### Langkah Instalasi

1. Clone atau download proyek ini
2. Install Flask:
   ```bash
   pip install flask
   ```
3. Jalankan aplikasi:
   ```bash
   python app.py
   ```
4. Buka browser dan akses `http://localhost:5000`

## 📖 Penjelasan Algoritma

### 1. Basic Palindrome Check
```python
def is_palindrome_basic(s):
    return s == s[::-1]
```
- **Cara Kerja**: Membandingkan string asli dengan string yang dibalik
- **Karakteristik**: Case-sensitive, termasuk spasi dan tanda baca
- **Contoh**: "Aba" → False, "aba" → True

### 2. Clean Palindrome Check
```python
def is_palindrome_clean(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1], cleaned
```
- **Cara Kerja**: Membersihkan string (hanya alphanumeric, lowercase) lalu membalik
- **Karakteristik**: Case-insensitive, mengabaikan spasi dan tanda baca
- **Contoh**: "A man, a plan, a canal: Panama" → True

### 3. Iterative Palindrome Check
```python
def is_palindrome_iterative(s):
    # Menggunakan two pointers dari awal dan akhir string
```
- **Cara Kerja**: Menggunakan dua pointer (kiri dan kanan) yang bergerak ke tengah
- **Kompleksitas**: O(n) waktu, O(1) ruang (tidak termasuk pembersihan)
- **Keunggulan**: Efisien dalam penggunaan memori

### 4. Recursive Palindrome Check
```python
def is_palindrome_recursive(s):
    # Menggunakan fungsi rekursif untuk memeriksa karakter
```
- **Cara Kerja**: Membandingkan karakter pertama dan terakhir secara rekursif
- **Kompleksitas**: O(n) waktu, O(n) ruang (karena call stack)
- **Keunggulan**: Elegant dan mudah dipahami

### 5. Automata Palindrome Check
```python
def is_palindrome_automata_case_insensitive(input_str):
    # Menggunakan finite state automata dengan stack
```
- **Cara Kerja**: Menggunakan konsep automata dengan dua state (PUSH dan POP)
- **State PUSH**: Memasukkan karakter ke stack sampai tengah string
- **State POP**: Membandingkan karakter dengan yang ada di stack
- **Keunggulan**: Implementasi konsep teoretis computer science

## 🧪 Contoh Penggunaan

### Input yang Menghasilkan True (Palindrom):
- "racecar"
- "A man, a plan, a canal: Panama"
- "race a car" (setelah dibersihkan menjadi "raceacar")
- "Was it a car or a cat I saw?"
- "Madam"
- "12321"

### Input yang Menghasilkan False (Bukan Palindrom):
- "hello"
- "Python"
- "race a car" (basic check - karena spasi)
- "12345"
