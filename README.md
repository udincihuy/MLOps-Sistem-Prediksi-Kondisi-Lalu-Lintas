# Sistem Prediksi Harga Minyak Berbasis MLOps

## Struktur Direktori

Berikut struktur proyek yang digunakan:

```text
MLOps-Sistem-Prediksi-harga-minyak/
├── data/           → Berkaitan dengan data yang diambil (data ada versioningnya)
│   ├── raw/        → Data mentah dari API
│   └── processed/  → Data yang sudah dibersihkan
├── models/         → Penyimpanan model hasil training
├── notebooks/      → Eksperimen dan Exploratory Data Analysis (EDA)
├── src/            → Source code utama (data ingestion, training, dll)
│   └── hello.py    → Script coba-coba saat setup
├── config/         → File konfigurasi (parameter, setting, dsb)
├── tests/          → Unit testing
├── docs/           → Dokumentasi tambahan
├── .gitignore      → File untuk mengabaikan file/folder tertentu di Git
├── LICENSE         → Lisensi proyek
└── README.md       → Dokumentasi utama proyek
```

Lk - 04
1. Mengambil Data (Data Ingestion)
Jalankan skrip ini untuk menarik data terbaru dan menyimpannya di folder data/raw/.


python src/ingest_data.py
2. Membersihkan Data (Preprocessing)
Jalankan skrip ini untuk membuang data yang rusak/kosong dan merapikan formatnya. Hasilnya akan muncul di folder data/processed/.


python src/preprocess.py
 
Penjelasan File Utama
ingest_data.py: Bertugas sebagai "pengumpul data". Skrip ini memastikan data masuk ke sistem dengan aman tanpa mengubah isi aslinya.

preprocess.py: Bertugas sebagai "penyaring data". Skrip ini melakukan pembersihan (cleaning) seperti menghapus nilai kosong dan menyeragamkan format teks.

traffic_data_raw.csv: Sampel data yang berisi informasi jumlah kendaraan, waktu, dan kondisi cuaca di lokasi sensor.## Menjalankan skrip pengumpul data (singkat)
Prasyarat: Python dan paket `yfinance`, `pandas`.

Jalankan:
```
python src\ingest_data.py
```

Output: file di `data/raw/` bernama `oil_YYYY-MM-DD.csv`.

## Alur Penambahan Versi Data (Continual Learning dengan DVC)

Proyek ini mengimplementasikan pelacakan silsilah data (*data lineage*) menggunakan **Data Version Control (DVC)**. Berikut adalah alurnya:

1. **Inisialisasi Data Awal (v1):** Data harga minyak mentah (`CL=F`) diunduh menggunakan skrip `src/ingest_data.py` dan disimpan ke dalam file `data/raw/oil.csv`. File mentah ini dilacak menggunakan DVC dengan perintah `dvc add data/raw/oil.csv`. Metadata pelacakan (file `.dvc` dan `.gitignore`) kemudian disimpan ke dalam Git.
2. **Simulasi Continual Learning:** Untuk menyimulasikan berjalannya waktu dan masuknya data baru, skrip ingesti dijalankan kembali. Skrip secara otomatis akan mengambil data terbaru dan menggabungkannya ke file CSV yang sudah ada tanpa duplikasi.
3. **Pembaruan Versi Data (v2):** Setelah file dataset membesar karena adanya tambahan data baru, DVC digunakan kembali untuk melacak perubahannya (`dvc add`). DVC mendeteksi adanya perubahan ukuran (*size*) dan menghasilkan *hash value* (MD5) yang baru.
4. **Audit & Penyimpanan:** Perubahan metadata versi 2 ini (*hash* baru) di-*commit* kembali ke dalam Git. Hal ini memungkinkan kita untuk melakukan *rollback* ke versi data tanggal tertentu (v1 atau v2) di masa depan jika performa model menurun akibat data yang tidak valid.
## Model yang Digunakan
Model yang digunakan untuk prediksi:

- Nama: harga_minyak_model
- Versi: 3
- Stage: Production

Model ini dipilih karena memiliki nilai RMSE paling kecil.

---

## Data Versioning (DVC)
Dataset dikelola menggunakan DVC agar perubahan data dapat dilacak.
    