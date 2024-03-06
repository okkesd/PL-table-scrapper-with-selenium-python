import matplotlib.pylab as plt
import math as m

v = 30
g = 9.8
adim = 0.05

theta = [m.pi / 6 + m.pi / 36 * x for x in range(10)] # radyan cinsinden 10 tane aci olusturur
theta_for_legend = [f"{30 + 5*x}\u00b0" for x in range(10)] # grafigin lejantina koymak icin ayni acilari derece cinsinden olusturur
t = [0.0 + adim * x for x in range(200)] # 0'dan 4.95'e kadar 200 tane zaman olusturur
en_uzak = {"aci": 0, "uzaklik": 0} # en uzaga hangi merminin gittigini bu objede tutacagiz

# zamana ve hiza gore x,y konumunu donduren fonksiyon
def konum(aci, zaman, v, g):
    x = v * m.cos(aci) * zaman
    y = (v * m.sin(aci) * zaman) - (g * zaman ** 2) / 2
    return x, y


fig, ax = plt.subplots()

for aci in theta: # her bir aci icin

    # bu aci icin olusturulacak listeleri sifirla
    data_x = []
    data_y = []
    for zaman in t: # zaman vektorundeki her bir zaman icin

        single_data_x, single_data_y = konum(aci, zaman, v, g) #koordinatlari hesapla
        if single_data_y >= 0: # y degeri 0'dan buyukse listeye ekle
            data_x.append(single_data_x)
            data_y.append(single_data_y)
        else:
            break

    # en uzaga gidenin bu aci olup olmadıgına bak
    if (data_x[-1] > en_uzak["uzaklik"]):
        en_uzak["uzaklik"] = data_x[-1]
        en_uzak["aci"] = m.degrees(aci)

    plt.plot(data_x, data_y)

plt.title("Balistik mermi deneyi")
plt.xlabel("Zaman (s)")
plt.ylabel("Yükseklik (m)")
plt.legend(theta_for_legend)

print(en_uzak)
# Cıktı: {'aci': 45.0, 'uzaklik': 91.21677477306463}, en uzaga giden atis 45 derece ile yapilan atistir

plt.show()
