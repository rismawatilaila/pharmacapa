"""
Script untuk mengenerate slide presentasi PowerPoint (.pptx) PharmaCAPA AI
Desain: 16:9 Widescreen, Clinical Navy Theme, Kartu Modern, Tabel Terstruktur, dan Speaker Notes.
"""

import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor

# Inisialisasi Presentasi 16:9
prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_slide_layout = prs.slide_layouts[6]

# Palet Warna Clinical Navy (Pharma 4.0)
COLOR_BG_DARK = RGBColor(11, 25, 44)         # #0b192c Dark Navy
COLOR_CARD_BG = RGBColor(19, 42, 69)         # #132a45 Card Navy
COLOR_CARD_BORDER = RGBColor(3, 105, 161)    # #0369a1 Border Blue
COLOR_CYAN_ACCENT = RGBColor(56, 189, 248)   # #38bdf8 Cyan
COLOR_WHITE = RGBColor(255, 255, 255)
COLOR_TEXT_MUTED = RGBColor(203, 213, 225)   # #cbd5e1 Light Slate
COLOR_BADGE_BG = RGBColor(2, 132, 199)       # #0284c7 Sky Blue
COLOR_WARNING_BG = RGBColor(180, 83, 9)      # Amber
COLOR_DANGER_BG = RGBColor(185, 28, 28)      # Red
COLOR_SUCCESS_BG = RGBColor(21, 128, 61)     # Green

def apply_background(slide):
    """Mewarnai latar belakang slide menjadi dark navy"""
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = COLOR_BG_DARK
    bg.line.fill.background()
    return bg

def add_header(slide, category, title, subtitle=None):
    """Membuat header standar dengan category badge, judul utama, dan garis pemisah"""
    # Badge Kategori
    badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.45), Inches(4.5), Inches(0.35))
    badge.fill.solid()
    badge.fill.fore_color.rgb = COLOR_BADGE_BG
    badge.line.color.rgb = COLOR_CYAN_ACCENT
    badge.line.width = Pt(1)
    tf = badge.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = f"✚ {category.upper()}"
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = COLOR_WHITE
    p.alignment = PP_ALIGN.CENTER
    
    # Judul Slide
    tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.85), Inches(11.7), Inches(0.6))
    tf2 = tb.text_frame
    tf2.word_wrap = True
    p2 = tf2.paragraphs[0]
    p2.text = title
    p2.font.size = Pt(22)
    p2.font.bold = True
    p2.font.color.rgb = COLOR_WHITE
    
    # Subtitle jika ada
    if subtitle:
        p3 = tf2.add_paragraph()
        p3.text = subtitle
        p3.font.size = Pt(12)
        p3.font.color.rgb = COLOR_CYAN_ACCENT

def add_card(slide, left, top, width, height, title, items, badge_text=None, border_color=COLOR_CARD_BORDER):
    """Membuat kartu informasi dengan border elegan dan list poin"""
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = COLOR_CARD_BG
    card.line.color.rgb = border_color
    card.line.width = Pt(1.5)
    
    tb = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.15), width - Inches(0.4), height - Inches(0.3))
    tf = tb.text_frame
    tf.word_wrap = True
    
    if badge_text:
        p_badge = tf.paragraphs[0]
        p_badge.text = f"[{badge_text.upper()}]"
        p_badge.font.size = Pt(10)
        p_badge.font.bold = True
        p_badge.font.color.rgb = COLOR_CYAN_ACCENT
        p_title = tf.add_paragraph()
    else:
        p_title = tf.paragraphs[0]
        
    p_title.text = title
    p_title.font.size = Pt(15)
    p_title.font.bold = True
    p_title.font.color.rgb = COLOR_WHITE
    
    for item in items:
        p = tf.add_paragraph()
        p.text = f"•  {item}"
        p.font.size = Pt(11.5)
        p.font.color.rgb = COLOR_TEXT_MUTED

def set_speaker_notes(slide, notes_text):
    """Menyematkan narasi pembicara pada notes slide"""
    notes_slide = slide.notes_slide
    notes_text_frame = notes_slide.notes_text_frame
    notes_text_frame.text = notes_text

# ==============================================================================
# SLIDE 1: COVER SLIDE
# ==============================================================================
s1 = prs.slides.add_slide(blank_slide_layout)
apply_background(s1)

# Hero Container Box
hero_box = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.2), Inches(1.0), Inches(10.9), Inches(5.5))
hero_box.fill.solid()
hero_box.fill.fore_color.rgb = COLOR_CARD_BG
hero_box.line.color.rgb = COLOR_CYAN_ACCENT
hero_box.line.width = Pt(2)

tb = s1.shapes.add_textbox(Inches(1.6), Inches(1.3), Inches(10.1), Inches(4.8))
tf = tb.text_frame
tf.word_wrap = True

p_badge = tf.paragraphs[0]
p_badge.text = "✚  SISTEM KECERDASAN BUATAN INDUSTRI FARMASI — PHARMA 4.0"
p_badge.font.size = Pt(12)
p_badge.font.bold = True
p_badge.font.color.rgb = COLOR_CYAN_ACCENT

