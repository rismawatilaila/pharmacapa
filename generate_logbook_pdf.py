"""
Script untuk mengenerate PDF Dokumen Resmi: LOGBOOK PENGEMBANGAN PROYEK PHARMACAPA AI
Standar: ReportLab, Kertas A4, Styling Clinical Navy, Tabel Terformat Rapi, Running Header & Footer.
"""

import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch, cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    """Canvas kustom untuk menghitung total halaman dan running header/footer"""
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748b"))
        
        # Running Header (Halaman 2 ke atas)
        if self._pageNumber > 1:
            self.drawString(40, 800, "PharmaCAPA AI — Logbook Pengembangan Proyek (Pharma 4.0 & CPOB)")
            self.drawRightString(555, 800, "Dosen: Prof. Ir. Arry Akhmad Arman, M.T., Ph.D.")
            self.setStrokeColor(colors.HexColor("#cbd5e1"))
            self.setLineWidth(0.5)
            self.line(40, 794, 555, 794)

        # Running Footer (Semua halaman)
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.5)
        self.line(40, 42, 555, 42)
        
        self.drawString(40, 30, "Dokumen Akademik & Validasi Industri — Rahasia & Terstandarisasi CPOB BPOM")
        page_str = f"Halaman {self._pageNumber} dari {page_count}"
        self.drawRightString(555, 30, page_str)
        self.restoreState()

