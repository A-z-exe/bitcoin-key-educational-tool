# Bitcoin Key Educational Tool

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Python](https://img.shields.io/badge/Python-3.9%2B-green)
![Educational Project](https://img.shields.io/badge/Educational-Only-blue)
![CI](https://github.com/A-z-exe/bitcoin-key-educational-tool/actions/workflows/ci.yml/badge.svg)

ابزاری **صرفاً آموزشی** برای دیدن این‌که یک کلید خصوصی بیت‌کوین چطور ساخته می‌شود،
چطور به آدرس تبدیل می‌شود و چگونه می‌توان موجودی یک آدرس را از API عمومی خواند.

---

## ⚠️ هشدار اخلاقی و قانونی

> این برنامه برای **یادگیری** است، نه برای پیدا کردن پول.
>
> - ✅ مجاز: یادگیری کریپتوگرافی، آزمایش API، پروژهٔ درسی
> - ❌ غیرمجاز: سرقت، تصاحب کلید دیگران، هر فعالیت مخرب
> - 📊 احتمال تصادفی رسیدن به کلیدی با موجودی: حدود ۱ در ۲^۲۵۶ (عملاً صفر)
>
> مسئولیت هر نوع سوءاستفاده کاملاً با کاربر است.

هیچ کلیدی از دستگاه شما خارج نمی‌شود؛ فقط آدرس‌ها برای خواندن موجودی به API
عمومی فرستاده می‌شوند.

---

## ابزار چه کاری انجام می‌دهد

1. با `bitcoinlib` یک کلید خصوصی و آدرس متناظر می‌سازد
2. موجودی آدرس را از BlockCypher یا blockchain.info می‌خواند
3. آدرس‌های دارای موجودی را در فایل ذخیره می‌کند
4. آمار سرعت و تعداد بررسی را در ترمینال نشان می‌دهد

---

## نصب

```bash
git clone https://github.com/A-z-exe/bitcoin-key-educational-tool.git
cd bitcoin-key-educational-tool
python -m venv venv
# Windows: venv\Scripts\activate    |    Linux/macOS: source venv/bin/activate
pip install -r requirements.txt
```

پیش‌نیازها: Python 3.9+، `bitcoinlib`، `requests`، `colorama`، اتصال اینترنت برای API.

---

## اجرا

```bash
python enhanced_bitcoin_key_finder.py
```

برنامه دو مقدار می‌پرسد:

| پرسش | پیش‌فرض | سقف |
|------|---------|-----|
| تعداد تلاش | ۱۰۰ | ۱۰۰۰ |
| محدودهٔ زمانی (دقیقه) | ۵ | ۳۰ |

---

## خروجی‌ها

| فایل | محتوا |
|------|-------|
| `found_bitcoin_keys.json` | آدرس، کلید خصوصی، موجودی و زمان (اگر چیزی پیدا شود) |
| `found_bitcoin_keys.txt` | همان نتیجه به‌صورت یک خط متنی |
| `bitcoin_finder.log` | لاگ اجرا و خطاهای API |

هر سه فایل در `.gitignore` هستند.

---

## چرا پیدا کردن کلید تصادفی عملاً غیرممکن است؟

| مفهوم | مقدار |
|-------|--------|
| فضای کلید بیت‌کوین | 2^256 |
| اتم‌های جهان | حدود 2^265 |
| زمان لازم با سخت‌افزار امروزی | میلیاردها سال |
| احتمال موفقیت در یک اجرا | عملاً صفر |

این پروژه برای نمایش همین واقعیت ساخته شده است، نه برای دور زدن آن.

---

## محدودیت‌ها

- نرخ درخواست API محدود است؛ برنامه بین APIها جابه‌جا می‌شود و backoff دارد
- فقط دو API عمومی پشتیبانی می‌شوند (BlockCypher و blockchain.info)
- اجرای طولانی روی شبکه‌های محدود ممکن است به rate limit بخورد

---

## مشارکت

Fork کنید، یک branch بسازید، تغییر را commit کنید و Pull Request باز کنید.
برای تغییرات بزرگ اول Issue باز کنید.

---

## مجوز

MIT — فایل [LICENSE](LICENSE).

نویسنده: [AmirHossein Zarei](https://a-z-exe.github.io/) · [GitHub](https://github.com/A-z-exe)
