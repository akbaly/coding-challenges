import datetime

# Orijinal film süresini saat ve dakika olarak girin (örnek: 3 saat 18 dakika için 3.18)
orijinal_sure = "2.30"

# İzlemek istediğiniz hızı belirleyin
izleme_hizi = 1.5

# Orijinal süreyi saat ve dakika olarak ayırın
orijinal_saat, orijinal_dakika = map(int, orijinal_sure.split('.'))

# Orijinal süreyi dakika cinsinden hesaplayın
orijinal_sure_dk = orijinal_saat * 60 + orijinal_dakika

# İzleme süresini hesaplayın
izleme_suresi_dk = orijinal_sure_dk / izleme_hizi

# Şu anki saati alın
simdi = datetime.datetime.now()

# Gerçek bitiş zamanını hesaplayın
gercek_bitis_zamani = simdi + datetime.timedelta(minutes=izleme_suresi_dk)

# Gerçek kalan süreyi hesaplayın
gercek_kalan_sure = gercek_bitis_zamani - simdi

# Gerçek kalan süreyi saat ve dakika olarak ayırın
gercek_kalan_saat = gercek_kalan_sure.seconds // 3600
gercek_kalan_dakika = (gercek_kalan_sure.seconds // 60) % 60

# Sonuçları yazdırın
print("Gerçek kalan süre: {} saat {} dakika".format(gercek_kalan_saat, gercek_kalan_dakika))
print("Gerçek bitiş zamanı: {}".format(gercek_bitis_zamani))
