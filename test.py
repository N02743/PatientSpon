import tkinter as tk

# ฟังก์ชันเปลี่ยนหน้า
def show_page(page_name):
    for widget in content_frame.winfo_children():
        widget.destroy()
    label = tk.Label(content_frame, text=f"คุณอยู่ที่หน้า {page_name}", font=("Arial", 20))
    label.pack(expand=True)

# หน้าต่างหลัก
root = tk.Tk()
root.title("แอปตัวอย่าง Top Navigation Bar")
root.geometry("600x400")

# Frame ด้านบน = Navigation Bar
nav_frame = tk.Frame(root, bg="#cccccc", height=40)
nav_frame.pack(side="top", fill="x")

# Frame ด้านล่าง = พื้นที่แสดงเนื้อหา
content_frame = tk.Frame(root, bg="white")
content_frame.pack(side="top", expand=True, fill="both")

# สร้างปุ่มเมนูใน Navigation Bar
pages = ["หน้าแรก", "ข้อมูลยา", "ตั้งค่า"]
for page in pages:
    btn = tk.Button(nav_frame, text=page, command=lambda p=page: show_page(p))
    btn.pack(side="left", padx=10, pady=5)

# แสดงหน้าหลักเริ่มต้น
show_page("หน้าแรก")

# เริ่มต้นแอป
root.mainloop()
