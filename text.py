class Hesab:
    def __init__(self, hesab_nömrəsi, balans):
        self.hesab_nömrəsi = hesab_nömrəsi
        self.balans = balans

    def depozit_et(self, məbləğ):
        self.balans += məbləğ
        print(f"{məbləğ} AZN yatırdınız. Yeni balans: {self.balans} AZN")

    def çıxar(self, məbləğ):
        if self.balans >= məbləğ:
            self.balans -= məbləğ
            print(f"{məbləğ} AZN çəkdiniz. Yeni balans: {self.balans} AZN")
        else:
            print("Kifayət qədər vəsait yoxdur")

    def balansı_göstər(self):
        print(f"Hesab Nömrəsi: {self.hesab_nömrəsi}, Balans: {self.balans} AZN")


class Kredit(Hesab):
    def __init__(self, hesab_nömrəsi, balans, kredit_məbləği):
        super().__init__(hesab_nömrəsi, balans)
        self.kredit_məbləği = kredit_məbləği

    def kredit_ver(self):
        self.depozit_et(self.kredit_məbləği)
        print(f"{self.kredit_məbləği} AZN kredit verildi. Yeni balans: {self.balans} AZN")

    def kredit_ödə(self):
        aylıq_ödəniş = self.kredit_məbləği / 12
        if self.balans >= aylıq_ödəniş:
            self.çıxar(aylıq_ödəniş)
            print(f"{aylıq_ödəniş} AZN kreditin ödənişi etdi. Yeni balans: {self.balans} AZN")
        else:
            print("Krediti ödəmək üçün kifayət qədər vəsait yoxdur")