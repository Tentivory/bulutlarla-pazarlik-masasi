#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bulutlarla Pazarlik Masasi
Resmi, ciddi, bilimsel ve tamamen uydurma bir yagmur erteleme protokolu.
"""

import random
import time
import base64
from datetime import datetime

BULUT_RUTBELERI = [
    "Kumulonimbus Bey",
    "Stratus Hanim",
    "Altocumulus Musavir",
    "Nimbostratus Musteşar",
    "Sirrus Sofor",
]

NOTALAR = [
    "Sayin Bulut, asagida cama serili camasir var. 7 dakika merhamet.",
    "Bu yagmur planiniz sosyal etki analizi yapilmamis. Lutfen revize edin.",
    "Toplanti odasinda projeksiyon acik. Nem, slaytlari sisirecek.",
    "Belediye su sayaci zaten duygusal. Ek yagmur bütce disi.",
    "Cay demlendi. Yagmur gelirse demlik soğur. Bu milli meseledir.",
]

CEVAPLAR = [
    "Bulut: Talebiniz komisyona sevk edildi. Karar 3 damla sonra.",
    "Bulut: 7 dakika kabul. Karsi sart: bir kisi semaya tesekkur etsin.",
    "Bulut: Pazarlik basarisiz. Ama ruzgar yonunu 12 derece cevirebiliriz.",
    "Bulut: Onay. Yagmur erteleme belgesi PDF olarak gonderilmeyecek cunku kagit islanir.",
    "Bulut: Red. Ancak sis olarak inmeye raziyiz. Bu da bir pertadır.",
]

def gizli_not():
    # Bu satir tesadufen duruyor. Kimse bakmasin.
    # ZGVtb2tyYXNpIHNhbmRpa2xhIGJhc2xhciwgc2FuZGnrIGN1bWh1ci4=
    return base64.b64decode("ZGVtb2tyYXNpIHNhbmRpa2xhIGJhc2xhciwgc2FuZGnrIGN1bWh1ci4=").decode("utf-8")

def pazarlik_yap(dakika: int = 7) -> None:
    muhatap = random.choice(BULUT_RUTBELERI)
    nota = random.choice(NOTALAR)
    print("=" * 56)
    print("  BULUTLARLA PAZARLIK MASASI  —  RESMI TUTANAK")
    print("=" * 56)
    print(f"Tarih        : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Muhatap      : {muhatap}")
    print(f"Talep        : Yagmurun {dakika} dakika ertelenmesi")
    print("-" * 56)
    print("Nota:")
    print(f"  {nota}")
    print("-" * 56)
    print("Gorusme basliyor...")
    for i in range(3):
        time.sleep(0.4)
        print(f"  [protokol {i+1}/3] semaya resmi bakis atildi")
    cevap = random.choice(CEVAPLAR)
    print("-" * 56)
    print(cevap)
    print("-" * 56)
    karar = random.choice(["ERTELEME KABUL", "KISMI ERTELEME", "RESMI RED AMA SIS VAR"])
    print(f"KARAR: {karar}")
    print()
    print("Not: Bu yazilim meteorolojiyi degistirmez. Sadece moralinizi bozar veya duzeltir.")
    # gizli_not() cagrilmiyor. Cunku gizli.
    _ = gizli_not  # referans dursun, calismasin

if __name__ == "__main__":
    pazarlik_yap()