p_title = tf.add_paragraph()
p_title.text = "PharmaCAPA AI — Operator & QA Deviation Copilot"
p_title.font.size = Pt(30)
p_title.font.bold = True
p_title.font.color.rgb = COLOR_WHITE

p_sub = tf.add_paragraph()
p_sub.text = "Sistem Manajemen Deviasi Bets Cepat, Analisis Akar Masalah (6M Ishikawa & 5-Whys), serta Penyusunan Dokumen CAPA Berstandar BPOM CPOB 2018/2024 & ICH Q9/Q10"
p_sub.font.size = Pt(14)
p_sub.font.color.rgb = COLOR_TEXT_MUTED

p_divider = tf.add_paragraph()
p_divider.text = "―" * 45
p_divider.font.color.rgb = COLOR_CARD_BORDER

p_meta1 = tf.add_paragraph()
p_meta1.text = "• Dosen Pengampu  : Prof. Ir. Arry Akhmad Arman, M.T., Ph.D."
p_meta1.font.size = Pt(13)
p_meta1.font.bold = True
p_meta1.font.color.rgb = COLOR_WHITE

p_meta2 = tf.add_paragraph()
p_meta2.text = "• Pengembang          : Tim PharmaCAPA AI"
p_meta2.font.size = Pt(13)
p_meta2.font.color.rgb = COLOR_TEXT_MUTED

p_meta3 = tf.add_paragraph()
p_meta3.text = "• Tautan Resmi         : https://rismawatilaila.github.io/pharmacapa/"
p_meta3.font.size = Pt(12)
p_meta3.font.bold = True
p_meta3.font.color.rgb = COLOR_CYAN_ACCENT

set_speaker_notes(s1, """Selamat pagi/siang Prof. Arry dan rekan-rekan sekalian.
Pada kesempatan ini kami mempresentasikan PharmaCAPA AI, sebuah inovasi kecerdasan buatan terapan untuk menjawab tantangan paling krusial di lantai produksi industri farmasi: investigasi deviasi mutu bets dan penyusunan CAPA.
Aplikasi ini memadukan kepatuhan regulasi ketat BPOM CPOB 2018/2024 dan ICH Q9/Q10 dengan paradigma Pharma 4.0 agar investigasi penyimpangan mutu di pabrik tidak lagi bertele-tele di atas kertas, melainkan presisi, objektif, dan dapat diakses langsung oleh operator di lini produksi.""")

# ==============================================================================
# SLIDE 2: LATAR BELAKANG & REALITAS DI LAPANGAN
# ==============================================================================
s2 = prs.slides.add_slide(blank_slide_layout)
apply_background(s2)
add_header(s2, "Kondisi Lapangan Eksisting", "Latar Belakang & Realitas di Lantai Produksi Farmasi", "Karakteristik Industri Farmasi vs Realitas Alur Pelaporan Deviasi Saat Ini")

add_card(s2, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0),
         "Karakteristik Pabrik Farmasi",
         [
             "Regulasi Paling Ketat: Memiliki prinsip Zero Defect Tolerance demi menjamin keselamatan jiwa pasien.",
             "Nilai Finansial Tinggi: Satu bets obat komersial bernilai ratusan juta hingga miliaran rupiah.",
             "Kritis Waktu: Setiap detik keterlambatan keputusan bets berisiko menyebabkan obat kadaluwarsa di karantina atau kelangkaan obat (drug shortage).",
             "Lingkungan Khusus: Ruang produksi bersih (Cleanroom Kelas A-D) memiliki pembatasan ketat terhadap kontaminasi benda asing."
         ],
         badge_text="Karakteristik Industri",
         border_color=COLOR_CYAN_ACCENT)

add_card(s2, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0),
         "Realitas Alur di Lapangan Saat Ini",
         [
             "Dominasi Kertas Manual: Lebih dari 85% pabrik masih mengandalkan lembaran formulir fisik rangkap di clipboard.",
             "Rantai Birokrasi Lambat: Operator mencatat di kertas -> diserahkan fisik ke Supervisor shift -> dibawa manual ke kantor Quality Assurance (QA).",
             "Keterlambatan Pelaporan: Insiden shift malam sering baru dilaporkan keesokan harinya sehingga data mengandalkan ingatan (recall bias).",
             "Silo Antar Divisi: Kordinasi antara Operator Lini, Teknisi Mesin, dan Analis QC terhambat rapat-rapat fisik berkepanjangan."
         ],
         badge_text="Kondisi Eksisting",
         border_color=COLOR_WARNING_BG)

set_speaker_notes(s2, """Dalam industri farmasi, satu bets obat bisa bernilai ratusan juta rupiah dan menyangkut keselamatan nyawa konsumen. Namun realitas di lapangan menunjukkan paradoks: di tengah mesin produksi modern, sistem pelaporan deviasi bets masih terjebak pada lembaran kertas rangkap manual. Ketika anomali terjadi saat shift malam, operator mencatat di clipboard, menunggu pagi untuk menyerahkannya ke supervisor, lalu diserahkan ke QA. Rantai informasi yang lambat ini menyebabkan penanganan insiden mutu tertunda.""")

