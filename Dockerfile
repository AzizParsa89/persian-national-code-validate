# 1. استفاده از ایمیج رسمی پایتون
FROM python:3.9-slim

# 2. تنظیم دایرکتوری کاری
WORKDIR /app

# 3. کپی کردن فایل‌های پروژه
COPY . /app

# 4. نصب وابستگی‌ها
RUN pip install --no-cache-dir -r requirements.txt

# 5. مشخص کردن پورت پیش‌فرض
EXPOSE 5000

# 6. اجرای برنامه با Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
