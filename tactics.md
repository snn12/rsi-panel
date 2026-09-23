# Taktika Bazası — RSI Panel saytı üçün
# Mənbə: araşdırma (2026-09). Hər taktika Bybit public API ilə hesablana bilir.
# Kline: GET /v5/market/kline (open, high, low, close, volume)
# Funding: GET /v5/market/funding/history | Tickers: GET /v5/market/tickers

## T1 — RSI Ekstrem Reversal (CANLIDIR)
- Market: crypto perp + spot. TF: 1H, 4H.
- Parametr: RSI-14 Wilder.
- Qayda: RSI >= 75 QIZMIŞ (short siqnal zonası), >= 81 ÇOX QIZMIŞ, >= 87 EKSTREM; RSI <= 20 SOYULMUŞ (long siqnal zonası).
- Zəiflik: güclü trenddə RSI zonada ilişib qalır — tək başına giriş deyil, kontekst kimi işlədilir.
- Status: index.html + signals.html-də canlıdır.

## T2 — RSI Trend Rejimi (bullish/bearish zona)
- Market: bütün marketlər. TF: 1H, 4H.
- Parametr: RSI-14.
- Qayda: RSI 50-dən yuxarı = bullish momentum (long tərəfə üstünlük); 50-dən aşağı = bearish. Güclü uptrenddə RSI 40-50 zonasından sıçrayış = long davamı; downtrenddə 50-60-dan geri dönmə = short davamı.
- Data: close kifayətdir.

## T3 — RSI Divergensiya (regular + hidden)
- Market: bütün marketlər, xüsusilə range. TF: 1H, 4H.
- Parametr: RSI-14, pivot gücü 5/5 (hər tərəfdə 5 bar).
- Qayda: Qiymət lower-low, RSI higher-low = bullish divergensiya (dönüş long). Qiymət higher-high, RSI lower-high = bearish. Hidden: qiymət higher-low + RSI lower-low = trend davamı long.
- Təsdiq: divergensiya + şam reversal patterni; stop = pattern altında; TP = 2x ATR.
- Data: high/low/close. Hesablama: swing pivot axtarışı.

## T4 — EMA 12/50 Krossover (trend)
- Market: trend marketləri (crypto perp, qızıl, indeks). Sideways-də whipsaw verir.
- Parametr: EMA-12, EMA-50.
- Qayda: EMA12 yuxarı kəsdi = long; aşağı kəsdi = çıx/sell. Stop = əvvəlki swing low. Yalan siqnal filtri: kəsişmədən sonra məsafə kiçikdirsə (<5%) və qiymət EMA12 üzərindədirsə güclü say.
- Data: close, minimum 60+ şam (hazırda limit=50 — bu taktika üçün limit 100+ lazımdır).

## T5 — Golden Cross / Death Cross (SMA 50/200)
- Market: spot, ETF, stocks, gündəlik TF. Gecikən təsdiq siqnalıdır, giriş üçün deyil.
- Parametr: SMA-50, SMA-200.
- Qayda: SMA50 yuxarı kəsdi = golden cross (bullish struktur); aşağı = death cross. Təsdiq: kəsişmədə hər iki MA yuxarı baxır + qiymət hər ikisinin üstündə + həcm yüksək.
- Data: close, minimum 210+ şam (hazırda limit=50 — bu taktika üçün limit 250 lazımdır).

## T6 — MACD 12/26/9 Krossover + Histogram
- Market: bütün marketlər. TF: 1H, 4H, 1D.
- Parametr: EMA-12, EMA-26, signal EMA-9.
- Qayda: MACD xətti signalı yuxarı kəsdi = bullish; histogram 0-dan yuxarı = momentum təsdiqi. Divergensiya (qiymət vs histogram) dönüş xəbərçisidir.
- Data: close, minimum 40+ şam.

## T7 — Bollinger 20/2: Walk, Tag, %b
- Market: bütün marketlər. Standart: SMA-20, ±2 SD (içində ~90% data).
- Qayda: %b >= 1 (üst banddan yuxarı bağlanış) = güc/davam siqnalı, reversal deyil; %b <= 0 əksi. Trenddə qiymət bandı "gəzir" (walk) — əksinə trade etmək olmaz.
- Qayda (Bollingerin özü): band tag-i tək başına sell/buy deyil.
- Data: close, 25+ şam.

## T8 — Bollinger Squeeze (sıxılma → partlayış)
- Market: crypto perp (güclü partlayışlar), forex. Yönü demir, yalnız "böyük hərəkət yaxındır" deyir.
- Parametr: BB 20/2, BandWidth = (üst-alt)/orta.
- Qayda: BandWidth 6 aylıq minimumda (və ya son 120 şamın ən dar 5%-i) = SQUEEZE. Giriş: üst banddan yuxarı təsdiqli bağlanış + həcm sıçrayışı = long (əksi short). Stop: orta SMA altı və ya 1.5x ATR.
- Data: high/low/close/volume, 130+ şam (tarix müqayisəsi üçün limit 200 tövsiyə).

