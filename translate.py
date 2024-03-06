from googletrans import Translator

translator = Translator()

def kelime_cevir(kelime):
    ceviri = translator.translate(kelime, dest='en').text
    return ceviri

while True:
    giris = input("Çevirilecek kelimeyi girin (Çıkmak için 'q' tuşuna basın): ")
    if giris == "q":
        break
    else:
        ceviri = kelime_cevir(giris)
        print(ceviri)
