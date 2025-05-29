GÜRÜLTÜ GİDERME VE SES TEMİZLEME PROJESİ
========================================

Bu proje, verilen bir ses dosyasını okuyarak gürültü giderme işlemlerini uygular ve temizlenmiş ses dosyasını oluşturur.
Ayrıca orijinal ve temiz seslerin dalga formları ve spektrogramları grafik olarak gösterilir.


KLASÖR YAPISI
----------------

Proje_Sinyal/
│
├── veriler/
│   ├── Kayit.wav         → Orijinal ses dosyası
│   └── temiz.wav         → Yeni ses dosyası (Temizlenmiş)
│
├── frekans_analizi.py    → Gürültü giderme algoritmaları kullanılan python dosyası
├── grafikler.py          → Ses doyalarının grafiklerini oluşturan python dosyası
└── main.py               → Projeyi çalıştıran ana dosya

GEREKLİ KÜTÜPHANELER
---------------------

Projenin çalışabilmesi için ihtiyacımız olan Python kütüphaneleri:

- numpy
- scipy
- matplotlib
- soundfile

Kütüphane kurulumu için terminalden şunu yazıp çalıştırabilirsiniz:

pip3 install numpy scipy matplotlib soundfile


ÇALIŞTIRMA TALİMATI
-------------------

1. `veriler/` klasörüne `Kayit.wav` adında bir WAV dosyası ekleyin. (Mono veya stereo olabilir.)
2. `main.py` dosyasını çalıştırın: Aşağıdaki komut ile çalıştırın

python main.py 

Dosyayı koşturduktan sonra gerçekleşek olan adımlar:
- İlk olarak ' frekans_analizi.py ' dosyası içindeki fonksiyon çağrılır (ses_temizle) böylece 'veriler/Kayit.wav' dosyası işlenir.
- Ses temizleme işlemlerinin ardından temizlenmiş ses 'veriler/temiz.wav' şeklinde kaydedilir.
- Son olarak orijinal ve temizlenmiş sese ait grafik analizleri sırasıyla gösterilir.

GRAFİK ANALİZLERİ
-----------------

Program koşturulduktan sonra gösterilecek olan grafiklerin sırası aşağıdaki gibi olacaktır.

- Orijinal sesin dalga formu
- Orijinal sesin spektrogramı
- Temizlenmiş sesin dalga formu
- Temizleniş sesin spektrogramı
- İki ses dalgasının üst üste karşılatırılması
- İki spektrogramın yan yana karşılatırılması
- Dalga formu farkı
- Spektrogram farkı


NOTLAR
------

- Orijinal sesin bozuk olması temizleme verimliliğini etkileyebilir.
- ses_temizleme fonkisyonundaki bazı sabitler ihtiyaca göre yeniden ayarlanabilir.
