## 🧩 รายละเอียดงาน
สร้างเว็บเซิร์ฟเวอร์อย่างง่ายด้วย **Python Flask** โดยมี 4 เส้นทาง (Routes):

---
<pre> 
⚙️ โครงสร้างไฟล์ที่จำเป็น
flask-project-0755/
├── app.py              # ไฟล์หลัก
└── templates/         
    ├── index.html      # หน้าเว็บแนะนำสถานที่ท่องเที่ยว 
    └── tech.html       # หน้าเว็บแสดงข้อมูลเทคโนโลยี
└── static/
     └── css
└── README.md    
</pre>
---



🚀 ขั้นตอนการติดตั้งและรันเซิร์ฟเวอร์

### 1️⃣ ติดตั้ง Flask
```bash
pip install flask
```

### 2️⃣ สร้างไฟล์ `app.py`
- ใช้คำสั่ง render_template สำหรับหน้าเว็บที่ต้องการแสดงผล HTML 
(หน้าแสดงแนะนำสถานที่ท่องเที่ยว และ หน้าแสดงเทคโนโลยีที่สนใจ)

### 3️⃣ รันเซิร์ฟเวอร์
```bash
python app.py
```


### 4️⃣ เปิดเบราว์เซอร์และเข้าชม

- http://localhost:5000/  
- http://localhost:5000/tech  
- http://localhost:5000/myid  
- http://localhost:5000/draw/3  

---




## 🧠 หลักการทำงาน
- ใช้ **Flask** เพื่อสร้าง Web Server ด้วย Python
- ใช้ `@app.route()` เพื่อกำหนด URL path แต่ละหน้า
- รันเซิร์ฟเวอร์ด้วย `app.run(debug=True)`


---