# ==============================================================================
# SLIDE 3: THE SILENT KILLER (MASALAH SISTEM KERTAS MANUAL)
# ==============================================================================
s3 = prs.slides.add_slide(blank_slide_layout)
apply_background(s3)
add_header(s3, "Pain Points & Dampak Negatif", "The Silent Killer: Dampak Penanganan Deviasi Berbasis Kertas", "Kerugian Finansial, Deviasi Berulang, dan Risiko Kegagalan Audit CPOB")

add_card(s3, Inches(0.8), Inches(1.8), Inches(5.6), Inches(2.4),
         "1. Lead Time Terlalu Panjang (30-45 Hari)",
         [
             "Investigasi manual memakan waktu lebih dari 1 bulan kerja.",
             "Bets tertahan di gudang karantina (holding cost tinggi).",
             "Risiko penundaan suplai obat ke rumah sakit/apotek."
         ],
         badge_text="Lead Time Kritis",
         border_color=COLOR_DANGER_BG)

add_card(s3, Inches(6.8), Inches(1.8), Inches(5.7), Inches(2.4),
         "2. Investigasi Dangkal (Superficial RCA)",
         [
             "> 70% laporan manual berhenti pada kesimpulan klise: 'Human Error'.",
             "Solusi semu selalu pelatihan ulang (retraining operator).",
             "Akar masalah mekanis & metode tidak pernah tersentuh."
         ],
         badge_text="Bias Investigasi",
         border_color=COLOR_WARNING_BG)

add_card(s3, Inches(0.8), Inches(4.5), Inches(5.6), Inches(2.4),
         "3. Deviasi Berulang (Repeat Deviations)",
         [
             "Karena akar masalah sistemik tidak terselesaikan, deviasi terulang kembali.",
             "Peningkatan scrap rate dan pemborosan bahan baku obat.",
             "Penurunan produktivitas fasilitas manufaktur."
         ],
         badge_text="Kegagalan Sistemik",
         border_color=COLOR_DANGER_BG)

add_card(s3, Inches(6.8), Inches(4.5), Inches(5.7), Inches(2.4),
         "4. Risiko Temuan Audit BPOM & ALCOA+",
         [
             "Dokumen fisik rawan tercecer, rusak, atau tulisan tidak terbaca.",
             "Melanggar prinsip Data Integrity ALCOA+ (Legible & Contemporaneous).",
             "Ancaman pembekuan izin edar / sanksi CPOB dari BPOM."
         ],
         badge_text="Kepatuhan Hukum",
         border_color=COLOR_CARD_BORDER)

set_speaker_notes(s3, """Dampak dari sistem manual kertas sangat destruktif bagi pabrik farmasi. Berdasarkan pengamatan industri, lead time investigasi rata-rata mencapai 30 hingga 45 hari. Selama itu, bets bernilai ratusan juta mandek di karantina. Yang lebih berbahaya adalah kecenderungan investigasi dangkal yang menyalahkan personil atau 'human error'. Karena akar masalah mekanik atau metode tidak diperbaiki, deviasi berulang di bets berikutnya. Ini menjadi sasaran temuan audit kritis saat inspeksi BPOM.""")

# ==============================================================================
# SLIDE 4: PARADIGMA PHARMA 4.0
# ==============================================================================
s4 = prs.slides.add_slide(blank_slide_layout)
apply_background(s4)
add_header(s4, "Transformasi Digital Industri", "Paradigma Pharma 4.0: Mengapa Industri Membutuhkan AI?", "Mengadopsi Kerangka Kerja ISPE Pharma 4.0 untuk Keunggulan Operasional")

add_card(s4, Inches(0.8), Inches(1.8), Inches(3.6), Inches(5.0),
         "1. Digital Connectivity",
         [
             "Konektivitas langsung di lini produksi ruang bersih (Cleanroom).",
             "Pelaporan insiden via gawai smartphone / tablet portabel.",
             "Menghilangkan transfer kertas fisik keluar-masuk ruang steril.",
             "Pelaporan seketika saat anomali terdeteksi (Real-Time)."
         ],
         badge_text="Konektivitas")

add_card(s4, Inches(4.8), Inches(1.8), Inches(3.6), Inches(5.0),
         "2. AI-Assisted RCA",
         [
             "Inferensi heuristik cerdas untuk analisis kausalitas mendalam.",
             "Otomasi pembuatan Diagram Tulang Ikan 6M (Ishikawa).",
             "Penelusuran rantai penalaran 5-Whys terstruktur.",
             "Menghilangkan bias subjektif antar personil investigasi."
         ],
         badge_text="Kecerdasan Buatan",
         border_color=COLOR_CYAN_ACCENT)

