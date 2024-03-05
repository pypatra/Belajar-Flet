

data_time = int(input("Berapa Lama (Menit)\t:")) * 60

for i in range(data_time,0,-1):
  detik = int(i) % 60
  menit = int(i/60) % 60
  print(f"{menit:02}:{detik:02}")