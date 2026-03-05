## Struktur Direktori

Berikut struktur proyek yang digunakan:

```bash
MLOps-Sistem-Prediksi-Kondisi-Lalu-Lintas/
│
├── data/                      # Berkaitan dengan data yang diambil (data ada versioningnya)
│   ├── raw/                   # Data mentah dari API
│   └── processed/             # Data yang sudah dibersihkan
│
├── models/                    # Penyimpanan model hasil training
│
├── notebooks/                 # Eksperimen dan Exploratory Data Analysis
│
├── src/                       # Source code utama
│   └── hello.py               # Script coba coba saat setup
│
├── config/                    # File konfigurasi
│
├── tests/                     # Unit testing
│
├── docs/                      # Dokumentasi tambahan
│
├── .gitignore                 # File untuk mengabaikan file/folder tertentu di Git
├── LICENSE                    # Lisensi proyek
└── README.md                  # Dokumentasi utama proyekgit add README.md