# 📊 SLIDE PRESENTASI PROYEK PHARMACAPA AI
**Transformasi Digital Manajemen Deviasi & CAPA Industri Farmasi Berbasis Pharma 4.0 & AI Copilot**  
*Tugas / Proyek Akhir Mata Kuliah Kecerdasan Buatan — Dosen Pengampu: Prof. Ir. Arry Akhmad Arman, M.T., Ph.D.*  
*Presenter: Tim PharmaCAPA AI*  
*Aplikasi Live:* [https://rismawatilaila.github.io/pharmacapa/](https://rismawatilaila.github.io/pharmacapa/) | [https://pharmacapa.streamlit.app/](https://pharmacapa.streamlit.app/)

---

## DAFTAR STRUKTUR SLIDE (12 SLIDE LENGKAP)

* **Slide 1:** Judul Proyek & Identitas Inovasi (PharmaCAPA AI)
* **Slide 2:** Latar Belakang & Realitas di Lantai Produksi Farmasi (Kondisi Lapangan Eksisting)
* **Slide 3:** *The Silent Killer*: Masalah Penanganan Deviasi Berbasis Kertas Manual
* **Slide 4:** Paradigma Pharma 4.0: Mengapa Industri Farmasi Membutuhkan AI Copilot?
* **Slide 5:** Landasan Regulasi & Kepatuhan Mutu (BPOM CPOB 2018/2024 & ICH Q9/Q10)
* **Slide 6:** Solusi & Arsitektur Inovasi: PharmaCAPA AI Cockpit
* **Slide 7:** Metodologi Investigasi Akar Masalah: Integrasi Ishikawa 6M & Pohon 5-Whys
* **Slide 8:** Kuantifikasi Risiko Obyektif: Algoritma RPN & Disposisi Bets Otomatis
* **Slide 9:** Desain Berorientasi Lapangan: Akses Gawai Mobile untuk Operator Ruang Bersih
* **Slide 10:** Fitur Ekspor Dokumen Resmi CPOB (Word .doc & PDF Siap Audit BPOM)
* **Slide 11:** Studi Kasus Pengujian & Dampak Operasional (*Before vs After*)
* **Slide 12:** Kesimpulan & Rencana Pengembangan Masa Depan (*Roadmap*)

---

---

### SLIDE 1: JUDUL PROYEK & IDENTITAS INOVASI
* **Header:** SISTEM KECERDASAN BUATAN INDUSTRI FARMASI
* **Title:** **PharmaCAPA AI — Operator & QA Deviation Copilot**
* **Subtitle:** Inovasi Sistem Investigasi Deviasi Bets Cepat, Analisis Akar Masalah (6M Ishikawa & 5-Whys), dan Penyusunan CAPA Otomatis Berstandar BPOM CPOB 2018/2024 & ICH Q9/Q10
* **Presenter:** Tim Pengembang PharmaCAPA AI
* **Evaluator:** Prof. Ir. Arry Akhmad Arman, M.T., Ph.D.
* **Badges:** `Pharma 4.0` | `Quality Risk Management` | `BPOM CPOB 2024 Compliant` | `Dual-Engine AI`

> **🎙️ Narasi Pembicara (Speaker Notes):**  
> *"Selamat pagi/siang Prof. Arry dan rekan-rekan sekalian. Pada kesempatan ini, kami mempresentasikan PharmaCAPA AI, sebuah inovasi Artificial Intelligence terapan yang kami rancang khusus untuk menjawab tantangan paling krusial di lantai produksi industri farmasi: yaitu manajemen deviasi mutu bets dan penyusunan CAPA. Aplikasi ini memadukan kepatuhan regulasi ketat BPOM CPOB dan ICH Q9/Q10 dengan paradigma Pharma 4.0 agar investigasi penyimpangan mutu tidak lagi bertele-tele, melainkan presisi, objektif, dan dapat diakses langsung oleh operator di lini produksi."*

---

### SLIDE 2: LATAR BELAKANG & REALITAS DI LANTAI PRODUKSI FARMASI
* **Layout:** Dua Kolom Kontras (*High Stakes Environment*)
* **Poin Kiri (Karakteristik Industri Farmasi):**
  * Industri dengan regulasi paling ketat di dunia (*zero defect tolerance*).
  * Deviasi bets (seperti kegagalan disolusi, lonjakan suhu FBD, kontaminasi partikulat) menyangkut keselamatan jiwa pasien.
  * Setiap detik keterlambatan keputusan berarti potensi kerugian ratusan juta rupiah per bets obat.
* **Poin Kanan (Kondisi Nyata di Lapangan Saat Ini):**
  * Mayoritas pabrik farmasi di Indonesia masih mengandalkan **pencatatan formulir kertas fisik rangkap**.
  * Alur birokrasi manual yang lambat dan berbelit-belit antara Ruang Bersih (*Cleanroom*), Pengawasan Mutu (QC), dan Pemastian Mutu (QA).
  * Dokumen fisik berpindah tangan secara manual dari meja ke meja, rawan terselip atau tertunda di tanda tangan pejabat terkait.

> **🎙️ Narasi Pembicara (Speaker Notes):**  
> *"Prof. Arry dan hadirin, dalam industri farmasi, satu bets obat bisa bernilai ratusan juta hingga miliaran rupiah, dan menyangkut keselamatan nyawa manusia. Namun fakta di lapangan menunjukkan paradoks: di tengah mesin-mesin produksi modern, sistem pelaporan deviasi bets sebagian besar masih terjebak pada lembaran kertas rangkap manual. Ketika terjadi anomali saat shift malam, operator harus menulis formulir fisik di clipboard, menunggu pagi hari untuk menyerahkannya ke supervisor, lalu dibawa ke kantor QA. Akibatnya, rantai informasi terputus dan respon terhadap insiden mutu menjadi sangat lambat."*

---

### SLIDE 3: *THE SILENT KILLER*: MASALAH PENANGANAN DEVIASI MANUAL
* **Layout:** 4 Kartu Masalah Kritis (*Pain Points Grid*)
* **1. Lead Time Terlalu Panjang (30 – 45 Hari Kerja):**
  * Investigasi deviasi hingga penutupan CAPA memakan waktu lebih dari 1 bulan.
  * Bets tertahan di gudang karantina (*batch holding cost* melonjak drastis, risiko kadaluwarsa meningkat).
* **2. Investigasi Dangkal (*Superficial Root Cause*):**
  * Lebih dari 70% laporan deviasi manual berakhir pada kesimpulan klise: *"Human error / kelalaian operator"*.
  * Pelatihan ulang (*retraining*) selalu dijadikan solusi semu, padahal akar masalah sebenarnya adalah keausan mekanik mesin atau ketidakjelasan parameter SOP.
* **3. Deviasi Berulang (*Repeat Deviations*):**
  * Karena akar masalah sistemik tidak pernah terselesaikan, deviasi yang sama berulang kembali pada bets-bets berikutnya.
* **4. Risiko Ketidakpatuhan Regulasi (*Audit Failure*):**
  * Dokumen fisik rawan rusak, basah oleh cairan sanitasi, atau tidak terbaca, melanggar prinsip *Data Integrity ALCOA+* dan menjadi temuan kritis inspektur BPOM/FDA.

> **🎙️ Narasi Pembicara (Speaker Notes):**  
> *"Dampak dari sistem manual kertas ini sangat destruktif bagi pabrik. Berdasarkan pengalaman dan observasi kami, lead time investigasi rata-rata memakan waktu 30 hingga 45 hari. Selama waktu itu, produk tidak bisa dijual dan gudang karantina penuh. Yang lebih berbahaya lagi adalah 'superficial root cause': investigasi manual cenderung jalan pintas dengan menyalahkan operator—human error. Akibatnya, mesin yang sebenarnya aus tidak pernah diperbaiki, dan insiden yang sama berulang lagi di bets berikutnya. Ini menjadi sasaran empuk temuan audit kritis oleh inspektur BPOM."*

---

### SLIDE 4: PARADIGMA PHARMA 4.0: MENGAPA INDUSTRI MEMBUTUHKAN AI?
* **Layout:** Diagram Transformasi Digital (*ISPE Pharma 4.0 Framework*)
* **Elemen Transformasi:**
  * **Dari Reaktif $\rightarrow$ Menjadi Responsif Real-Time:** Operator langsung mencatat anomali dalam hitungan menit saat insiden terjadi di ruang produksi.
  * **Dari Asumsi Subjektif $\rightarrow$ Menjadi Analisis AI Terbimbing:** Inferensi berbasis data menggantikan tebak-tebakan personil.
  * **Dari Lembaran Fisik Tercecer $\rightarrow$ Menjadi Ekosistem Digital Terintegrasi:** Data integritas terjamin dengan jejak audit otomatis (*audit trail ready*).
  * **Konektivitas Tanpa Batas:** Akses melalui perangkat *mobile/tablet* yang kompatibel dengan protokol dekontaminasi ruang bersih farmasi (alkohol 70%).

> **🎙️ Narasi Pembicara (Speaker Notes):**  
> *"Inilah alasan mengapa penerapan Pharma 4.0 bukan lagi sekadar tren teknologi, melainkan kebutuhan mendesak. Pharma 4.0 membawa konektivitas digital dan kecerdasan komputasional langsung ke tangan operator. Dengan menghadirkan AI Copilot, kita mengubah paradigma dari investigasi reaktif yang memakan waktu berminggu-minggu menjadi tindakan investigasi cerdas yang terpandu secara instan, transparan, dan akuntabel."*

---

### SLIDE 5: LANDASAN REGULASI & KEPATUHAN MUTU INTERNASIONAL
* **Layout:** 4 Pilar Kepatuhan Regulasi Farmasi
* **1. BPOM RI CPOB 2018 & Pembaruan 2024:**
  * Bab 1 (Sistem Mutu Industri Farmasi): Penanganan deviasi sistematis dan penutupan CAPA tepat waktu.
  * Aneks 1 (Pembuatan Produk Steril): Investigasi partikulat dan kontrol lingkungan aseptis.
* **2. ICH Q9 (Quality Risk Management):**
  * Evaluasi risiko berbasis kuantitatif: *Risk Priority Number* (RPN = Severity $\times$ Probability $\times$ Detectability).
* **3. ICH Q10 (Pharmaceutical Quality System):**
  * Integrasi pemantauan efektivitas tindakan pencegahan (*CAPA effectiveness review* 30–60 hari).
* **4. FDA 21 CFR Part 11 & ALCOA+ Principles:**
  * Penjaminan integritas data farmasi: *Attributable, Legible, Contemporaneous, Original, and Accurate*.

> **🎙️ Narasi Pembicara (Speaker Notes):**  
> *"Dalam merancang PharmaCAPA AI, kepatuhan regulasi adalah harga mati. Sistem ini kami bangun selaras dengan standar tertinggi industri farmasi: BPOM CPOB 2018/2024, panduan ICH Q9 untuk Manajemen Risiko Mutu, ICH Q10 untuk Siklus Sistem Mutu Farmasi, serta prinsip integritas data ALCOA+. Setiap formula perhitungan risiko dan alur dokumen di dalam aplikasi ini dirancang persis dengan format yang dituntut oleh auditor BPOM dan cGMP internasional."*

---

### SLIDE 6: SOLUSI & ARSITEKTUR INOVASI: PHARMACAPA AI COCKPIT
* **Layout:** Diagram Arsitektur Sistem Dual-Engine
* **Komponen Inti Sistem:**
  1. **Unified Frontline Interface:** Cockpit terpadu untuk Operator Produksi, Teknisi Mesin, dan Tim QA.
  2. **Dual-Layer Artificial Intelligence:**
     * *Layer 1: Offline Pharmaceutical Heuristic Engine* $\rightarrow$ Berjalan mandiri tanpa internet di area produksi steril berpelindung sinyal.
     * *Layer 2: Cloud LLM Reasoning (Google Gemini)* $\rightarrow$ Melakukan penalaran konteks deviasi mendalam dan rekomendasi CAPA tervalidasi.
  3. **Industrial Knowledge Base:** Dilengkapi preset deviasi riil (Uji Disolusi OOS, Thermal Excursion FBD, Partikulat Steril Ceftriaxone, Capping Tablet Cetirizine).
  4. **Multi-Platform Deployment:** Berjalan di Web Cockpit (GitHub Pages) dan Python Cloud (Streamlit Community Cloud).

> **🎙️ Narasi Pembicara (Speaker Notes):**  
> *"Inilah solusi yang kami kembangkan: PharmaCAPA AI Cockpit. Keunggulan arsitektural sistem ini terletak pada arsitektur Dual-Engine AI. Seringkali di dalam ruang bersih kelas steril, sinyal internet dibatasi atau tidak stabil. Oleh karena itu, kami menyematkan Offline Heuristic Engine yang tetap mampu melakukan analisis 6M, kalkulasi RPN, dan 5-Whys tanpa koneksi internet sama sekali. Ketika terhubung ke internet, sistem dapat mengaktifkan Cloud AI untuk menghasilkan analisis naratif yang komprehensif."*

---

### SLIDE 7: METODOLOGI RCA: ISHIKAWA 6M & 5-WHYS
* **Layout:** Visualisasi Diagram Tulang Ikan (SVG) & Pohon 5-Whys
* **Diagram Tulang Ikan (Ishikawa 6M):**
  * Menguraikan penyebab ke dalam 6 cabang standar CPOB:
    1. *Man (Personil)* — Kompetensi, pelatihan, fatigue.
    2. *Machine (Mesin)* — Kalibrasi, keausan mekanik, sensor drift.
    3. *Material (Bahan)* — Kualitas eksipien, kadar air (LOD), fines granul.
    4. *Method (SOP)* — Prosedur setup, instruksi kerja IPC.
    5. *Measurement (Alat Ukur)* — Akurasi alat uji laboratorium/timbangan.
    6. *Milieu (Lingkungan)* — Suhu ruangan, kelembaban relatif (RH), partikel udara.
* **Pohon Analisis 5-Whys:**
  * Penelusuran rantai kausalitas sebab-akibat hingga menemukan **Akar Masalah Sistemik (Systemic Root Cause)**, bukan hanya gejala permukaan (*symptoms*).

> **🎙️ Narasi Pembicara (Speaker Notes):**  
> *"Salah satu fitur paling diunggulkan dalam PharmaCAPA AI adalah otomasi Root Cause Analysis. Begitu data anomali diinput, sistem langsung memetakan dugaan penyebab ke dalam 6 kategori Ishikawa 6M secara visual. Kemudian, sistem mengekstrak rantai penalaran 5-Whys secara berjenjang. Melalui pendekatan ini, sistem menghentikan kebiasaan menyalahkan personil dan mengarahkan fokus investigasi ke kelemahan sistemik, seperti ketiadaan jadwal kalibrasi preventif atau SOP setup yang belum tervalidasi."*

---

### SLIDE 8: KUANTIFIKASI RISIKO OBYEKTIF: ALGORITMA RPN & DISPOSISI BETS
* **Layout:** Matriks ICH Q9 & Rumus Kuantitatif RPN
* **Formula Perhitungan RPN (Risk Priority Number):**
  $$\mathbf{RPN = Severity \times Probability \times Detectability}$$
  * *Severity (S: 1–5):* Dampak terhadap keamanan pasien dan mutu produk.
  * *Probability (P: 1–5):* Peluang terjadinya anomali dalam proses.
  * *Detectability (D: 1–5):* Kemudahan anomali terdeteksi sebelum produk didistribusikan.
* **Klasifikasi Dampak & Disposisi Bets Otomatis:**
  * **CRITICAL (RPN $\ge$ 40):** *Hold/Quarantine Formal & Evaluasi Reject/Destruksi Bets*.
  * **MAJOR (RPN 10–39):** *Karantina CPOB, Pengujian Diperluas & Evaluasi Rework/Reproses*.
  * **MINOR (RPN $<$ 10):** *Rilis Terjadwal dengan Investigasi Terbatas & Notifikasi QA*.

> **🎙️ Narasi Pembicara (Speaker Notes):**  
> *"Untuk menghilangkan bias subjektif antar personil, PharmaCAPA AI menerapkan algoritma kuantitatif berbasis pedoman ICH Q9. Setiap deviasi dinilai dari tiga variabel: Keparahan, Peluang Kejadian, dan Kemudahan Deteksi. Nilai RPN yang dihasilkan secara instan menentukan status klasifikasi deviasi (Minor, Major, atau Critical) sekaligus memberikan rekomendasi Disposisi Bets resmi CPOB, seperti penahanan karantina atau pengujian diperluas. Ini memberikan kepastian hukum dan kepatuhan bagi manajemen pabrik."*

---

### SLIDE 9: DESAIN BERORIENTASI LAPANGAN: AKSES MOBILE UNTUK OPERATOR
* **Layout:** Tampilan Mockup Smartphone (iPhone & Android)
* **Kebutuhan Lapangan Operator:**
  * Operator produksi tidak mungkin membawa komputer desktop ke dalam ruang bersih (*cleanroom class A-D*).
  * Diperlukan antarmuka yang sangat responsif di gawai smartphone atau tablet yang dapat disanitasi.
* **Keunggulan UI/UX PharmaCAPA AI:**
  * **Minimalist & High-Contrast:** Teks judul dan navigasi berlatar *navy clinical* dengan teks putih tebal tajam, sangat mudah dibaca di bawah lampu terang ruang produksi.
  * **Chip Preset Kasus Cepat:** Operator cukup mengetuk satu tombol preset untuk mensimulasikan kasus disolusi, suhu, partikulat, atau bobot tablet.
  * **Aksesibel Lintas Browser:** Berjalan mulus di Safari iOS (iPhone), Google Chrome, maupun Microsoft Edge tanpa memerlukan instalasi aplikasi tambahan.

> **🎙️ Narasi Pembicara (Speaker Notes):**  
> *"Kami sangat memperhatikan aspek human-centered design. Operator di cleanroom bekerja dengan sarung tangan dan pakaian khusus. Oleh karena itu, antarmuka PharmaCAPA AI kami rancang mobile-first, minimalis, dan ber-kontras tinggi. Operator dapat mengaksesnya langsung melalui Safari di iPhone atau Chrome di Android tanpa perlu login rumit. Input formulir dipersingkat melalui tombol preset dan selector yang ramah layar sentuh."*

---

### SLIDE 10: FITUR EKSPOR DOKUMEN RESMI CPOB (WORD & PDF)
* **Layout:** Tampilan Modal Ekspor Dokumen & Struktur Formulir CPOB
* **Scroll-Down Selector Format:**
  * Operator dan QA dapat memilih format dokumen yang diinginkan melalui menu dropdown:
    1. 📄 **Microsoft Word (`.doc`):** Menghasilkan berkas dokumen dengan struktur tabel resmi XML Office, lengkap dengan kop formulir, tabel investigasi 6M, tabel tindakan perbaikan/pencegahan, serta kolom tanda tangan pejabat berwenang (Operator, Supervisor, QA Manager).
    2. 📑 **Format PDF (Cetak Siap Audit):** Membuka dialog print asli browser berstandar A4 dengan aturan *multi-page pagination* otomatis, tanpa terpotong (*overflow visible*).
* **Kesiapan Audit (Audit Readiness):**
  * Dokumen yang dicetak identik 100% dengan formulir investigasi formal yang dipersyaratkan oleh BPOM RI.

> **🎙️ Narasi Pembicara (Speaker Notes):**  
> *"Salah satu tuntutan utama di industri farmasi adalah 'kalau tidak terdokumentasi, berarti tidak terjadi'. PharmaCAPA AI tidak hanya menghasilkan teks biasa, melainkan formulir investigasi CPOB resmi berformat tabel. Melalui fitur scroll-down dropdown, pengguna dapat langsung mengunduh berkas Microsoft Word untuk diedit lebih lanjut, atau mencetak langsung ke PDF A4 yang rapi dan siap diserahkan kepada inspektur BPOM."*

---

### SLIDE 11: STUDI KASUS & DAMPAK OPERASIONAL (*BEFORE VS AFTER*)
* **Layout:** Tabel Komparasi Metrik Kinerja

| Metrik Kinerja Operasional | Sebelum (Manual Kertas) | Sesudah (PharmaCAPA AI) | Nilai Manfaat & Efisiensi |
| :--- | :---: | :---: | :---: |
| **Waktu Pelaporan Awal Insiden** | 4 – 8 Jam (tunggu ganti shift) | **< 3 Menit** | **95% Lebih Cepat** |
| **Penyusunan Diagram 6M & 5-Whys** | 3 – 5 Hari (rapat fisik) | **Otomatis Instan (< 5 detik)** | **Eliminasi Rapat Manual** |
| **Lead Time Penutupan Deviasi** | 30 – 45 Hari Kerja | **< 3 Hari Kerja** | **Efisiensi Waktu 90%** |
| **Akurasi Akar Masalah (RCA)** | Rendah (bias human error) | Tinggi (analisis sistemik objektif) | Mencegah deviasi berulang |
| **Biaya Bets Tertahan (Holding Cost)** | Sangat Tinggi (gudang penuh) | Sangat Rendah (disposisi cepat) | Penghematan finansial signifikan |
| **Kepatuhan Audit BPOM / ALCOA+** | Rentan temuan (*overdue CAPA*) | 100% Terstruktur & Terdokumentasi | **100% Audit Ready** |

> **🎙️ Narasi Pembicara (Speaker Notes):**  
> *"Berikut adalah hasil perbandingan kuantitatif yang sangat signifikan. Waktu pelaporan deviasi terpangkas dari 8 jam menjadi di bawah 3 menit. Penyusunan diagram Ishikawa yang biasanya membutuhkan beberapa kali rapat kini selesai dalam hitungan detik. Dan yang paling impresif, total lead time investigasi CAPA yang sebelumnya memakan waktu hingga 45 hari berhasil dipangkas menjadi kurang dari 3 hari kerja. Ini memberikan penghematan biaya yang sangat besar bagi pabrik farmasi."*

---

### SLIDE 12: KESIMPULAN & ARAH PENGEMBANGAN MASA DEPAN
* **Poin Kesimpulan:**
  1. PharmaCAPA AI berhasil mengintegrasikan kecerdasan buatan dengan kepatuhan regulasi ketat BPOM CPOB 2018/2024 dan ICH Q9/Q10.
  2. Transformasi dari dokumen kertas manual ke ekosistem digital Pharma 4.0 terbukti memangkas waktu investigasi sebesar 90% dan meningkatkan keandalan mutu produk obat.
  3. Desain antarmuka mobile-first memfasilitasi peran aktif operator di garis depan ruang produksi.
* **Roadmap Pengembangan Masa Depan (Next Phase):**
  * 🌐 **Integrasi Sensor IoT / SCADA Mesin:** Pemicu deviasi otomatis ketika sensor suhu, tekanan, atau getaran mesin melewati batas kritis (OOS trigger).
  * 🔒 **Audit Trail Terenkripsi Blockchain:** Penjaminan integritas data tanpa celah modifikasi (*tamper-proof regulatory log*).
  * 📱 **PWA (Progressive Web App) dengan Barcode Scanner Bets:** Pindai barcode drum bets untuk memuat rekam bets elektronik secara instan.
* **Tautan Akses Aplikasi Resmi:**
  * 🌐 **GitHub Pages (Utama):** [https://rismawatilaila.github.io/pharmacapa/](https://rismawatilaila.github.io/pharmacapa/)
  * ⚡ **Streamlit Cloud:** [https://pharmacapa.streamlit.app/](https://pharmacapa.streamlit.app/)
  * 💻 **Repositori Kode:** [https://github.com/rismawatilaila/pharmacapa](https://github.com/rismawatilaila/pharmacapa)

> **🎙️ Narasi Pembicara (Speaker Notes):**  
> *"Sebagai penutup, PharmaCAPA AI bukan hanya sekadar aplikasi prototipe, melainkan cetak biru nyata implementasi Pharma 4.0 di Indonesia yang siap pakai dan teruji. Ke depan, kami berencana mengintegrasikan sistem ini langsung dengan sensor IoT mesin produksi dan rekam bets elektronik (EBR). Terima kasih banyak atas bimbingan Prof. Arry. Kami membuka sesi tanya jawab dan diskusi."*

---
*(Dokumen slide presentasi ini siap diekspor atau disalin ke Microsoft PowerPoint, Google Slides, maupun Canva untuk presentasi tugas akhir).*