add_card(s4, Inches(8.8), Inches(1.8), Inches(3.7), Inches(5.0),
         "3. Data Integrity & Trust",
         [
             "Pencatatan digital otomatis yang memenuhi standar ALCOA+.",
             "Perhitungan matriks risiko objektif (ICH Q9 RPN Matrix).",
             "Penerbitan dokumen CAPA tervalidasi siap audit BPOM.",
             "Pemantauan batas waktu (Target Date) dan review efektivitas."
         ],
         badge_text="Kepatuhan Terintegrasi")

set_speaker_notes(s4, """Penerapan Pharma 4.0 bukan sekadar digitalisasi tanpa arah, melainkan menghubungkan lantai produksi dengan kecerdasan komputasi. Melalui Pharma 4.0, operator dapat langsung melaporkan anomali proses lewat gawai steril di ruang bersih. AI Copilot bertindak sebagai partner berpikir yang membedah anomali data, mengeliminasi bias subjektif, dan memastikan kepatuhan regulasi data integritas ALCOA+ terpenuhi secara otomatis.""")

# ==============================================================================
# SLIDE 5: LANDASAN KEPATUHAN REGULASI
# ==============================================================================
s5 = prs.slides.add_slide(blank_slide_layout)
apply_background(s5)
add_header(s5, "Standar Mutu & Regulasi Farmasi", "Landasan Regulasi: Menjamin Kepatuhan Hukum Mutu Obat", "Harmonisasi Standar BPOM CPOB 2018/2024, cGMP FDA, dan ICH Guidelines")

add_card(s5, Inches(0.8), Inches(1.8), Inches(5.6), Inches(2.4),
         "BPOM RI CPOB 2018 & Pembaruan 2024",
         [
             "Bab 1 (Sistem Mutu Industri Farmasi): Penanganan deviasi sistematis & investigasi komprehensif.",
             "Aneks 1 (Produk Steril): Pengendalian partikulat & mikrobiologi.",
             "Mandat: Setiap bets OOS wajib diinvestigasi sebelum rilis."
         ],
         badge_text="Regulasi Nasional BPOM",
         border_color=COLOR_CYAN_ACCENT)

add_card(s5, Inches(6.8), Inches(1.8), Inches(5.7), Inches(2.4),
         "ICH Q9: Quality Risk Management (QRM)",
         [
             "Penetapan kuantitatif Risk Priority Number (RPN).",
             "Formula: RPN = Severity (S) x Probability (P) x Detectability (D).",
             "Klasifikasi dampak objektif: Critical, Major, atau Minor."
         ],
         badge_text="Standar Risiko ICH Q9",
         border_color=COLOR_CYAN_ACCENT)

add_card(s5, Inches(0.8), Inches(4.5), Inches(5.6), Inches(2.4),
         "ICH Q10: Pharmaceutical Quality System (PQS)",
         [
             "Siklus perbaikan mutu berkesinambungan (Continuous Improvement).",
             "Penyusunan Corrective Action (CA) & Preventive Action (PA).",
             "Kewajiban Tinjauan Efektivitas (Effectiveness Check 30-60 hari)."
         ],
         badge_text="Sistem Mutu ICH Q10")

add_card(s5, Inches(6.8), Inches(4.5), Inches(5.7), Inches(2.4),
         "FDA 21 CFR Part 211 & ALCOA+ Principles",
         [
             "21 CFR 211.192: Penyelidikan menyeluruh terhadap kegagalan bets.",
             "Data Integrity ALCOA+: Attributable, Legible, Contemporaneous, Original, and Accurate.",
             "Jejak rekam digital yang terverifikasi dan siap diaudit."
         ],
         badge_text="Standar Global FDA")

set_speaker_notes(s5, """Kepatuhan regulasi adalah pondasi mutlak dalam farmasi. PharmaCAPA AI dibangun dengan mengacu langsung pada pedoman resmi: CPOB BPOM 2018/2024 Bab 1 dan Aneks 1 steril, ICH Q9 untuk evaluasi risiko berbasis RPN, ICH Q10 untuk penanganan siklus CAPA dan review efektivitas, serta FDA 21 CFR Part 211. Sistem ini bukan sekadar alat bantu ketik, melainkan sistem pemastian kepatuhan regulasi otomatis.""")

# ==============================================================================
# SLIDE 6: SOLUSI PHARMACAPA AI COCKPIT
# ==============================================================================
s6 = prs.slides.add_slide(blank_slide_layout)
apply_background(s6)
add_header(s6, "Inovasi Solusi", "Solusi: PharmaCAPA AI Cockpit", "Arsitektur Sistem Dual-Engine AI & Antarmuka Operator-QA Terpadu")

