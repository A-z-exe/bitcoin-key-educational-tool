# 🔑 Bitcoin Key Educational Tool

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Python](https://img.shields.io/badge/Python-3.7%2B-green)
![Educational Project](https://img.shields.io/badge/Educational-Only-blue)
![Cryptography](https://img.shields.io/badge/Cryptography-Learning-purple)
![GitHub Repo stars](https://img.shields.io/github/stars/A-z-exe/bitcoin-key-educational-tool?style=social)
![GitHub forks](https://img.shields.io/github/forks/A-z-exe/bitcoin-key-educational-tool?style=social)

یک ابزار **کاملاً آموزشی** برای درک بهتر مفاهیم کلید خصوصی بیت‌کوین و مباحث پایه کریپتوگرافی.

---

## 🚨 اخلاق و قانون

> **⚠️ هشدار مهم:** این ابزار صرفاً برای **یادگیری کریپتوگرافی** طراحی شده است.
> 
> - ✅ **مجاز:** یادگیری، تحقیق، درک مفاهیم کریپتوگرافی
> - ❌ **غیرمجاز:** استفاده برای سرقت، تصاحب غیرقانونی، یا هرگونه فعالیت مخرب
> - 📊 **احتمال پیدا کردن کلید با موجودی:** 1 در 2^256 (عملاً **صفر**)
> - 🎓 **هدف:** آموزش و درک علمی مفاهیم بلاک‌چین

**مسئولیت هرگونه سوءاستفاده کاملاً با کاربر است.**

---

## 🎓 مفاهیم آموزشی

### 🧮 چرا این کار عملاً غیرممکن است؟

| مفهوم | مقدار | توضیح |
|-------|--------|-------|
| **فضای کلید بیت‌کوین** | 2^256 | تعداد کلیدهای ممکن |
| **اتم‌های جهان** | ≈2^265 | تعداد تقریبی اتم‌ها در کل جهان |
| **زمان لازم** | میلیاردها سال | با قدرتمندترین کامپیوترها |
| **احتمال موفقیت** | 0.0000...0001% | عملاً صفر |

### 📚 کاربردهای آموزشی:
- 🔐 درک مفهوم کلید خصوصی/عمومی
- 🔗 آشنایی با الگوریتم‌های هش‌سازی  
- 🌐 یادگیری API های بلاک‌چین
- 💡 درک امنیت کریپتوگرافی
- 🧪 تست و آزمایش مفاهیم

---

## 🌟 ویژگی‌ها

- 🔑 **تولید کلیدهای خصوصی** با استاندارد بیت‌کوین
- 💰 **بررسی موجودی** با چندین API معتبر
- 🎨 **رابط کاربری رنگی** و خوانا
- 📊 **گزارش پیشرفت لحظه‌ای** با آمار دقیق
- 💾 **ذخیره خودکار** نتایج و لاگ‌ها
- 🔄 **چندین روش تولید** کلید (تصادفی، متوالی، ...)
- 📈 **آمار عملکرد** و سرعت بررسی

---

## ⚡ شروع سریع

```bash
# نصب و اجرا در 3 مرحله ساده
git clone https://github.com/A-z-exe/bitcoin-key-educational-tool.git
cd bitcoin-key-educational-tool && pip install -r requirements.txt
python enhanced_bitcoin_key_finder.py
```

---

## 📦 پیش‌نیازها

- **Python 3.7+** (پیشنهاد: 3.9+)
- **اتصال به اینترنت** (برای API ها)
- **سیستم‌عامل:** Windows / Linux / macOS
- **RAM:** حداقل 512 MB

---

## 🛠️ نصب کامل

### روش 1: نصب معمولی
```bash
git clone https://github.com/A-z-exe/bitcoin-key-educational-tool.git
cd bitcoin-key-educational-tool
pip install -r requirements.txt
```

### روش 2: محیط مجازی (پیشنهادی)
```bash
git clone https://github.com/A-z-exe/bitcoin-key-educational-tool.git
cd bitcoin-key-educational-tool
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🚀 استفاده

### اجرای ساده:
```bash
python enhanced_bitcoin_key_finder.py
```

### نمونه خروجی:
```
🔑 Generated Private Key: 5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS
📍 Bitcoin Address: 1F1tAaz5x1HUXrCNLbtMDqcw6o5GNn4xqX  
💰 Balance: 0.00000000 BTC
📊 Checked: 1,247 addresses | Speed: 12.5 addr/sec
```

---

## 📊 آمار و عملکرد

- **سرعت معمول:** 10-50 آدرس در ثانیه
- **وابستگی به API:** سرعت محدود توسط rate limit
- **فایل‌های خروجی:**
  - `found_addresses.txt` - آدرس‌های دارای موجودی
  - `checked_addresses.log` - تاریخچه بررسی‌ها
  - `statistics.json` - آمار کلی

---

## 🔧 تنظیمات

می‌توانید تنظیمات زیر را در کد تغییر دهید:

```python
# تنظیمات قابل تغییر
CHECK_DELAY = 0.1  # تاخیر بین بررسی‌ها (ثانیه)
BATCH_SIZE = 100   # تعداد آدرس در هر batch
API_TIMEOUT = 30   # timeout برای API ها
```

---

## 🔄 API های پشتیبانی شده

- 🌐 **Blockchain.info** - API اصلی
- ⚡ **BlockCypher** - پشتیبان سریع  
- 🔗 **Blockchair** - پشتیبان جامع
- 📊 **BitPay Insight** - پشتیبان اضافی

---

## 🎯 موارد استفاده آموزشی

### 👨‍🎓 برای دانشجویان:
- درس‌های امنیت شبکه
- مباحث کریپتوگرافی
- پروژه‌های دانشگاهی
- تحقیقات بلاک‌چین

### 👨‍💻 برای توسعه‌دهندگان:  
- تست API های بیت‌کوین
- درک ساختار کلیدها
- یادگیری کتابخانه‌های کریپتو
- توسعه اپلیکیشن‌های بلاک‌چینی

---

## 🚫 محدودیت‌ها

- ⏱️ **Rate Limit:** محدودیت تعداد درخواست API
- 🌐 **وابستگی اینترنت:** نیاز به اتصال پایدار
- 💻 **منابع سیستم:** استفاده از CPU برای تولید کلید
- 📊 **احتمال موفقیت:** عملاً صفر (آموزشی است!)

---

## 🛡️ امنیت و حریم خصوصی

- ✅ کلیدهای تولیدی محلی هستند
- ✅ هیچ کلیدی ارسال نمی‌شود
- ✅ فقط آدرس‌ها برای بررسی موجودی چک می‌شوند
- ✅ تمام عملیات روی دستگاه شما انجام می‌شود

---

## 🤝 مشارکت

مشارکت‌ها استقبال می‌شود! لطفاً:

1. **Fork** کنید
2. **Branch** جدید بسازید (`feature/amazing-feature`)
3. **Commit** کنید (`Add: amazing feature`)  
4. **Push** کنید (`origin feature/amazing-feature`)
5. **Pull Request** باز کنید

برای تغییرات بزرگ، ابتدا یک **Issue** باز کنید.

---

## 📄 مجوز

این پروژه تحت [مجوز MIT](LICENSE) منتشر شده است.

---

## 👨‍💻 سازنده

**امیرحسین زارعی**
- 🌐 **GitHub:** [@A-z-exe](https://github.com/A-z-exe)
- 📱 **Telegram:** [@A_Z_exe](https://t.me/A_Z_exe)  
- 📷 **Instagram:** [@A_Z_exe](https://instagram.com/A_Z_exe)

---

## 🙏 تشکر ویژه

- 🪙 **Bitcoin Core** برای مستندات فنی
- 🌐 **Blockchain.info** برای API رایگان
- 🐍 **Python Community** برای کتابخانه‌های عالی
- 💖 ساخته شده با **Python** و **عشق**

---

## 📈 آمار

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)  
![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)
![Educational](https://img.shields.io/badge/Purpose-Educational-yellow.svg)

---

⭐ **اگر این ابزار آموزشی برای شما مفید بود، لطفاً ستاره بدهید!** ⭐

> **یادآوری:** هدف این پروژه صرفاً آموزش است. از آن برای یادگیری استفاده کنید! 🎓
