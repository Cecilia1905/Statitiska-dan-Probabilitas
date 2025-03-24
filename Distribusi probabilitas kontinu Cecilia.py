import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Langkah 2: Bangkitkan Data Waktu Pengiriman
# Parameter distribusi
mean = 5  # rata-rata waktu pengiriman dalam hari
std_dev = 2  # standar deviasi dalam hari
sample_size = 1000  # jumlah sampel

# Bangkitkan data waktu pengiriman
shipping_times = np.random.normal(mean, std_dev, sample_size)

# Langkah 3: Buat DataFrame dengan Pandas
# Buat DataFrame
df = pd.DataFrame(shipping_times, columns=['Waktu Pengiriman'])

# Tampilkan 5 baris pertama
print("5 Baris Pertama Data Waktu Pengiriman:")
print(df.head())

# Langkah 4: Visualisasi Distribusi Waktu Pengiriman
plt.figure(figsize=(8, 6))
sns.histplot(df['Waktu Pengiriman'], kde=True, color='blue')
plt.title('Distribusi Waktu Pengiriman Paket')
plt.xlabel('Waktu Pengiriman (hari)')
plt.ylabel('Frekuensi')
plt.show()

# Langkah 5: Analisis Probabilitas
# Probabilitas waktu pengiriman kurang dari 3 hari
prob_less_than_3 = np.sum(df['Waktu Pengiriman'] < 3) / sample_size
print(f"Probabilitas paket dikirim dalam waktu kurang dari 3 hari: {prob_less_than_3:.2f}")

# Probabilitas waktu pengiriman antara 4 dan 7 hari
prob_between_4_and_7 = np.sum((df['Waktu Pengiriman'] >= 4) & (df['Waktu Pengiriman'] <= 7)) / sample_size
print(f"Probabilitas paket dikirim dalam waktu antara 4 dan 7 hari: {prob_between_4_and_7:.2f}")

# Langkah 6: Visualisasi Probabilitas Kumulatif
plt.figure(figsize=(8, 6))
sns.ecdfplot(df['Waktu Pengiriman'], color='green')
plt.title('Probabilitas Kumulatif Waktu Pengiriman Paket')
plt.xlabel('Waktu Pengiriman (hari)')
plt.ylabel('Probabilitas Kumulatif')
plt.show()

# Langkah 7: Analisis Statistik Deskriptif
# Statistik deskriptif
print("Statistik Deskriptif Waktu Pengiriman:")
print(df['Waktu Pengiriman'].describe())
