from tkinter import *

def submit():
    value1 = entry1.get()
    value2 = entry2.get()
    value3 = entry3.get()
    print("ค่าที่รับเข้ามา:", value1, value2, value3)

root = Tk()
root.title("ตัวอย่างการใช้งาน Textbox")
root.title('ทดสอบโปรแกรม python')
root.geometry('1000x1000')


# สร้างกล่องข้อความแรก
entry1 = Entry(root, width=30)
entry1.pack()

# สร้างกล่องข้อความที่สอง
entry2 = Entry(root, width=30)
entry2.pack()

# สร้างกล่องข้อความที่สาม
entry3 = Entry(root, width=30)
entry3.pack()

# สร้างปุ่ม Submit
submit_button = Button(root, text="Submit", command=submit)
submit_button.pack()

root.mainloop()