add_card(s6, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0),
         "Arsitektur Dual-Engine AI",
         [
             "1. Offline Pharmaceutical Heuristic Engine (Default):",
             "   - Berjalan 100% lokal di browser tanpa koneksi internet.",
             "   - Solusi ideal untuk cleanroom berpelindung sinyal radio (Faraday shield).",
             "   - Menghitung RPN, memetakan 6M Ishikawa & 5-Whys seketika.",
             "",
             "2. Cloud LLM Reasoning (Google Gemini API):",
             "   - Analisis narasi mendalam untuk kasus deviasi kustom kompleks.",
             "   - Rekomendasi tindakan CAPA adaptif berbasis data farmasi global."
         ],
         badge_text="Teknologi Dual-Engine",
         border_color=COLOR_CYAN_ACCENT)

add_card(s6, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0),
         "Fitur Unggulan Sistem",
         [
             "4 Preset Kasus Riil Farmasi: Disolusi OOS Paracetamol, Lonjakan Suhu FBD Amoxicillin, Partikulat Steril Ceftriaxone, dan Capping Cetirizine.",
             "Kalkulator RPN & Disposisi Otomatis: Hold/Quarantine, Evaluasi Rework, atau Reject formal CPOB.",
             "Visualisasi SVG Interaktif 6M: Diagram tulang ikan dengan indikator akar masalah berdenyut (pulsing red).",
             "Generator Dokumen Resmi CPOB: Unduh format Microsoft Word (.doc) dan cetak langsung ke PDF A4 siap audit."
         ],
         badge_text="Kapabilitas Sistem",
         border_color=COLOR_SUCCESS_BG)

set_speaker_notes(s6, """Arsitektur PharmaCAPA AI memiliki keunggulan unik melalui Dual-Engine AI. Seringkali di dalam ruang produksi steril, koneksi internet dibatasi. Oleh karena itu, kami menyematkan Offline Heuristic Engine yang tetap dapat menganalisis data, menghitung RPN, dan membuat diagram 6M tanpa internet sama sekali. Jika terhubung ke internet, sistem dapat mengaktifkan Cloud Gemini LLM untuk penalaran mendalam. Sistem ini juga dilengkapi 4 studi kasus deviasi industri riil.""")

# ==============================================================================
# SLIDE 7: METODOLOGI RCA (ISHIKAWA 6M & 5-WHYS)
# ==============================================================================
s7 = prs.slides.add_slide(blank_slide_layout)
apply_background(s7)
add_header(s7, "Metodologi Analisis Akar Masalah", "Metodologi RCA: Integrasi Ishikawa 6M & 5-Whys", "Membongkar Akar Masalah Sistemik dan Menghentikan Budaya Menyalahkan Operator")

add_card(s7, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0),
         "Diagram Tulang Ikan (Ishikawa 6M)",
         [
             "1. Man (Personil): Verifikasi sertifikasi, kelelahan shift, four-eyes principle.",
             "2. Machine (Mesin): Kalibrasi sensor hidrolik, keausan mekanik, drift load cell.",
             "3. Material (Bahan): Kualitas eksipien, kadar air (LOD), proporsi fines granul.",
             "4. Method (Metode): Validasi SOP, kelengkapan checklist setup mesin, line clearance.",
             "5. Measurement (Alat Ukur): Kalibrasi spektrofotometer, akurasi timbangan analitik.",
             "6. Milieu (Lingkungan): Kontrol suhu, kelembaban (RH), perbedaan tekanan udara (DP)."
         ],
         badge_text="Domain Ishikawa 6M",
         border_color=COLOR_CYAN_ACCENT)

add_card(s7, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0),
         "Pohon Penalaran Kausalitas 5-Whys",
         [
             "Mengapa 1 (Gejala Awal): Uji disolusi tahap S1/S2 gagal (Q=73.5%).",
             "Mengapa 2 (Mekanik): Kekerasan kaplet terlalu tinggi (> 14 kP), porositas rendah.",
             "Mengapa 3 (Setting Proses): Tekanan kompresi aktual mencapai 24.8 kN (Target 18-20 kN).",
             "Mengapa 4 (Alat/Instrumen): Load cell rotary tablet press mengalami drift kalibrasi +5.2 kN.",
             "Mengapa 5 (AKAR MASALAH SISTEMIK):",
             "🎯 Alarm over-force pada HMI dinonaktifkan sementara dan belum ada checklist verifikasi verifikasi sensor pra-produksi."
         ],
         badge_text="Rantai Kausalitas 5-Whys",
         border_color=COLOR_WARNING_BG)

set_speaker_notes(s7, """Fitur utama PharmaCAPA AI adalah investigasi akar masalah berbasis metode ilmiah 6M dan 5-Whys. Sistem secara otomatis memetakan dugaan penyebab ke dalam 6 cabang Ishikawa: Man, Machine, Material, Method, Measurement, dan Milieu. Kemudian sistem menelusuri 5 tingkat 'Mengapa'. Sebagai contoh pada kasus disolusi OOS: akar masalah sebenarnya bukan operator yang lalai, melainkan sensor tekanan mesin yang mengalami drift dan alarm HMI yang dinonaktifkan tanpa verifikasi pra-produksi.""")