## T9 — ATR Stop Ölçüsü (2-3x ATR)
- Market: bütün marketlər. Bu giriş deyil, risk filtridir.
- Parametr: ATR-14.
- Qayda: stop məsafəsi = 2x ATR (aqressiv) / 3x ATR (geniş). TP = 2x ATR (1:2 R:R üçün) və ya trailing.
- Data: high/low/close, 20+ şam.

## T10 — Donchian Breakout 20 + Həcm
- Market: futures, əmtəə, likvid perp-lər.
- Parametr: 20 şamın ən yüksək high / ən aşağı low.
- Qayda: 20 şamlıq yuxarı qırılma = long; həcm təsdiqi (cari həcm > orta həcm 20) yalan qırılmaları ~ yarıya endirir (təxminən 56% → 47% fail).
- Data: high/low/close/volume, 30+ şam.

## T11 — Funding Rate Kontrarian (yalnız perp)
- Market: YALNIZ crypto perpetual. Bybit: 8 saatdan bir.
- Parametr: son funding rate + 7 günlük orta.
- Qayda: funding >= +0.05%/8h = kalabalık long, flush riski (long-a ehtiyatla, dar stop). <= -0.05%/8h = kalabalık short, squeeze riski (short-a ehtiyatla). Neytral ±0.01% = siqnal yox. Tək başına giriş deyil — risk konteksti kimi.
- Data: GET /v5/market/funding/history (200 record) və ya tickers → fundingRate.
- Qeyd: trenddə funding həftələrlə yüksək qala bilir — yüksək funding = avtomatik short deyil.

## T12 — Həcm Sıçrayışı + RSI Təsdiqi
- Market: bütün marketlər.
- Parametr: həcm SMA-20, RSI-14.
- Qayda: cari həcm > 2x orta həcm + RSI zonaya girir (≥70 və ya ≤30) = iştiraklı hərəkət, siqnal güclü say. Həcm təsdiqsiz RSI ekstremi zəif say.
- Data: close + volume, 30+ şam.

## Skor sistemi (sayt üçün plan)
- Hər coin hər taktikadan keçir/keçmir (1/0) alır.
- Sonda cəmi bal: məs. 12 taktikadan 7+ keçənlər "GÜCLÜ", 4-6 "ORTA".
- Hər taktikanın market etiketi olur (PERP / SPOT / STOCK ...).
- Taktikalar ASAN → ÇƏTİN sırası ilə əlavə olunur: T2, T6, T7, T9, T12 (asan) → T4, T10, T11 → T3, T8, T5 (çətin, çox data lazım).

## Market bölmələri (saytda canlıdır)
- CRYPTO PERP (110-dan ~95-i): T1 (75/81/87/20, 1H/4H), sonra T2, T4, T6, T7, T8, T9, T10, T11, T12.
- STOCKS (12 simvol: AAPL, NVDA, TSLA, META, MSTR, INTC, MU, SNDK, SKHYNIX, SAMSUNG, SOXL, SOXS — hamısı Bybit linear, qiymətlə doğrulandı): T2, T5 (əsas), T6, T7. Ekstrem hədlər fərqli olacaq: 70/30 (təsdiqlənəcək, hazırda 75/20 göstərir).
- ƏMTƏƏ (3 simvol: XAU qızıl, XAG gümüş, XAUT): T2, T4, T6 (trend). Qızıl trend marketidir — reversal taktikaları ehtiyatla.
- Qayda: eyni taktika adı fərqli marketdə = ayrı parametr dəsti + ayrı market etiketi. Parametrsiz köçürmək olmaz.

## T13 — XAU Bullish Reversal Setup (CUSTOM, CANLIDIR)
- Market: YALNIZ XAU (XAUUSDT). Mənbə: istifadəçinin şəxsi setup-ı.
- Struktur (göndərilən rəqəmlər nümunə idi — sayt dinamik hesablayır): dəstək = son 50 4H şamın dibi; hədəf T1 = son zirvə; T2 = zirvə + (zirvə-dəstək) ölçülmüş hərəkət. Pozulma: dəstək decisiv qırılsa.
- Saytda hesablanan qayda: qiymət >= dinamik dəstək + RSI-4H >= 50 = 1 XAL, əks halda 0. Trend xətti + bulud qırılması vizual təsdiq kimi qeyddədir (sayt hesablamır).
- Risk: 1-2% kapital, stop dəstək altında.
- Status: coin.html-də T13 sətri + skor.html-də 1 xal + analysis/xauusdt.md.

## Skor sistemi (CANLIDIR — skor.html)
- Hər taktika 1 xal: T1 ekstrem • T2 zona • T4 trend • T6 momentum • T7 band • T11 funding • T12 həcm • T13 XAU setup (yalnız XAU).
- Maksimum: 7 (XAU üçün 8). Səhifədə hədd seçimi: Hamısı / 2+ / 3+ / 4+, bal sırasına görə düzülür, keçən taktikaların hamısı görünür.
