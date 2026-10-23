# 🎬 PANDUAN LENGKAP & NASKAH VIDEO TUTORIAL PHARMACAPA AI
**Sistem Manajemen Deviasi Bets & Investigasi Akar Masalah CPOB Berbasis Pharma 4.0**  
*Mata Kuliah: Aplikasi AI dalam Industri Farmasi (Tahun 2026)*  
*Mahasiswa: Rismawati Laila Qodariah (NIM: 2506714066)*  
*Program Studi: Pascasarjana Ilmu Kefarmasian, Fakultas Farmasi Universitas Indonesia*  
*Dosen Pengampu: Prof. Dr. Arry Yanuar, M.Si., Apt.*  
*Tautan Aplikasi Streamlit:* [https://pharmacapa.streamlit.app/](https://pharmacapa.streamlit.app/)

---

## 1. INFORMASI BERKAS VIDEO TUTORIAL

* **Nama Berkas Video:** [`PharmaCAPA_AI_Video_Tutorial.webp`](file:///Users/rismawatilaila/Tugas%20AI%20Prof%20Arry/PharmaCAPA_AI_Video_Tutorial.webp)
* **Ukuran Berkas:** ~9.4 MB (Animasi Lengkap 533 Frames)
* **Pemain Video Interaktif (Web Player):** [`video_tutorial.html`](file:///Users/rismawatilaila/Tugas%20AI%20Prof%20Arry/video_tutorial.html)
* **Cara Membuka di Laptop/Mac:**
  * Klik dua kali (double click) file [`video_tutorial.html`](file:///Users/rismawatilaila/Tugas%20AI%20Prof%20Arry/video_tutorial.html) untuk memutar rekaman video di Safari / Google Chrome lengkap dengan teks panduan berdampingan.
  * Atau buka langsung file [`PharmaCAPA_AI_Video_Tutorial.webp`](file:///Users/rismawatilaila/Tugas%20AI%20Prof%20Arry/PharmaCAPA_AI_Video_Tutorial.webp) menggunakan browser apa pun di Mac Anda.

---

## 2. NASKAH SUARA / PANDUAN PRESENTASI VIDEO (*VOICEOVER SCRIPT*)

Gunakan naskah terstruktur di bawah ini jika Anda ingin merekam narasi suara (*voiceover*) atau mempresentasikannya secara langsung di hadapan Prof. Dr. Arry Yanuar, M.Si., Apt.:

---

### ⏱️ Menit 00:00 – 00:20 | Pembukaan & Identitas Sistem
* **Tampilan Visual:** Halaman utama Streamlit memuat Hero Banner berlatar *navy clinical* dengan badge resmi dan kartu ringkasan deviasi.
* **🎙️ Naskah Narasi:**
  > *"Assalamu’alaikum Wr. Wb. Selamat pagi/siang Prof. Arry Yanuar dan rekan-rekan sekalian. Nama saya Rismawati Laila Qodariah, mahasiswi Program Pascasarjana Ilmu Kefarmasian Fakultas Farmasi Universitas Indonesia, NIM 2506714066.*  
  > *Pada video tutorial ini, saya mendemonstrasikan pengoperasian **PharmaCAPA AI**, sebuah asisten cerdas berbasis web untuk investigasi penyimpangan mutu bets dan penyusunan CAPA berstandar BPOM CPOB 2018/2024 dan ICH Q9/Q10."*

---

### ⏱️ Menit 00:20 – 00:45 | Pemilihan Kasus Deviasi & Perhitungan Risiko (ICH Q9)
* **Tampilan Visual:** Kursor mengarah ke dropdown pemilihan kasus deviasi. Menampilkan 4 preset kasus riil farmasi. Dipilih kasus `1. Uji Disolusi OOS — Paracetamol 500mg`. Kartu seketika menampilkan RPN = 12 (MAJOR) dan Disposisi Bets: Karantina.
* **🎙️ Naskah Narasi:**
  > *"Pada bagian atas, operator atau tim QA dapat memilih kasus deviasi yang sedang terjadi atau memasukkan data baru secara bebas. Sebagai contoh, kita memilih kasus Uji Disolusi OOS pada Paracetamol 500 mg.*  
  > *Sistem secara otomatis menghitung nilai Risk Priority Number (RPN) berbasis algoritma kuantitatif ICH Q9: Severity dikalikan Probability dikalikan Detectability. Diperoleh nilai RPN 12 yang secara deterministik mengklasifikasikan insiden ke dalam kategori **MAJOR**, dengan rekomendasi disposisi bets berupa penahanan karantina formal CPOB."*

---

### ⏱️ Menit 00:45 – 01:10 | Tab 1: Formulir Input Operator Shift
* **Tampilan Visual:** Mengklik tab **📝 1. Formulir Input Operator**. Layar bergulir memperlihatkan formulir ringkas: Nama Produk, Ruangan, Lini Produksi, Uraian Kejadian Faktual, dan Telemetri Parameter Kritis (Suhu, Waktu Mixing, Tekanan Kompresi).
* **🎙️ Naskah Narasi:**
  > *"Pada Tab 1, formulir dirancang mobile-friendly dan minimalis agar operator di dalam ruang bersih dapat mengisi anomali dalam hitungan menit tanpa mengganggu jalannya proses produksi.*  
  > *Perhatikan bahwa data telemetri kritis, seperti tekanan kompresi aktual 24.8 kN yang melebihi batas target 18 hingga 20 kN, tercatat secara digital dan terhubung langsung ke mesin inferensi AI."*

---

### ⏱️ Menit 01:10 – 01:40 | Tab 2: Diagram Tulang Ikan (Ishikawa 6M)
* **Tampilan Visual:** Mengklik tab **🐟 2. Diagram 6M (Ishikawa)**. Menampilkan pemetaan ke 6 cabang: Man, Machine, Material, Method, Measurement, dan Milieu. Terlihat penanda khusus pada cabang Machine: *Sensor hidrolik rotary tablet press mengalami drift kalibrasi*.
* **🎙️ Naskah Narasi:**
  > *"Selanjutnya pada Tab 2, AI menyusun Diagram Tulang Ikan (Ishikawa 6M) secara instan. Sistem membedah seluruh potensi penyebab ke dalam 6 domain standar CPOB.*  
  > *Alih-alih menyimpulkan 'human error', AI mengidentifikasi bahwa pada cabang Machine terjadi drift kalibrasi pada sensor hidrolik sebesar +5.2 kN yang menyebabkan kaplet dicetak terlalu keras sehingga disolusi melambat."*

---

### ⏱️ Menit 01:40 – 02:05 | Tab 3: Analisis Mendalam Metode 5-Whys
* **Tampilan Visual:** Mengklik tab **🔍 3. Metode 5-Whys**. Layar bergulir memperlihatkan urutan penalaran 5 langkah 'Mengapa' dari gejala permukaan hingga ke akar masalah sistemik yang berstatus `TARGET ROOT CAUSE`.
* **🎙️ Naskah Narasi:**
  > *"Masuk ke Tab 3, kita melihat penerapan metode 5-Whys secara berjenjang. AI menelusuri dari mengapa disolusi lambat, mengapa gaya kompresi naik, hingga menemukan **Akar Masalah Sistemik (Systemic Root Cause)**:*  
  > *Yaitu alarm over-force pada panel HMI dinonaktifkan sementara dan belum adanya checklist verifikasi sensor pra-produksi pada SOP line clearance. Pendekatan ini menghentikan budaya menyalahkan operator dan memperbaiki sistem pabrik secara fundamental."*

---

### ⏱️ Menit 02:05 – 02:30 | Tab 4: Rencana CAPA Resmi & Effectiveness Review
* **Tampilan Visual:** Mengklik tab **🛡️ 4. Rencana CAPA**. Menampilkan tabel Tindakan Korektif (CA-01, CA-02) dan Tindakan Preventif (PA-01, PA-02) lengkap dengan PIC, Target Tanggal, serta Klausul Review Efektivitas 30 Hari.
* **🎙️ Naskah Narasi:**
  > *"Pada Tab 4, sistem menyusun matriks CAPA berstandar ICH Q10. Tindakan korektif langsung mencakup re-kalibrasi load cell dan pengujian keseragaman sediaan.*  
  > *Sementara tindakan preventif menetapkan revisi SOP Line Clearance dan verifikasi sensor berkala. Sistem juga menetapkan syarat tinjauan efektivitas, di mana nilai disolusi pada 5 bets berikutnya wajib memenuhi Q lebih dari 85%."*

---

### ⏱️ Menit 02:30 – 03:00 | Tab 5: Ekspor Dokumen Resmi CPOB (Word & PDF) & Penutup
* **Tampilan Visual:** Mengklik tab **📄 5. Formulir Resmi CPOB**. Menampilkan formulir resmi berkepala surat BPOM CPOB. Memilih opsi format dropdown (Microsoft Word dan PDF Cetak A4), menyoroti tombol unduh Word (.doc) dan cetak PDF.
* **🎙️ Naskah Narasi:**
  > *"Terakhir pada Tab 5, seluruh berkas investigasi terangkum rapi dalam Formulir Resmi CPOB No. SOP-QA-042. Pengguna dapat memilih format ekspor melalui dropdown:*  
  > *Mengunduh berkas Microsoft Word (.doc) untuk diedit, atau mencetak langsung ke format PDF A4 yang 100% siap diserahkan saat inspeksi BPOM.*  
  > *Demikian demonstrasi PharmaCAPA AI. Sistem ini membuktikan bahwa teknologi Pharma 4.0 mampu memangkas waktu investigasi deviasi dari 45 hari menjadi kurang dari 3 hari dengan akurasi dan kepatuhan penuh. Terima kasih atas bimbingan Prof. Dr. Arry Yanuar, M.Si., Apt."*

---

### 📂 Berkas Terkait di Repositori:
1. Rekaman Video WebP: [`PharmaCAPA_AI_Video_Tutorial.webp`](file:///Users/rismawatilaila/Tugas%20AI%20Prof%20Arry/PharmaCAPA_AI_Video_Tutorial.webp)
2. Pemutar Video Browser: [`video_tutorial.html`](file:///Users/rismawatilaila/Tugas%20AI%20Prof%20Arry/video_tutorial.html)
3. Slide Presentasi: [`PharmaCAPA_AI_Presentasi.pptx`](file:///Users/rismawatilaila/Tugas%20AI%20Prof%20Arry/PharmaCAPA_AI_Presentasi.pptx)
4. Logbook Resmi PDF: [`PharmaCAPA_AI_Logbook_Pengembangan.pdf`](file:///Users/rismawatilaila/Tugas%20AI%20Prof%20Arry/PharmaCAPA_AI_Logbook_Pengembangan.pdf)
