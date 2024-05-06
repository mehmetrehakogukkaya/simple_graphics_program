
while True:   # Kütüphane eklemeleri için bir döngü oluşturuyoruz.
    import subprocess   # Kütüphane kurulumlarında yardımcı olması için subprocess kütüphanesini içe aktarıyoruz.
    import pip          # Kütüphane kurulumlarında yardımcı olması için pip kütüphanesini içe aktarıyoruz.

    try:  # Kütüphanelerin sorunsuz olarak içe aktarıldığından emin olmak için kullanıyoruz.
        import time   # Gecikme için time kütüphanesini içe aktarıyoruz.
        import matplotlib.pyplot as plt  # Verileri grafiğe döüştürmek için
                                         # matplotlib kütüphanesindeki pyplot modülünü içe aktarıyoruz.
        break  # Kütüphanelerin sorunsuz eklenmesi durumunda döngüyü durduruyoruz.

    except:# İçe aktarırken hata olması durumunda alttaki kodları çalıştırıyoruz(bu kısım .py dosyası ile açanlar için).
        try:  # python.exe' nin dosya yolunu yazarken hata olması durumunda çökmeyi önlemek için try kullanıyoruz.
            python_exe_path = input("python.exe'nin dosya yolunu girin: ")  # kullanıcıdan python.exe' nin yolunu
                                                                            # istiyoruz.
            subprocess.run([python_exe_path, "-m", "pip", "install", "time"]) # python.exe ile kütüphaneyi kuruyoruz.
            subprocess.run([python_exe_path, "-m", "pip", "install", "matplotlib"])#python.exe ile kütüphaneyi
                                                                                   # kuruyoruz.
            break  # Kütüphaneler başarılı bir şekilde içe aktarılınca döngüyü sonlandırıyoruz.
        except FileNotFoundError:  # python.exe' nin dosya yolu yanlış yazılırsa alttaki kod çalışır.
            print("\nDosya yolunu kontrol edin\n:")  # Hata mesajı veriyoruz.
        except Exception as e:  # Oluşan hataları e değişkenine atar ve isteğe bağlı işlem ve düzenleme yapmamıza
                                # olanak tanır.
            print(f"\nBir hata oluştu: {e}\n")   # Hata mesajı ve hata türünü kullanıcıya veriyoruz.
            
version="1.0" # Versiyon bilgisi belirtiyoruz.
print(f"Github link: https://github.com/mehmetrehakogukkaya/simple_graphics_program\n\nv{version}\n\n") # github ve
                                                                                     # versiyon bilgisi yazrıdıyoruz.
time.sleep(2) # Daha stabil bir kullanım için gecikme ekliyoruz(2sn)

print("Kütüphane kurulumları Tamamlandı...")  #Kullanıcıya kütüphane işlemlerinin bittiğini ve programın
                                              # kullanılabilir olduğunu bildiriyoruz
time.sleep(2)  # Daha stabil bir kullanım için gecikme ekliyoruz(2sn)

