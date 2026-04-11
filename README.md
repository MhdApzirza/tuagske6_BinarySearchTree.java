# Tugas ke-6 Struktur Data Kelas A

**Nama:** Muhammad Apzirza Rafi
**NIM:** 24106050077

*Implementasi: Manajemen Database Inventaris Barang menggunakan Struktur Data Binary Search Tree (BST) dalam bahasa Java dan Python.*

## 📝 Deskripsi Tugas
Program ini merupakan tugas penutup yang mensimulasikan penyimpanan dan pencarian data dalam skala yang lebih besar (100 baris data). Data dikelola menggunakan struktur data Binary Search Tree (BST) untuk mendemonstrasikan efisiensi pencarian dibandingkan struktur data linear.

Dalam struktur ini, data diatur secara hierarkis di mana setiap node kiri memiliki nilai lebih kecil dari induknya, dan setiap node kanan memiliki nilai lebih besar. Hal ini memungkinkan pencarian, penambahan, dan penghapusan data dilakukan dengan kecepatan $O(\log n)$.

## 🚀 Fitur Menu / Fungsi
- Batch Data Input: Mengintegrasikan 100 data barang (ID dan Nama) secara otomatis dari dataset Excel ke dalam pohon saat program dijalankan.

- Pencarian Cepat (Search): Menemukan nama barang berdasarkan ID tertentu dengan membandingkan nilai pada tiap cabang.

- Manajemen Data (Insert & Delete): Menambah barang baru secara manual atau menghapus data yang sudah ada tanpa merusak struktur pohon.

- Triple Traversal: Menyediakan tiga metode penelusuran data:
    - In-order: Menampilkan seluruh data secara terurut berdasarkan ID.
    - Pre-order: Menampilkan data dengan memprioritaskan akar (root) terlebih dahulu.
    - Post-order: Menampilkan data dengan memprioritaskan cabang (leaf) terlebih dahulu.

## ⚙️ Detail Implementasi
- Logic: Menggunakan algoritma rekursif untuk penelusuran cabang kiri dan kanan guna memastikan aturan BST tetap terjaga.

- Root Identification: Mengidentifikasi data pertama yang diinput (ID 5288 - Pensil) sebagai root utama pohon.

- Complexity: Dirancang untuk menangani 100 data barang dengan performa pencarian yang optimal.

- Language: Tersedia dalam versi Java (.java) dan Python (.py).

## 🎥 Video Demo
Demonstrasi teknis mengenai cara kerja BST, perbedaan hasil ketiga jenis traversal, serta efisiensi pencarian pada 100 data barang:

**[Nonton Video Demo](link)**
*Klik gambar di atas untuk memutar video demo di YouTube @Muhammad Apzirza Rafi.*
