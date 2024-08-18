#Spotify-Top-Tracks-App
Bu program açık kaynak kodludur ve güvenilirdir. Programın kullanımı basittir. Spotify Developer Portal üzerinden aldığınız "Client ID" ve "Client Secret" 
bilgilerini kullanarak Spotify'da en çok dinlediğiniz şarkıları görüntüleyebilir ve tek tuş ile çalma listesi haline getirebilirsiniz.
Limit kısmına listenin kaç şarkıdan oluşmasını istediğinizi yazmalısınız. "Time Range" kısmında da 3 farklı zaman aralığı bulunuyor.
Bu aralıkların açıklamaları aşağıdaki gibidir: 

short_term: Son 1 ay,
medium_term: Son 6 ay,
long_term: Tüm zamanlar

Spotipy kütüphanesinin kurulumu için terminal'e bunu yazın:
pip install spotipy // Windows
pip3 install spotipy // MacOS

Şimdiden iyi kullanımlar!

DÜZENLEME: Bazı antivirüsler exe dosyası için false-positive sonuç verebiliyor. Kodlar tamamıyla temiz. İsterseniz ChatGPT gibi yapay zekalara kodları gönderip taratabilirsiniz.
Virüs olarak algılanma sebepleri de pyinstaller ile exe dosyası haline getirilmiş olması ve spotipy modülünün Spotify API'den istediği bilgiler, izinler.
Kodu çalıştırmadan önce iyice araştırıp temiz olduğundan emin olabilirsiniz.
