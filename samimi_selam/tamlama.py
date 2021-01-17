from samimi_selam.isimler import TURKISH_NOUNS

sozluk = set(TURKISH_NOUNS)

def son_sesli_harf(word):
	match = re.search(r'([aeıioöuü])[^aeıioöuü]*$', word)
	if match:
		return match.group(1)

def sozlukte_bulunur(sozcuk):
    return sozcuk in sozluk


def eki_al(sozcuk, ek_uzunlugu):
    return sozcuk[-ek_uzunlugu:]


def koku_al(sozcuk, ek_uzunlugu):
    return sozcuk[:-ek_uzunlugu]


def kucuk_harfe_cevir(sozcuk):
    sozcuk.lower()


def son_sesli_duzdur(sozcuk):
    return son_sesli_harf(sozcuk) in {"a", "e", "ı", "i", "â", "î"}


def son_sesli_yuvarlaktir(sozcuk):
    return not son_sesli_duzdur(sozcuk)


def son_sesli_incedir(sozcuk):
    return son_sesli_harf(sozcuk) in {"e", "i", "ö", "ü", "î"}


def son_sesli_kalindir(sozcuk):
    return not son_sesli_incedir(sozcuk)


def kaynastirmasiz_ektir(tamlama_eki):
    return len(tamlama_eki) == 1


def son_harfi_kalinlastir(kok):
    kalin_harita = {"b": "p", "c": "ç", "d": "t", "g": "k", "ğ": "k"}
    son_harf = kok[-1]
    kalin_son_harf = kalin_harita.get(son_harf)
    if kalin_son_harf:
        return kok[:-1] + kalin_son_harf


def tamlama_ekini_temizle_ozel(sozcuk, tamlama_eki, sekil_uyumu, ses_uyumu):
    ek_uzunlugu = len(tamlama_eki)
    ek = eki_al(sozcuk, ek_uzunlugu)
    kok = koku_al(sozcuk, ek_uzunlugu)
    kalin_kok = son_harfi_kalinlastir(kok)

    if ek == tamlama_eki and sekil_uyumu(kok) and ses_uyumu(kok):
        if sozlukte_bulunur(kok):
            return kok
        elif kalin_kok and sozlukte_bulunur(kalin_kok):
            return kalin_kok


def tamlama_ekini_temizle(sozcuk):
    temiz_sozcuk = tamlama_ekini_temizle_ozel(
        sozcuk, "i", son_sesli_duzdur, son_sesli_incedir
    )
    if temiz_sozcuk:
        return temiz_sozcuk
    temiz_sozcuk = tamlama_ekini_temizle_ozel(
        sozcuk, "si", son_sesli_duzdur, son_sesli_incedir
    )
    if temiz_sozcuk:
        return temiz_sozcuk
    temiz_sozcuk = tamlama_ekini_temizle_ozel(
        sozcuk, "ı", son_sesli_duzdur, son_sesli_kalindir
    )
    if temiz_sozcuk:
        return temiz_sozcuk
    temiz_sozcuk = tamlama_ekini_temizle_ozel(
        sozcuk, "sı", son_sesli_duzdur, son_sesli_kalindir
    )
    if temiz_sozcuk:
        return temiz_sozcuk
    temiz_sozcuk = tamlama_ekini_temizle_ozel(
        sozcuk, "u", son_sesli_yuvarlaktir, son_sesli_kalindir
    )
    if temiz_sozcuk:
        return temiz_sozcuk
    temiz_sozcuk = tamlama_ekini_temizle_ozel(
        sozcuk, "su", son_sesli_yuvarlaktir, son_sesli_kalindir
    )
    if temiz_sozcuk:
        return temiz_sozcuk
    temiz_sozcuk = tamlama_ekini_temizle_ozel(
        sozcuk, "ü", son_sesli_yuvarlaktir, son_sesli_incedir
    )
    if temiz_sozcuk:
        return temiz_sozcuk
    temiz_sozcuk = tamlama_ekini_temizle_ozel(
        sozcuk, "sü", son_sesli_yuvarlaktir, son_sesli_incedir
    )
    if temiz_sozcuk:
        return temiz_sozcuk
    return sozcuk