# ==============================================================================
# SLIDE 8: KUANTIFIKASI RISIKO ICH Q9 (RPN)
# ==============================================================================
s8 = prs.slides.add_slide(blank_slide_layout)
apply_background(s8)
add_header(s8, "Manajemen Risiko Mutu Kuantitatif", "Kuantifikasi Risiko: Algoritma RPN & Disposisi Bets", "Penilaian Objektif Berbasis ICH Q9 Quality Risk Management Tanpa Bias Personal")

add_card(s8, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0),
         "Algoritma Formula RPN (ICH Q9)",
         [
             "Formula: RPN = Severity (S) x Probability (P) x Detectability (D)",
             "",
             "• Severity (S: 1 - 5):",
             "  Mengukur keparahan dampak terhadap keamanan pasien dan bioavailabilitas obat.",
             "",
             "• Probability (P: 1 - 5):",
             "  Mengukur frekuensi atau kemungkinan terjadinya kegagalan proses di lini manufaktur.",
             "",
             "• Detectability (D: 1 - 5):",
             "  Mengukur kemudahan mendeteksi anomali sebelum obat lolos ke tahap distribusi komersial."
         ],
         badge_text="Formula ICH Q9",
         border_color=COLOR_CYAN_ACCENT)

add_card(s8, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0),
         "Klasifikasi Dampak & Disposisi Bets",
         [
             "🔴 CRITICAL (RPN >= 40):",
             "   - Dampak langsung terhadap sterilitas atau potensi toksisitas.",
             "   - Disposisi: Karantina Formal & Evaluasi Reject / Destruksi Produk.",
             "",
             "🟡 MAJOR (RPN 10 - 39):",
             "   - Kegagalan CQA seperti Disolusi OOS atau variasi kadar.",
             "   - Disposisi: Penahanan Karantina CPOB & Uji Diperluas (Expanded Testing).",
             "",
             "🟢 MINOR (RPN < 10):",
             "   - Deviasi kosmetik atau isolasi kecil yang tidak mempengaruhi CQA.",
             "   - Disposisi: Rilis Bersyarat dengan Notifikasi QA."
         ],
         badge_text="Kategori & Disposisi",
         border_color=COLOR_WARNING_BG)

set_speaker_notes(s8, """Untuk menghilangkan perdebatan dan subjektivitas antar personil, sistem menerapkan algoritma RPN kuantitatif berstandar ICH Q9. Parameter Severity, Probability, dan Detectability dikalikan secara otomatis. Nilai RPN ini langsung memicu klasifikasi deviasi menjadi Minor, Major, atau Critical, serta memberikan rekomendasi Disposisi Bets resmi CPOB seketika: apakah bets harus dikarantina untuk pengujian diperluas, atau harus ditolak.""")

# ==============================================================================
# SLIDE 9: AKSES MOBILE OPERATOR
# ==============================================================================
s9 = prs.slides.add_slide(blank_slide_layout)
apply_background(s9)
add_header(s9, "Aksesibilitas & Human-Centered Design", "Desain Lapangan: Akses Mobile untuk Operator Ruang Bersih", "Responsif di Layar Smartphone (Safari iOS & Android) Tanpa Hambatan Ruang Bersih")

add_card(s9, Inches(0.8), Inches(1.8), Inches(3.6), Inches(5.0),
         "Kebutuhan Operator Lini",
         [
             "Bekerja di dalam ruang bersih dengan pakaian khusus (gowning).",
             "Tidak memungkinkan membawa laptop atau PC desktop ke cleanroom.",
             "Membutuhkan perangkat portabel yang dapat disanitasi alkohol 70%.",
             "Waktu input harus sangat singkat agar tidak mengganggu proses produksi."
         ],
         badge_text="Tantangan Cleanroom")

add_card(s9, Inches(4.8), Inches(1.8), Inches(3.6), Inches(5.0),
         "Optimalisasi Antarmuka",
         [
             "Mobile-First Responsive: Menyesuaikan sempurna dengan rasio layar smartphone.",
             "Preset Chips Cepat: Pilihan 1-klik untuk insiden disolusi, suhu, partikulat, atau bobot.",
             "Clinical High-Contrast: Teks putih tebal di atas latar navy, sangat jelas terbaca di bawah lampu terang pabrik.",
             "Navigasi Tab Minimalis: 5 tab sekuensial yang intuitif bagi operator."
         ],
         badge_text="Fitur UI/UX",
         border_color=COLOR_CYAN_ACCENT)

add_card(s9, Inches(8.8), Inches(1.8), Inches(3.7), Inches(5.0),
         "Kompatibilitas Global",
         [
             "100% Berjalan di Safari iPhone, Google Chrome, Edge, & Firefox.",
             "Zero Installation: Tanpa perlu download dari App Store / Play Store.",
             "Bebas Kuota API: Heuristic engine berjalan tanpa bergantung server luar.",
             "Tautan resmi bersih: https://rismawatilaila.github.io/pharmacapa/"
         ],
         badge_text="Aksesibilitas Multi-Device",
         border_color=COLOR_SUCCESS_BG)

