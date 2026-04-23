# 🔥 Password Al-Qassam Tool

Advanced CLI tool for generating smart password wordlists based on user data.

---

## 📌 Features

* Smart password generation based on personal info
* High / Medium / Low priority system
* Multi-threaded engine (fast generation)
* Password ranking system
* Huge combination generation
* Safe stop with `Ctrl + C`

---

## ⚙️ Installation (Step by Step)

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Mohamed701-call/password_Al-Qassam.git
cd password_Al-Qassam
```

---

### 2️⃣ Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install the tool

```bash
pip install .
```

---

### 4️⃣ Run the tool

```bash
alqassam
```

---

## 🚀 Usage

### Mode 1 (Advanced)

```
High Priority Words: Mohamed, Khaled
Medium Priority: 2001, 1907, asc
Low Priority: 74, nora
```

### What happens:

* Generates all variations:

  * mohamed / MOHAMED / Mo7amed / mOhAmEd
* Combines words in all possible ways:

  * MohamedKhaled
  * KhaledMohamed
* Mixes priorities:

  * Mohamed2001
  * Khaled1907asc74
* Changes order and casing

---

## 📊 Example Output

```
Mohamed
MOHAMED
mo7amed
MohamedKhaled
KhaledMohamed
MO7AMED1907ASC74
mOhAmEd98573398asc74
```

---

## 🧠 How It Works

1. Generate variants لكل كلمة
2. Combine الكلمات بكل ترتيب ممكن
3. Apply transformations:

   * Uppercase / lowercase
   * Leetspeak (a → 4, o → 0)
4. Rank النتائج
5. Save في ملف

---

## ⛔ Notes

* الأداة للأغراض التعليمية فقط
* الاستخدام بدون إذن غير قانوني
* عدد الكلمات ممكن يكون ضخم جدًا

---

## 🛑 Stop the tool

اضغط:

```bash
Ctrl + C
```

---

## 📁 Output

* يتم حفظ النتائج في ملف `.txt`
* كل كلمة في سطر

---

## 💡 Tips

* استخدم كلمات واقعية (اسم + تاريخ + رقم)
* كل ما البيانات أدق → النتائج أقوى

---

## 👨‍💻 Author

Mohamed Khaled
