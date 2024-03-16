import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Membaca data Excel
data = pd.read_excel('magelang.xlsx', dtype={'NISN': str})

# Konversi kolom yang diperlukan ke tipe data numerik
data[['MAT', 'KMP', 'BIN', 'ING']] = data[['MAT', 'KMP', 'BIN', 'ING']].apply(pd.to_numeric, errors='coerce')

# Definisi fungsi rekomendasi
def rekomendasi(row):
    if row['MAT'] > 75 and row['KMP'] > 75:
        jalur = 'STEM'
        materi = 'Aplikasi Matematika dan Sains dalam Teknologi'
        metode = 'Pembelajaran Berbasis Proyek'
    elif row['BIN'] > 75 and row['ING'] > 75:
        jalur = 'Bahasa'
        materi = 'Literatur dan Studi Kebahasaan Lanjutan'
        metode = 'Diskusi dan Analisis Teks'
    else:
        jalur = 'Campuran'
        materi = 'Pengayaan Interdisipliner'
        metode = 'Pembelajaran Kelompok dan Peer Teaching'

    return pd.Series([jalur, materi, metode])

# Menerapkan rekomendasi untuk semua siswa
data[['Jalur', 'Materi', 'Metode']] = data.apply(rekomendasi, axis=1)

# Menampilkan data dengan rekomendasi di Streamlit
def main():
    st.title('Rekomendasi Jalur, Materi, dan Metode Pembelajaran')
    st.write('Data Siswa:')
    st.write(data)

    # Menampilkan grafik pie rekomendasi jalur
    jalur_counts = data['Jalur'].value_counts()
    st.write('Grafik Pie Rekomendasi Jalur:')
    fig, ax = plt.subplots()
    ax.pie(jalur_counts, labels=jalur_counts.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)

if __name__ == '__main__':
    main()