set_speaker_notes(s9, """Kami sangat memprioritaskan kemudahan pemakaian oleh operator lini produksi. Operator memakai sarung tangan karet dan pakaian steril, sehingga tidak mungkin menggunakan laptop di ruang bersih. Oleh karena itu, antarmuka PharmaCAPA AI dirancang mobile-first, sangat kontras, dan dapat dibuka langsung melalui Safari di iPhone maupun Chrome di Android tanpa perlu instalasi aplikasi tambahan. Cukup ketuk preset kasus, dan analisis langsung tersaji.""")

# ==============================================================================
# SLIDE 10: FITUR EKSPOR DOKUMEN RESMI CPOB
# ==============================================================================
s10 = prs.slides.add_slide(blank_slide_layout)
apply_background(s10)
add_header(s10, "Dokumentasi Resmi Kepatuhan", "Fitur Ekspor Dokumen Resmi CPOB (Word & PDF)", "Scroll-Down Selector Format: Menghasilkan Dokumen Terstandarisasi Siap Audit")

add_card(s10, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0),
         "1. Ekspor Microsoft Word (.doc)",
         [
             "Struktur Berkas Tabel XML Office Standar:",
             "• Kop Formulir Resmi Pabrik Farmasi (No. Dokumen: SOP-QA-042).",
             "• Bagian 1: Data Identitas Bets & Telemetri Kejadian.",
             "• Bagian 2: Kajian Risiko Mutu ICH Q9 (Tabel RPN & Klasifikasi).",
             "• Bagian 3: Matriks Analisis Akar Masalah 6M Ishikawa.",
             "• Bagian 4: Rantai Penalaran Kausalitas 5-Whys.",
             "• Bagian 5: Tabel Rencana CAPA (Corrective & Preventive Action) dengan PIC, Batas Waktu, dan Kriteria Review.",
             "• Bagian 6: Kolom Tanda Tangan Resmi (Pelapor, QA, dan QA Manager)."
         ],
         badge_text="Format Microsoft Word",
         border_color=COLOR_CYAN_ACCENT)

add_card(s10, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0),
         "2. Format PDF (Cetak Siap Audit)",
         [
             "Format Cetak Presisi Standar Kertas A4:",
             "• Menggunakan CSS @media print profesional.",
             "• Multi-page pagination otomatis tanpa ada teks yang terpotong.",
             "• Modal dan tombol interaktif disembunyikan otomatis saat mencetak.",
             "• Dapat langsung disimpan menjadi berkas PDF resmi.",
             "",
             "Keunggulan bagi Tim QA:",
             "• Menghilangkan pekerjaan administrasi pengetikan ulang berjam-jam.",
             "• Format 100% konsisten antar departemen pabrik.",
             "• Langsung siap diserahkan saat inspeksi mendadak oleh auditor BPOM."
         ],
         badge_text="Format Cetak PDF A4",
         border_color=COLOR_SUCCESS_BG)

set_speaker_notes(s10, """Di industri farmasi berlaku prinsip: 'If it is not documented, it did not happen'. PharmaCAPA AI menyediakan fitur ekspor dokumen resmi berstandar CPOB melalui scroll-down selector dropdown. Pengguna dapat memilih format Microsoft Word untuk diedit dan disesuaikan, atau format PDF A4 yang siap dicetak dengan pembagian halaman rapi. Dokumen ini lengkap dengan kop surat, tabel 6M, tabel tindakan CAPA, dan kolom tanda tangan pejabat berwenang.""")

# ==============================================================================
# SLIDE 11: STUDI KASUS & DAMPAK OPERASIONAL
# ==============================================================================
s11 = prs.slides.add_slide(blank_slide_layout)
apply_background(s11)
add_header(s11, "Evaluasi Kinerja & Dampak Bisnis", "Studi Kasus & Dampak Operasional: Before vs After", "Kuantifikasi Manfaat Nyata Implementasi PharmaCAPA AI di Pabrik Farmasi")

# Tabel Komparasi
rows, cols = 7, 4
left, top, width, height = Inches(0.8), Inches(1.8), Inches(11.7), Inches(5.0)
table_shape = s11.shapes.add_table(rows, cols, left, top, width, height)
table = table_shape.table

# Set Column Widths
table.columns[0].width = Inches(3.2)
table.columns[1].width = Inches(3.0)
table.columns[2].width = Inches(3.0)
table.columns[3].width = Inches(2.5)

headers = ["Parameter Kinerja", "Sebelum (Manual Kertas)", "Sesudah (PharmaCAPA AI)", "Nilai Efisiensi"]
for i, h in enumerate(headers):
    cell = table.cell(0, i)
    cell.fill.solid()
    cell.fill.fore_color.rgb = COLOR_CARD_BORDER
    p = cell.text_frame.paragraphs[0]
    p.text = h
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = COLOR_WHITE
    p.alignment = PP_ALIGN.CENTER

