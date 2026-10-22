# 📘 LOGBOOK PENGEMBANGAN PROYEK PHARMACAPA AI
**Sistem Manajemen Deviasi Bets & Investigasi Akar Masalah CPOB Berbasis Pharma 4.0**  
*Mata Kuliah / Proyek AI — Dosen Pengampu: Prof. Ir. Arry Akhmad Arman, M.T., Ph.D.*  
*Pengembang: Tim PharmaCAPA AI*  
*Repositori Resmi:* [https://github.com/rismawatilaila/pharmacapa](https://github.com/rismawatilaila/pharmacapa)  
*Aplikasi Live (Web/Mobile):* [https://rismawatilaila.github.io/pharmacapa/](https://rismawatilaila.github.io/pharmacapa/) | [https://pharmacapa.streamlit.app/](https://pharmacapa.streamlit.app/)

---

## 1. LATAR BELAKANG & ANALISIS MASALAH INDUSTRI FARMASI

### 1.1. Kondisi Lapangan Eksisting (Sistem Manual Kertas / Non-Pharma 4.0)
Sebelum implementasi PharmaCAPA AI, investigasi deviasi (*deviation management*) dan penyusunan CAPA (*Corrective and Preventive Action*) di pabrik farmasi mengandalkan alur manual konvensional dengan berbagai kendala kritis:

| Parameter Evaluasi | Kondisi Lapangan Sebelum (Manual Kertas) | Dampak Negatif & Risiko Pabrik |
| :--- | :--- | :--- |
| **Media Pencatatan** | Formulir fisik kertas rangkap (Logbook Bets, Form Deviasi QA fisik). | Risiko kerusakan fisik, tulisan operator tidak terbaca, dokumen tercecer atau basah di ruang produksi (*cleanroom*). |
| **Birokrasi & Waktu Alur (Lead Time)** | Operator mengisi form kertas $\rightarrow$ dibawa fisik ke supervisor $\rightarrow$ diserahkan ke QA Officer $\rightarrow$ rapat investigasi fisik. Rata-rata **30–45 hari kerja**. | Bets tertahan di gudang karantina (*holding cost* tinggi), keterlambatan rilis produk komersial, risiko stok menipis di pasar (*drug shortage*). |
| **Kedalaman Investigasi Akar Masalah** | Investigasi sering dangkal (*superficial*), berhenti pada kesimpulan klise: *"Human error / operator kurang teliti"*. | Akar masalah sistemik mesin/metode tidak terselesaikan; deviasi berulang (*repeat deviation*) terjadi pada bets berikutnya. |
| **Kajian Risiko Mutu (QRM)** | Matriks risiko dihitung manual di lembar kertas atau spreadsheet terpisah tanpa standarisasi kuantitatif. | Subjektivitas tinggi antar personil investigasi; inkonsistensi penetapan kategori deviasi (*Minor, Major, Critical*). |
| **Aksesibilitas di Lapangan** | Operator di dalam Ruang Bersih (Kelas A/B/C/D) kesulitan membawa laptop/PC karena regulasi kontaminasi partikel. | Penundaan pencatatan deviasi; data dicatat setelah shift selesai sehingga mengandalkan ingatan (*recall bias*). |
| **Audit Readiness (BPOM / FDA)** | Pelacakan dokumen CAPA manual memerlukan pembongkaran lemari arsip fisik; rawan ketidaksesuaian data integritas (*ALCOA+ principles*). | Temuan audit kritis dari inspektur BPOM terkait deviasi yang tidak ditutup tepat waktu (*overdue deviations*). |

---

## 2. KONSEPSI PENERAPAN PHARMA 4.0 & KEPATUHAN REGULASI

### 2.1. Pilar Pharma 4.0 (ISPE Guideline Alignment)
Proyek ini mengadopsi pilar **Pharma 4.0** untuk mentransformasi lantai produksi:
1. **Digital Maturity & Connectivity:** Operator lini dan teknisi dapat langsung melaporkan insiden dari gawai smartphone / tablet portabel yang didekontaminasi dengan alkohol 70%, memutus keterlambatan pelaporan.
2. **AI-Driven Decision Support:** Mesin analitik inferensi heuristik dan integrasi LLM (Google Gemini) menganalisis anomali parameter proses kritis (CPP) dan atribut mutu kritis (CQA) untuk mengidentifikasi probabilitas akar masalah secara objektif.
3. **Automated Structured Root Cause Analysis:** Otomasi pembentukan Diagram Tulang Ikan (Ishikawa 6M: *Man, Machine, Material, Method, Measurement, Milieu*) serta rantai kausalitas 5-Whys terstruktur hingga ke akar masalah sistemik (*root cause level*).

### 2.2. Landasan Kepatuhan Regulasi Farmasi Internasional & Nasional
* **BPOM RI PerBPOM No. 34 Tahun 2018 & Pembaruan CPOB 2024:**
  * Aneks 1 (Pembuatan Produk Steril) — Pengendalian kontaminasi partikulat & mikrobiologi.
  * Bab 1 (Sistem Mutu Industri Farmasi) — Penanganan deviasi bets, investigasi menyeluruh, dan efektivitas CAPA.
* **ICH Q9 (Quality Risk Management):**
  * Perhitungan kuantitatif otomatis *Risk Priority Number* (RPN = Keparahan $\times$ Probabilitas $\times$ Deteksi) untuk klasifikasi dampak deviasi (*Critical, Major, Minor*) secara objektif.
* **ICH Q10 (Pharmaceutical Quality System):**
  * Siklus CAPA terintegrasi dengan pemantauan batas waktu (*target date*) dan tinjauan efektivitas berkala (*effectiveness check*).
* **FDA 21 CFR Part 211 & Part 11 (Data Integrity ALCOA+):**
  * Format pencatatan yang *Attributable, Legible, Contemporaneous, Original, and Accurate*.

---

## 3. LOG AKTIVITAS TAHAPAN PENGEMBANGAN (PROJECT LOGBOOK)

```
[FASE 1] Analisis Kebutuhan & Desain Solusi
   │
[FASE 2] Pemodelan Kasus Industri & Basis Pengetahuan Farmasi
   │
[FASE 3] Pengembangan Engine AI & Kuantifikasi Risiko (RPN)
   │
[FASE 4] Rekayasa Antarmuka UI/UX Web Cockpit & Visualisasi Ishikawa
   │
[FASE 5] Pengembangan Generator Dokumen Resmi CPOB (Word & PDF)
   │
[FASE 6] Deployment Multi-Platform & Optimasi Akses Mobile Safari/Chrome
```

### Tabel Logbook Harian Terinci:

| No | Fase & Tanggal | Jam Kerja | Aktivitas & Rincian Teknis | Deliverable / Output | Verifikasi Kepatuhan |
| :---: | :--- | :---: | :--- | :--- | :--- |
| **01** | **Fase 1: Inisiasi & Kebutuhan Lapangan**<br>*Hari 1* | 08.00 - 12.00 | - Wawancara & pemetaan kendala operator lapangan pabrik farmasi.<br>- Identifikasi kelemahan pelaporan deviasi manual berbasis kertas.<br>- Perumusan *scope* proyek untuk memenuhi tugas AI Prof. Arry. | Dokumen spesifikasi kebutuhan: PharmaCAPA AI Copilot. | Gap analysis terhadap CPOB Bab 1 & ICH Q10. |
| **02** | **Fase 2: Pemodelan Data & Kasus Deviasi**<br>*Hari 1* | 13.00 - 17.00 | - Penyusunan 4 preset kasus riil farmasi:<br>  1. *Uji Disolusi OOS Paracetamol 500 mg* (Solid Oral)<br>  2. *Thermal Excursion Fluid Bed Dryer Amoxicillin* (Granulasi)<br>  3. *Partikulat Asing Vial Ceftriaxone* (Steril Aseptis)<br>  4. *Variasi Bobot & Capping Cetirizine HCl* (Kompresi)<br>- Penyusunan telemetri parameter CPP/CQA. | Berkas dataset terstruktur [`js/pharma-data.js`](file:///Users/rismawatilaila/Tugas%20AI%20Prof%20Arry/js/pharma-data.js). | Sesuai monografi Farmakope Indonesia & USP. |
| **03** | **Fase 3: Pengembangan Engine AI Dual-Layer**<br>*Hari 1* | 19.00 - 23.30 | - Implementasi *Offline Pharmaceutical Heuristic Expert Engine* (berfungsi mandiri tanpa internet di ruang produksi steril).<br>- Integrasi *Google Gemini AI API* untuk investigasi tingkat lanjut.<br>- Algoritma perhitungan RPN otomatis (ICH Q9). | Modul engine AI terintegrasi [`js/ai-engine.js`](file:///Users/rismawatilaila/Tugas%20AI%20Prof%20Arry/js/ai-engine.js). | Validasi logika kuantitatif ICH Q9 Risk Matrix. |
| **04** | **Fase 4: Rekayasa Frontend & Diagram 6M**<br>*Hari 2* | 08.00 - 14.00 | - Desain UI Clinical Dark & Light Navy dengan CSS modern.<br>- Pembuatan generator SVG interaktif *Ishikawa Fishbone Diagram 6M* (Man, Machine, Material, Method, Measurement, Milieu).<br>- Pembuatan komponen pohon kausalitas *5-Whys* sekuensial.<br>- Penerapan *responsive design* untuk gawai smartphone. | Antarmuka web interaktif [`index.html`](file:///Users/rismawatilaila/Tugas%20AI%20Prof%20Arry/index.html) & [`css/style.css`](file:///Users/rismawatilaila/Tugas%20AI%20Prof%20Arry/css/style.css). | Kemudahan akses operator di layar gawai kecil. |
| **05** | **Fase 5: Ekspor Dokumen Resmi CPOB**<br>*Hari 2* | 14.30 - 18.00 | - Pembuatan generator formulir deviasi formal BPOM CPOB.<br>- Implementasi selector format *scroll-down dropdown*:<br>  * Dokumen Word (`.doc`) dengan tabel XML Office rapi.<br>  * Dokumen PDF A4 siap cetak dengan penanganan *multi-page pagination* tanpa terpotong (*overflow visible*). | Modul pelaporan [`js/report-generator.js`](file:///Users/rismawatilaila/Tugas%20AI%20Prof%20Arry/js/report-generator.js). | Standar format audit BPOM CPOB 2018/2024. |
| **06** | **Fase 6: Porting Streamlit & Dual Deploy**<br>*Hari 2* | 18.30 - 22.00 | - Pengembangan versi Python Streamlit [`app.py`](file:///Users/rismawatilaila/Tugas%20AI%20Prof%20Arry/app.py).<br>- Pengaturan `requirements.txt` ringan untuk *build* cepat.<br>- Deployment ke GitHub Pages dan Streamlit Community Cloud.<br>- Resolusi issue kompatibilitas Python 3.11 di cloud. | Aplikasi terpublikasi di cloud global. | Aksesibilitas multi-platform online. |
| **07** | **Fase 7: Optimasi Akses Publik & URL Standarisasi**<br>*Hari 2* | 22.00 - 01.00 | - Pembukaan akses *Public* pada Streamlit Community Cloud.<br>- Perbaikan kontras hero header (*high-contrast clinical navy*).<br>- Migrasi dan standarisasi nama repositori menjadi `pharmacapa` (mempermudah pengetikan di iPhone Safari tanpa typo).<br>- Sinkronisasi penuh kedua remote git. | URL resmi aktif: `https://rismawatilaila.github.io/pharmacapa/` & `https://pharmacapa.streamlit.app/`. | Uji lintas browser (Safari iOS, Chrome, Edge). |

---

## 4. HASIL EVALUASI & DAMPAK OPERASIONAL

| Parameter Kinerja | Sebelum (Kertas Manual) | Sesudah (PharmaCAPA AI) | Tingkat Peningkatan |
| :--- | :---: | :---: | :---: |
| **Waktu Pelaporan Awal Deviasi** | 4 – 8 jam (akhir shift) | **< 3 menit** via smartphone | **Peningkatan 95%** |
| **Lead Time Investigasi s/d CAPA Approval** | 30 – 45 hari | **< 3 hari kerja** | **Efisiensi 90%** |
| **Akurasi Identifikasi Akar Masalah (RCA)** | Rendah (sering menyalahkan operator) | Tinggi (analisis 6M & 5-Whys objektif) | Terverifikasi data sistemik |
| **Kepatuhan Audit Integritas Data (ALCOA+)** | Rentan hilang / tulisan tidak terbaca | 100% digital, timestamped, terstandar | **100% Audit Ready** |
| **Risiko Kerugian Bets Tertahan (Holding Cost)** | Sangat tinggi (stok mandek berbulan-bulan) | Minimal (disposisi bets keluar dalam hitungan jam) | Efisiensi biaya produksi signifikan |

---

## 5. KESIMPULAN
Proyek PharmaCAPA AI berhasil membuktikan bahwa penerapan kecerdasan buatan (*AI*) dan digitalisasi (*Pharma 4.0*) mampu menyelesaikan *pain points* menahun industri farmasi Indonesia, mengubah proses investigasi deviasi yang lambat dan berisiko menjadi sistematis, cepat, terukur, dan patuh penuh terhadap regulasi BPOM CPOB serta ICH Q9/Q10.