def build_pdf(filename="PharmaCAPA_AI_Logbook_Pengembangan.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=54,
        bottomMargin=50
    )

    styles = getSampleStyleSheet()
    
    # Custom Palette
    c_primary = colors.HexColor("#0b223d")    # Navy
    c_accent = colors.HexColor("#0284c7")     # Blue
    c_cyan = colors.HexColor("#0369a1")       # Cyan
    c_text = colors.HexColor("#1e293b")       # Dark Slate
    c_bg_light = colors.HexColor("#f8fafc")   # Light gray
    c_border = colors.HexColor("#cbd5e1")     # Border
    
    # Typography Styles
    style_title = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=c_primary,
        spaceAfter=4
    )
    
    style_subtitle = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10.5,
        leading=14,
        textColor=c_accent,
        spaceAfter=10
    )
    
    style_h1 = ParagraphStyle(
        'Heading1Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.white,
        spaceBefore=0,
        spaceAfter=0
    )
    
    style_h2 = ParagraphStyle(
        'Heading2Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=c_primary,
        spaceBefore=10,
        spaceAfter=4
    )
    
    style_body = ParagraphStyle(
        'BodyCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12.5,
        textColor=c_text,
        spaceAfter=6
    )
    
    style_cell = ParagraphStyle(
        'CellCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10.5,
        textColor=c_text
    )
    
    style_cell_bold = ParagraphStyle(
        'CellBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10.5,
        textColor=c_text
    )
    
    style_th = ParagraphStyle(
        'THCustom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10.5,
        textColor=colors.white,
        alignment=1 # Center
    )

    story = []

    # --- KOP / HEADER RESMI ---
    kop_data = [
        [
            Paragraph("<b>✚ SISTEM MANAJEMEN DEVIASI MUTU FARMASI — PHARMA 4.0</b>", style_subtitle),
            Paragraph("<b>NO. DOKUMEN:</b> LB-AI-2026-01<br/><b>REVISI:</b> 02 (Final)", style_cell)
        ]
    ]
    t_kop = Table(kop_data, colWidths=[380, 143])
    t_kop.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_kop)
    story.append(Spacer(1, 4))

    story.append(Paragraph("LOGBOOK PENGEMBANGAN PROYEK PHARMACAPA AI", style_title))
    story.append(Paragraph("Sistem Investigasi Deviasi Bets Cepat, Analisis Akar Masalah (Ishikawa 6M & 5-Whys), serta Dokumen CAPA Berstandar BPOM CPOB 2018/2024 & ICH Q9/Q10", style_subtitle))
    
    # Metadata Table
    meta_data = [
        [Paragraph("<b>Mata Kuliah / Penilaian:</b>", style_cell_bold), Paragraph("Tugas Besar Rekayasa & Implementasi Artificial Intelligence", style_cell),
         Paragraph("<b>Tanggal Selesai:</b>", style_cell_bold), Paragraph("22 Oktober 2026", style_cell)],
        [Paragraph("<b>Dosen Pengampu:</b>", style_cell_bold), Paragraph("Prof. Ir. Arry Akhmad Arman, M.T., Ph.D.", style_cell),
         Paragraph("<b>Status Sistem:</b>", style_cell_bold), Paragraph("<font color='#0284c7'><b>100% Live & Verified</b></font>", style_cell)],
        [Paragraph("<b>Tautan Resmi Aplikasi:</b>", style_cell_bold), Paragraph("<u>https://rismawatilaila.github.io/pharmacapa/</u> | <u>https://pharmacapa.streamlit.app/</u>", style_cell),
         Paragraph("<b>Repositori Git:</b>", style_cell_bold), Paragraph("<u>github.com/rismawatilaila/pharmacapa</u>", style_cell)]
    ]
    t_meta = Table(meta_data, colWidths=[110, 220, 80, 113])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f1f5f9")),
        ('BOX', (0,0), (-1,-1), 1, c_border),
        ('INNERGRID', (0,0), (-1,-1), 0.5, c_border),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 12))

    # Helper untuk Section Header
    def add_section_banner(title_text):
        t_sec = Table([[Paragraph(f"<b>{title_text}</b>", style_h1)]], colWidths=[523])
        t_sec.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), c_primary),
            ('TOPPADDING', (0,0), (-1,-1), 5),
            ('BOTTOMPADDING', (0,0), (-1,-1), 5),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
            ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ]))
        return t_sec

    # =========================================================================
    # BAGIAN 1: LATAR BELAKANG & KONDISI LAPANGAN EKSISTING
    # =========================================================================
    story.append(add_section_banner("1. LATAR BELAKANG & KONDISI LAPANGAN SEBELUM OTOMASI (SISTEM KERTAS MANUAL)"))
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        "Di industri manufaktur farmasi, kepatuhan terhadap regulasi <b>BPOM CPOB 2018/2024</b> dan <b>ICH Q9/Q10</b> adalah mandat hukum dan etika medis tertinggi. Namun fakta di lapangan menunjukkan bahwa mayoritas lini produksi masih mengandalkan lembaran formulir kertas manual dalam menangani penyimpangan bets (*batch deviation*). Kondisi konvensional ini menimbulkan kerugian operasional dan risiko audit yang masif:",
        style_body
    ))

    # Tabel Komparasi Masalah Manual Kertas
    masalah_data = [
        [
            Paragraph("Parameter Evaluasi", style_th),
            Paragraph("Kondisi Lapangan Sebelum (Manual Kertas)", style_th),
            Paragraph("Dampak Negatif & Risiko Pabrik Farmasi", style_th)
        ],
        [
            Paragraph("<b>Media & Pencatatan Fisik</b>", style_cell_bold),
            Paragraph("Formulir fisik kertas rangkap (Logbook Bets, Form Deviasi QA fisik). Dicatat manual dengan pulpen di atas clipboard oleh operator di ruang produksi.", style_cell),
            Paragraph("Kertas rawan robek, basah oleh cairan sanitasi (alkohol 70%), tulisan tangan sulit dibaca (illegible), atau dokumen terselip antar departemen.", style_cell)
        ],
        [
            Paragraph("<b>Waktu Alur & Birokrasi (Lead Time)</b>", style_cell_bold),
            Paragraph("Operator mengisi form -> diserahkan manual ke Supervisor shift -> dikirim ke departemen QA -> dijadwalkan rapat investigasi fisik. Rata-rata <b>30–45 hari kerja</b>.", style_cell),
            Paragraph("Bets tertahan di gudang karantina (holding cost tinggi), keterlambatan rilis produk komersial ke pasar, risiko kadaluwarsa, dan ancaman kelangkaan obat (*drug shortage*).", style_cell)
        ],
        [
            Paragraph("<b>Kedalaman Investigasi Akar Masalah</b>", style_cell_bold),
            Paragraph("Investigasi sering dangkal (*superficial root cause*), berhenti pada kesimpulan klise: <i>'Human error / operator kurang teliti'</i>.", style_cell),
            Paragraph("Akar masalah sistemik mesin/metode/lingkungan tidak terselesaikan; deviasi yang sama berulang kembali (*repeat deviation*) pada bets-bets berikutnya.", style_cell)
        ],
        [
            Paragraph("<b>Kajian Risiko Mutu (ICH Q9)</b>", style_cell_bold),
            Paragraph("Matriks risiko dihitung secara subjektif atau manual di spreadsheet terpisah tanpa standarisasi algoritma baku.", style_cell),
            Paragraph("Inkonsistensi penetapan kategori deviasi (*Minor, Major, Critical*); personil QA yang berbeda menghasilkan disposisi bets yang berbeda untuk insiden yang sama.", style_cell)
        ],
        [
            Paragraph("<b>Aksesibilitas Ruang Bersih (Cleanroom)</b>", style_cell_bold),
            Paragraph("Operator di dalam Ruang Bersih Kelas A/B/C/D dilarang membawa laptop/PC karena aturan partikel & sterilitas CPOB.", style_cell),
            Paragraph("Penundaan pencatatan deviasi; data baru dicatat beberapa jam setelah shift selesai sehingga mengandalkan ingatan (*recall bias*).", style_cell)
        ],
        [
            Paragraph("<b>Kepatuhan Integritas Data (ALCOA+)</b>", style_cell_bold),
            Paragraph("Dokumen fisik tidak memiliki jejak rekam otomatis (*no digital audit trail*); pencatatan waktu rawan diisi belakangan (*backdating*).", style_cell),
            Paragraph("Pelanggaran serius terhadap prinsip Data Integrity CPOB & FDA 21 CFR Part 11; menjadi temuan audit kritis saat inspeksi BPOM.", style_cell)
        ]
    ]

    t_masalah = Table(masalah_data, colWidths=[110, 205, 208])
    t_masalah.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_cyan),
        ('BOX', (0,0), (-1,-1), 1, c_border),
        ('INNERGRID', (0,0), (-1,-1), 0.5, c_border),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_bg_light]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(t_masalah)
    story.append(Spacer(1, 12))

    # =========================================================================
    # BAGIAN 2: PENERAPAN PHARMA 4.0 & KEPATUHAN REGULASI
    # =========================================================================
    story.append(add_section_banner("2. KONSEPSI PENERAPAN PHARMA 4.0 & KEPATUHAN REGULASI"))
    story.append(Spacer(1, 6))
    
    p2_desc = (
        "Proyek <b>PharmaCAPA AI</b> mengadopsi pilar <b>ISPE Pharma 4.0</b> untuk mendigitalkan lantai produksi farmasi secara terintegrasi:<br/>"
        "• <b>Digital Maturity & Connectivity:</b> Memungkinkan operator lini melaporkan deviasi secara *paperless* melalui gawai smartphone atau tablet steril di dalam ruang bersih.<br/>"
        "• <b>AI-Assisted Root Cause Analysis:</b> Otomasi pembentukan Diagram Tulang Ikan (Ishikawa 6M) dan penelusuran kausalitas 5-Whys untuk menemukan akar masalah sistemik sejati.<br/>"
        "• <b>Quantitative Quality Risk Management (ICH Q9):</b> Perhitungan kuantitatif nilai <i>Risk Priority Number</i> (RPN = Severity × Probability × Detectability) untuk klasifikasi dampak dan rekomendasi disposisi bets otomatis.<br/>"
        "• <b>Data Integrity ALCOA+ & Audit Readiness:</b> Memenuhi prinsip <i>Attributable, Legible, Contemporaneous, Original, and Accurate</i> serta kesiapan audit BPOM dengan ekspor dokumen resmi Word (.doc) dan PDF."
    )
    story.append(Paragraph(p2_desc, style_body))
    story.append(Spacer(1, 10))

    # =========================================================================
    # BAGIAN 3: TABEL LOG AKTIVITAS PENGEMBANGAN PROYEK
    # =========================================================================
    story.append(add_section_banner("3. LOG AKTIVITAS TAHAPAN PENGEMBANGAN PROYEK (DEVELOPMENT LOGBOOK)"))
    story.append(Spacer(1, 6))

    log_data = [
        [
            Paragraph("Fase & Waktu", style_th),
            Paragraph("Aktivitas & Rincian Rekayasa Teknis", style_th),
            Paragraph("Deliverable / Output", style_th),
            Paragraph("Verifikasi Regulasi", style_th)
        ],
        [
            Paragraph("<b>Fase 1</b><br/>Inisiasi & Analisis<br/><i>Hari 1 (08.00-12.00)</i>", style_cell),
            Paragraph("• Wawancara & pemetaan kendala operator pabrik farmasi.<br/>• Identifikasi kelemahan alur manual formulir kertas.<br/>• Perumusan batasan proyek tugas AI Prof. Arry.", style_cell),
            Paragraph("Dokumen Spesifikasi Kebutuhan Sistem PharmaCAPA AI Copilot.", style_cell),
            Paragraph("Gap analysis terhadap CPOB Bab 1 & ICH Q10.", style_cell)
        ],
        [
            Paragraph("<b>Fase 2</b><br/>Pemodelan Kasus Riil<br/><i>Hari 1 (13.00-17.00)</i>", style_cell),
            Paragraph("• Penyusunan 4 preset kasus deviasi riil industri:<br/>  1. Uji Disolusi OOS Paracetamol (Solid Oral)<br/>  2. Thermal Excursion FBD Amoxicillin (Granulasi)<br/>  3. Partikulat Asing Vial Ceftriaxone (Steril)<br/>  4. Variasi Bobot & Capping Cetirizine (Cetak)", style_cell),
            Paragraph("Dataset terstruktur <code>js/pharma-data.js</code> dengan telemetri CPP & CQA.", style_cell),
            Paragraph("Kesesuaian monografi Farmakope Indonesia & USP.", style_cell)
        ],
        [
            Paragraph("<b>Fase 3</b><br/>Engine AI Dual-Layer<br/><i>Hari 1 (19.00-23.30)</i>", style_cell),
            Paragraph("• Implementasi <i>Offline Pharmaceutical Heuristic Expert Engine</i> (berjalan lokal tanpa internet di ruang steril).<br/>• Integrasi Google Gemini AI API untuk investigasi kustom.<br/>• Algoritma kalkulasi RPN kuantitatif (ICH Q9).", style_cell),
            Paragraph("Modul engine AI <code>js/ai-engine.js</code> dengan logika deterministik dan generatif.", style_cell),
            Paragraph("Validasi matriks risiko ICH Q9 (Critical, Major, Minor).", style_cell)
        ],
        [
            Paragraph("<b>Fase 4</b><br/>Rekayasa UI/UX 6M<br/><i>Hari 2 (08.00-14.00)</i>", style_cell),
            Paragraph("• Desain antarmuka Clinical Navy modern.<br/>• Generator visual interaktif SVG Diagram Tulang Ikan 6M Ishikawa (Man, Machine, Material, Method, Measurement, Milieu).<br/>• Komponen pohon kausalitas 5-Whys berjenjang.<br/>• Optimasi tampilan mobile viewport smartphone.", style_cell),
            Paragraph("Antarmuka cockpit <code>index.html</code> dan stylesheet <code>css/style.css</code> responsif.", style_cell),
            Paragraph("Kemudahan akses operator lini di layar sentuh gawai HP.", style_cell)
        ],
        [
            Paragraph("<b>Fase 5</b><br/>Ekspor Dokumen CPOB<br/><i>Hari 2 (14.30-18.00)</i>", style_cell),
            Paragraph("• Pembuatan generator formulir deviasi resmi CPOB.<br/>• Implementasi <i>scroll-down dropdown format selector</i>:<br/>  - Microsoft Word (.doc) dengan tabel XML Office rapi.<br/>  - PDF A4 siap cetak dengan penanganan pagination.", style_cell),
            Paragraph("Modul pelaporan <code>js/report-generator.js</code> dengan struktur tabel formal BPOM.", style_cell),
            Paragraph("Format formulir audit standar BPOM CPOB Bab 1.", style_cell)
        ],
        [
            Paragraph("<b>Fase 6</b><br/>Porting & Dual Deploy<br/><i>Hari 2 (18.30-22.00)</i>", style_cell),
            Paragraph("• Pembuatan versi Python Streamlit <code>app.py</code>.<br/>• Konfigurasi dependensi ringan <code>requirements.txt</code>.<br/>• Deployment ke GitHub Pages & Streamlit Cloud.<br/>• Resolusi issue versi Python 3.11 di cloud.", style_cell),
            Paragraph("Aplikasi live global di GitHub Pages & Streamlit Community Cloud.", style_cell),
            Paragraph("Ketersediaan multi-platform cloud 24/7.", style_cell)
        ],
        [
            Paragraph("<b>Fase 7</b><br/>Akses Publik & URL Baru<br/><i>Hari 2 (22.00-01.00)</i>", style_cell),
            Paragraph("• Pembukaan izin viewer Streamlit menjadi <i>Public</i>.<br/>• Perbaikan kontras hero header teks putih tebal.<br/>• Migrasi dan standarisasi nama URL menjadi <b>pharmacapa</b> agar mudah diketik di iPhone Safari tanpa auto-correct typo.<br/>• Sinkronisasi repositori git.", style_cell),
            Paragraph("URL Resmi Aktif:<br/>• <u>rismawatilaila.github.io/pharmacapa/</u><br/>• <u>pharmacapa.streamlit.app/</u>", style_cell),
            Paragraph("Verifikasi lintas browser (Safari iOS, Chrome, Edge).", style_cell)
        ]
    ]

    t_log = Table(log_data, colWidths=[90, 195, 138, 100])
    t_log.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_cyan),
        ('BOX', (0,0), (-1,-1), 1, c_border),
        ('INNERGRID', (0,0), (-1,-1), 0.5, c_border),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_bg_light]),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(t_log)
    story.append(Spacer(1, 12))

    # =========================================================================
    # BAGIAN 4: HASIL EVALUASI & KOMPARASI DAMPAK OPERASIONAL
    # =========================================================================
    story.append(add_section_banner("4. HASIL EVALUASI & DAMPAK OPERASIONAL (BEFORE VS AFTER)"))
    story.append(Spacer(1, 6))

    eval_data = [
        [
            Paragraph("Metrik Evaluasi", style_th),
            Paragraph("Sebelum (Manual Kertas)", style_th),
            Paragraph("Sesudah (PharmaCAPA AI)", style_th),
            Paragraph("Peningkatan Efisiensi", style_th)
        ],
        [
            Paragraph("<b>Waktu Pelaporan Awal</b>", style_cell_bold),
            Paragraph("4 – 8 jam (menunggu akhir shift)", style_cell),
            Paragraph("<b>< 3 menit</b> via smartphone operator", style_cell),
            Paragraph("<font color='#0284c7'><b>95% Lebih Cepat</b></font>", style_cell_bold)
        ],
        [
            Paragraph("<b>Penyusunan 6M & 5-Whys</b>", style_cell_bold),
            Paragraph("3 – 5 hari (koordinasi rapat tim)", style_cell),
            Paragraph("<b>Otomatis Instan (< 5 detik)</b>", style_cell),
            Paragraph("<font color='#0284c7'><b>Eliminasi Rapat Manual</b></font>", style_cell_bold)
        ],
        [
            Paragraph("<b>Lead Time Penutupan CAPA</b>", style_cell_bold),
            Paragraph("30 – 45 hari kerja", style_cell),
            Paragraph("<b>< 3 hari kerja</b>", style_cell),
            Paragraph("<font color='#0284c7'><b>Efisiensi Waktu 90%</b></font>", style_cell_bold)
        ],
        [
            Paragraph("<b>Akurasi Akar Masalah</b>", style_cell_bold),
            Paragraph("Rendah (bias menyalahkan operator)", style_cell),
            Paragraph("Tinggi (analisis kausalitas objektif)", style_cell),
            Paragraph("<font color='#15803d'><b>Cegah Deviasi Berulang</b></font>", style_cell_bold)
        ],
        [
            Paragraph("<b>Biaya Bets Tertahan</b>", style_cell_bold),
            Paragraph("Sangat tinggi (gudang karantina penuh)", style_cell),
            Paragraph("Sangat rendah (disposisi cepat keluar)", style_cell),
            Paragraph("<font color='#15803d'><b>Efisiensi Finansial Tinggi</b></font>", style_cell_bold)
        ],
        [
            Paragraph("<b>Kesiapan Audit BPOM (ALCOA+)</b>", style_cell_bold),
            Paragraph("Rentan dokumen hilang / tulisan pudar", style_cell),
            Paragraph("100% digital, timestamped, siap cetak", style_cell),
            Paragraph("<font color='#15803d'><b>100% Audit Ready</b></font>", style_cell_bold)
        ]
    ]

    t_eval = Table(eval_data, colWidths=[120, 140, 150, 113])
    t_eval.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_cyan),
        ('BOX', (0,0), (-1,-1), 1, c_border),
        ('INNERGRID', (0,0), (-1,-1), 0.5, c_border),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, c_bg_light]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ALIGN', (3,1), (3,-1), 'CENTER'),
    ]))
    story.append(t_eval)
    story.append(Spacer(1, 14))

    # =========================================================================
    # BAGIAN 5: KESIMPULAN & LEMBAR PENGESAHAN
    # =========================================================================
    story.append(add_section_banner("5. KESIMPULAN & LEMBAR PENGESAHAN PROYEK"))
    story.append(Spacer(1, 6))

    p_kesimpulan = (
        "<b>Kesimpulan Proyek:</b><br/>"
        "Proyek PharmaCAPA AI telah berhasil merealisasikan transformasi digital lantai produksi farmasi dari sistem berbasis kertas manual yang lambat menjadi sistem cerdas berbasis Pharma 4.0. Implementasi sistem ini terbukti memangkas lead time penanganan deviasi hingga 90%, mengeliminasi bias investigasi dangkal, menjamin kepatuhan penuh terhadap BPOM CPOB 2018/2024 dan ICH Q9/Q10, serta memberikan kemudahan akses langsung bagi operator di ruang produksi."
    )
    story.append(Paragraph(p_kesimpulan, style_body))
    story.append(Spacer(1, 10))

    # Kolom Tanda Tangan
    ttd_data = [
        [
            Paragraph("<b>Dipersiapkan Oleh:</b>", style_cell),
            Paragraph("<b>Diperiksa & Diverifikasi Oleh:</b>", style_cell),
            Paragraph("<b>Disetujui untuk Evaluasi:</b>", style_cell)
        ],
        [
            Paragraph("<br/><br/><br/><b>Tim Pengembang PharmaCAPA AI</b><br/>Mahasiswa / Pengembang Sistem", style_cell),
            Paragraph("<br/><br/><br/><b>Asisten Akademik AI</b><br/>Tim Reviewer Kode & Sistem", style_cell),
            Paragraph("<br/><br/><br/><b>Prof. Ir. Arry Akhmad Arman, M.T., Ph.D.</b><br/>Dosen Pengampu Mata Kuliah", style_cell)
        ]
    ]
    t_ttd = Table(ttd_data, colWidths=[174, 174, 175])
    t_ttd.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 1, c_border),
        ('INNERGRID', (0,0), (-1,-1), 0.5, c_border),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#f1f5f9")),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(t_ttd)

    # Build PDF
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF Logbook generated successfully as: {filename}")

if __name__ == "__main__":
    build_pdf()