data = [
    ("Waktu Pelaporan Deviasi Awal", "4 - 8 Jam (tunggu ganti shift)", "< 3 Menit via Smartphone", "95% Lebih Cepat"),
    ("Penyusunan Diagram 6M & 5-Whys", "3 - 5 Hari (rapat fisik)", "Otomatis Instan (< 5 detik)", "Eliminasi Rapat Manual"),
    ("Lead Time Penutupan CAPA", "30 - 45 Hari Kerja", "< 3 Hari Kerja", "Efisiensi Waktu 90%"),
    ("Akurasi Akar Masalah (RCA)", "Rendah (bias human error)", "Tinggi (analisis objektif)", "Cegah Deviasi Berulang"),
    ("Biaya Bets Tertahan (Holding Cost)", "Sangat Tinggi (gudang penuh)", "Sangat Rendah (disposisi cepat)", "Efisiensi Finansial"),
    ("Kesiapan Audit BPOM (ALCOA+)", "Rentan dokumen hilang/rusak", "100% Digital & Terstruktur", "100% Audit Ready")
]

for row_idx, row_data in enumerate(data, start=1):
    for col_idx, text in enumerate(row_data):
        cell = table.cell(row_idx, col_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = COLOR_CARD_BG if row_idx % 2 == 1 else RGBColor(15, 34, 58)
        p = cell.text_frame.paragraphs[0]
        p.text = text
        p.font.size = Pt(11)
        p.font.color.rgb = COLOR_CYAN_ACCENT if col_idx == 3 else COLOR_WHITE

set_speaker_notes(s11, """Tabel ini menunjukkan hasil komparasi kuantitatif sebelum dan sesudah implementasi PharmaCAPA AI. Pelaporan awal terpangkas dari 8 jam menjadi di bawah 3 menit. Pembuatan diagram 6M yang biasanya butuh berhari-hari kini terjadi seketika. Dan yang paling impresif, total lead time investigasi yang sebelumnya memakan waktu hingga 45 hari berhasil dipangkas menjadi kurang dari 3 hari kerja. Ini menghemat ratusan juta rupiah biaya holding bets di gudang karantina pabrik.""")

# ==============================================================================
# SLIDE 12: KESIMPULAN & ROADMAP MASA DEPAN
# ==============================================================================
s12 = prs.slides.add_slide(blank_slide_layout)
apply_background(s12)
add_header(s12, "Penutup & Langkah Selanjutnya", "Kesimpulan & Roadmap Pengembangan Masa Depan", "Transformasi Nyata Menuju Smart Pharmaceutical Manufacturing")

add_card(s12, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0),
         "Kesimpulan Utama",
         [
             "1. Kepatuhan Regulasi & AI Berpadu:",
             "   PharmaCAPA AI membuktikan bahwa kecerdasan buatan dapat diintegrasikan secara patuh dengan standar ketat BPOM CPOB dan ICH Q9/Q10.",
             "",
             "2. Efisiensi Nyata Lantai Produksi:",
             "   Transformasi dari dokumen kertas ke Pharma 4.0 memangkas lead time investigasi deviasi hingga 90% dan mencegah deviasi berulang.",
             "",
             "3. Memberdayakan Operator Lini:",
             "   Antarmuka mobile-first memungkinkan pelaporan langsung di ruang bersih tanpa melanggar batasan sterilitas."
         ],
         badge_text="Pencapaian Proyek",
         border_color=COLOR_SUCCESS_BG)

add_card(s12, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0),
         "Roadmap Pengembangan (Phase 2)",
         [
             "• Integrasi Langsung Sensor IoT / SCADA:",
             "  Pemicu deviasi otomatis ketika suhu FBD, tekanan kompresi, atau sensor partikel ruang bersih mendeteksi anomali OOS.",
             "",
             "• Audit Trail Terenkripsi Blockchain:",
             "  Penjaminan integritas data tanpa celah modifikasi (Tamper-Proof) untuk audit internasional FDA & EMA.",
             "",
             "• PWA dengan Barcode / QR Scanner:",
             "  Pindai barcode drum bahan baku untuk memuat riwayat Electronic Batch Record (EBR) seketika.",
             "",
             "🌐 Tautan Resmi: https://rismawatilaila.github.io/pharmacapa/"
         ],
         badge_text="Langkah Selanjutnya",
         border_color=COLOR_CYAN_ACCENT)

set_speaker_notes(s12, """Sebagai kesimpulan, PharmaCAPA AI bukan hanya proyek konseptual, melainkan cetak biru implementasi nyata Pharma 4.0 di Indonesia yang siap pakai dan teruji. Ke depan, kami berencana menghubungkan sistem ini langsung ke sensor IoT mesin industri farmasi dan rekam bets elektronik. Terima kasih banyak atas bimbingan Prof. Arry. Kami membuka sesi tanya jawab dan diskusi.""")

# Simpan Presentasi
output_filename = "PharmaCAPA_AI_Presentasi.pptx"
prs.save(output_filename)
print(f"Presentation saved successfully as: {output_filename}")