while True:   # Ana programın döngüde olmasını sağlıyoruz.

    def basla():   # Başlangıç için metod oluşturuyoruz.
        x = []     # Boş liste oluşturuyoruz.
        y = []     # Boş liste oluşturuyoruz.


        print("""\nBu program girilen değerlere göre grafik çizer.  
Çizilen grafik 2D bir düzlemde x,y değerleri ile belirlenir.\n\n
---------------------------------------------\n\n""")     # Temel bilgilendirme metni yazdırıyoruz.

        time.sleep(3)  # kullanıcıya üstteki metni okuması için kısa bir zaman veriyoruz(2sn).

        graphic_name = input("Grafiğe verilecek ismi yazın:")   # Grafiğin başlığını kullanıcıdan istiyoruz.
        time.sleep(0.5)  # Daha stabil bir kullanım için gecikme ekliyoruz(0.5sn)
        x_name = input("yatay(x) ekseni için verilecek ismi yazın:")  # kullanıcıdan yatay(x) eksen için isim istiyoruz.
        time.sleep(0.5)  # Daha stabil bir kullanım için gecikme ekliyoruz(0.5sn)
        y_name = input("dikey(y) ekseni için verilecek ismi yazın:")  # kullanıcıdan dikey(y) eksen için isim istiyoruz.
        time.sleep(0.5)  # Daha stabil bir kullanım için gecikme ekliyoruz(0.5sn)

        while True:
            graphic_grid =input("\nevet(e) hayır(h)\nGrafiğin ızgarası olsun mu? :")  # Izgara olsun mu?
            graphic_grid=graphic_grid.lower() # Kullanıcının büyük harf yazması durumunda hatayı önlemek
                                              # için küçük harfe çeviriyoruz.
            print("\n")
            if "e"==graphic_grid or "evet"==graphic_grid:  # Eğer cevap evet ise...
                plt.grid(True) # ızgarayı açıyoruz.
                break  # Döngüyü sonlandırıyoruz.
            elif "h"==graphic_grid or ""==graphic_grid or "hayır"==graphic_grid:  # Eğer cevap hayır ise...
                plt.grid(False)  # Izgaranın kapalı olduğundan emin olmak için kapatma işlemi yapıypruz.
                break  # Döngüyü sonlandırıyoruz.
            else:  # Hatalı tuşlama yapıldı ise...
                print("Geçersiz giriş, tekrar deneyin!")   # Hata mesajı verip döngünün başa dönmesini sağlıyoruz.


        plt.title(graphic_name)   # Kullanıcıdan aldığımız başlık ismini grafiğe işliyoruz.
        plt.xlabel(x_name)        # Kullanıcıdan aldığımız yatay(x) eksen ismini grafiğe işliyoruz.
        plt.ylabel(y_name)        # Kullanıcıdan aldığımız dikey(y) eksen ismini grafiğe işliyoruz.


        while True:   # Kullanıcının kullanamak istidiği miktarda veriyi girebilmesi için sonsuz döngü oluşturuyoruz.

            try:#Kullanıcının girmiş olduğu verilerin hatalı olması durumunda programın çökmemesi için try kullanıyoruz
                deger = input(f"Değer eklemek için boşluk bırakarak {x_name} ve {y_name} değerlerini sırasıyla yazın\n"
                              f"yada sadece enter tuşlayarak grafiği görüntüleyin: ")   # Kullanıcıdan
                                                                                        # değerleri istiyoruz.
                if deger=="":   # Kullanıcı daha fazla değer girmeyip enter tuşuna bastıysa...
                    print("\n\n\n")
                    break       # Dögüyü sonlandırıyoruz.
                else:           # Sonlandırmadıysa...
                    deger = deger.split()   # Girilen değerleri birbirinden ayırıyoruz.
                    if len(deger) != 2:     # Girilen değerler 2'den az yada fazla ise...
                        raise ValueError    # Doğrudan ValueError kısmına yönlendiriyoruz.
                    x.append(float(deger[0]))   # Ayrılan değerlerden 0. indexdeki değeri(yatay) x listesine ekliyoruz.
                    y.append(float(deger[1]))   # Ayrılan değerlerden 1. indexdeki değeri(dikey) y listesine ekliyoruz.


            except ValueError:   # Programın çökmesine neden olacak bir hata varsa,
                                 # alttaki kodu çalıştırıp döngünün başına dönüyoruz...
                print("Geçersiz giriş, tekrar deneyin!")   # Hata mesajı veriyoruz.

        try:   # x ve y listelerini grafiğe aktarırken, hata durumunda programın çökmemesi için try kullanıyoruz.
            plt.plot(x, y)  # x ve y listelerini grafiğe aktarıyoruz.
            plt.show()    # Grafik ekranını açıyoruz.

        except:  # x ve y listelerini grafiğe aktarırken hata olması durumunda alttaki kodu çalıştırıyoruz...
                print("Geçersiz giriş, tekrar deneyin!")   #hata mesajı veriyoruz.

    print("\n")   # Programın tekrarlaması durumunda karışıklığı önlemek için yeni satıra geçiyoruz
    basla()    # başla metodunu çalıştırıyoruz
    time.sleep(2) # Programın daha stabil bir şekilde ilerlemesi için bir başlangıç süresi ekliyoruz(2sn).
