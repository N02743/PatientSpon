import tkinter as tk
import random

global PATIENT_DATA

global TEST

def generate_timeline_data():
    data = []

    for i in range(20):
        x = random.randint(1, 30)
        data.append([f"drug {i}", x, random.randint(1, 31 - x) + x])
    
    return data

def get_timeline_data():
    # TODO: loading patient data
    
    
    # dummy data by random gen
    return generate_timeline_data()

def plot_timeline():
    print()
    

# def print_something(text):
#     print(text)

PATIENT_DATA = get_timeline_data()

TEST = 10

TEST = 12

app = tk.Tk()

app.title("Patient Spon form program")

# en1 = tk.Entry(app)
# en1.pack()

# data = generate_timeline_data()
# t1 = tk.Label(app, text=data)
# t1.pack()
print(PATIENT_DATA)
print(TEST)

app.state('zoomed')







# ฟังก์ชันเปลี่ยนหน้า
def show_page(page_name):
    for widget in content_frame.winfo_children():
        widget.destroy()
    label = tk.Label(content_frame, text=f"คุณอยู่ที่หน้า {page_name}", font=("Arial", 20))
    label.pack(expand=True)


# Frame ด้านบน = Navigation Bar
nav_frame = tk.Frame(app, bg="#cccccc", height=150)
nav_frame.pack(side="top", fill="x")
nav_frame.pack_propagate(False)

# Frame ด้านล่าง = พื้นที่แสดงเนื้อหา
content_frame = tk.Frame(app, bg="white")
content_frame.pack(side="top", expand=True, fill="both")

# สร้างปุ่มเมนูใน Navigation Bar
pages = ["หน้าแรก", "ข้อมูลยา", "ตั้งค่า"]
for page in pages:
    btn = tk.Button(nav_frame, text=page, command=lambda p=page: show_page(p))
    btn.pack(side="left", padx=10, pady=5)

# แสดงหน้าหลักเริ่มต้น
show_page("หน้าแรก")


# TODO: make nav bar

# TODO: push git







app.mainloop()
