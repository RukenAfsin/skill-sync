import json

class Product:

    def __init__(self, urunAdi, fiyat, satistami, kategori):
        self.urunAdi = urunAdi
        self.fiyat = fiyat
        self.satistami = satistami
        self.kategori = kategori
        

    @classmethod
    def function(cls):
        def wrapper():
            while True:
                urunAdi = input("ürün adı giriniz: ")
                fiyat = input("Ütün fiyatını giriniz: ")
                satistami = input("ürün satısta mı (evet/hayır): ")
                kategori = input("Hangi kategoride? ")

                if not urunAdi:
                    break

                product=  [
                    {
                    "urunAdi":urunAdi,
                    "fiyat":fiyat,
                    "satistami":satistami,
                    "kategori":kategori
                    }
                ]
                with open("JSON/product.json", "w") as file:
                    json.dump(product, file,ensure_ascii=False,indent=2)
                    file.write("\n")
        return wrapper



def look():
        with open("JSON/product.json","r") as file:
            data=json.load(file)
            print(data)

def main():
    Product.function()()

# look()

main()
