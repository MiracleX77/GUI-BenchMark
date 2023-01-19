import time,os.path,os
from tkinter import *
CPU_SCORE = 0
DISK_SCORE = 0
MEM_SCORE = 0

GB = 1073741824

def Cpu_benchmark():
    global CPU_SCORE
    print("Start CPU Benchmark.")
    start_time = time.time()

    i=0
    
    while  i <= 42317783 :
        cal = i*2+(i+1)*2-(i+2)*(i-2)-(i+3)*(i-3)    
        i += 1
    
    end_time = time.time()
    run_time = end_time-start_time

    CPU_SCORE=Calculation_score(run_time)
    entry_cpu.configure(state="normal")
    entry_total.configure(state="normal")
    entry_cpu.delete(0,'end')
    entry_total.delete(0,'end')
    entry_cpu.insert(0,CPU_SCORE)
    entry_total.insert(0,CPU_SCORE+DISK_SCORE+MEM_SCORE)
    entry_cpu.configure(state="readonly")
    entry_total.configure(state="readonly")




def Memory_benchmark():
    global MEM_SCORE
    print("Start Memmory Benchmark.")

    Empty_list = []
    start_time = time.time()
    while True :
        Empty_list.append(list())
        if Empty_list.__sizeof__() > GB:
            break
    
    end_time = time.time()
    run_time = end_time-start_time

    MEM_SCORE=Calculation_score(run_time)
    entry_memory.configure(state="normal")
    entry_total.configure(state="normal")
    entry_memory.delete(0,'end')
    entry_total.delete(0,'end')
    entry_memory.insert(0,MEM_SCORE)
    entry_total.insert(0,CPU_SCORE+DISK_SCORE+MEM_SCORE)
    entry_memory.configure(state="readonly")
    entry_total.configure(state="readonly")
    


def Disk_benchmark():
    global DISK_SCORE
    print("Start Disk Benchmark.")
    start_time = time.time()
    file_name = 'demofile.txt'

    if os.path.exists(file_name): # เช็คว่ามีไฟล์เดิมอยู่เเล้วหรือไม่calculation
        os.remove(file_name)    #ถ้ามีก็จะ ลบไฟล์เดิมทิ้ง เเล้วไปสร้างใหม่
    
    f = open(file_name, "wb+")
    
    junk_files=bytes(536870912) #  การสร้างไฟล์ขยะขนาด 500 Mb

    while True:
        f.write(junk_files)
        file_size = os.path.getsize(file_name)
        if file_size >= (GB):
            f.close()
            break
    os.remove(file_name) # จากการสร้างเสร็จก็ทำการลบไฟล์ เพื่อไม่ให้เก็บไว้ในเครื่อง
    
    end_time = time.time()
    run_time = end_time-start_time

    DISK_SCORE=Calculation_score(run_time)
    entry_disk.configure(state="normal")
    entry_total.configure(state="normal")
    entry_disk.delete(0,'end')
    entry_total.delete(0,'end')
    entry_disk.insert(0,DISK_SCORE)
    entry_total.insert(0,CPU_SCORE+DISK_SCORE+MEM_SCORE)
    entry_disk.configure(state="readonly")
    entry_total.configure(state="readonly")


def Calculation_score(runtime):
    if runtime<20:
        score = 30000 - runtime*250             #5000/20 = 250
    elif runtime <100:
        score = 25000 - (runtime-20)*62.5       #5000/(100-20)=62.5
    elif runtime <300:
        score = 20000 - (runtime-100)*25        #5000/(300-100)=25
    elif runtime <600:
        score = 15000 - (runtime-300)*16.67     #5000/(600-300)=16.67
    elif runtime <1000:
        score = 10000 - (runtime-600)*12.5      #5000/(1000-600)=12.5
    else:
        score = 5000 - (runtime-1000)*8         # 8 จากการคาดเดา โดยดูการลดตัวคูณลงมาเรื่อยๆ
    return round(score,2)
    

root = Tk()
root.title("Bench Mark Program")
root.configure(bg="")
root.resizable(width=False, height=False)


head_frame = Frame(bg="#FEF7CC",highlightbackground="white",highlightthickness=10)
head_frame.place(x=20, y=20, width=520, height=80)

run_frame = Frame(bg="#FEF7CC",highlightbackground="white",highlightthickness=10)
run_frame.place(x=45, y=125, width=300, height=350)

display_frame = Frame(bg="#FEF7CC",highlightbackground="white",highlightthickness=10)
display_frame.place(x=360, y=125, width=600, height=350)

    #ใส่ข้อความบนหน้าจอ
Head = Label(text="BENCH MARK BY SOFTSELL", font=("arial", 25,"bold"),fg="black",bg="#FEF8CF")
Head.place(x=30, y=35,width=500 ,height=50)

label_cpu = Label(text="CPU ", fg="black" ,bg="#FEF8CF", font=20 )
label_cpu.place(x=80, y=180 ,width=80 ,height=50)

label_memory = Label(text="MEMORY ", fg="black" ,bg="#FEF8CF", font=20)
label_memory.place(x=80, y=280 ,width=80 ,height=50)

label_disk = Label(text="DISK ", fg="black" ,bg="#FEF8CF", font=20)
label_disk.place(x=80, y=380 ,width=80 ,height=50)

label_score_cpu = Label(text="CPU SCORES : ", fg="black" ,bg="#FEF8CF", font=20)
label_score_cpu.place(x=415, y=180 ,width=150 ,height=50)

label_score_memory = Label(text="MEMORY SCORES : ", fg="black" ,bg="#FEF8CF", font=20)
label_score_memory.place(x=415, y=280 ,width=150 ,height=50)

label_score_disk = Label(text="DISK SCORES : ", fg="black" ,bg="#FEF8CF", font=20)
label_score_disk.place(x=415, y=380 ,width=150 ,height=50)

label_total = Label(text="TOTAL :", font=("arial", 20,"bold"),fg="black",bg="#F6EEE0")
label_total.place(x=565, y=40,width=120 ,height=50)

    #กล่องแสดงผลการรัน
entry_cpu = Entry(font=("arial", 30),fg="black",bg="pink",border=1.1,justify="right",textvariable=CPU_SCORE)
entry_cpu.place(x=580, y=185 ,width=300 ,height=40)


entry_memory = Entry(font=("arial", 30),fg="black",bg="pink",border=1.1,justify="right")
entry_memory.place(x=580, y=285,width=300 ,height=40)

entry_disk = Entry(font=("arial", 30),fg="black",bg="pink",border=1.1,justify="right")
entry_disk.place(x=580, y=385 ,width=300 ,height=40)

entry_total = Entry(font=("arial", 30),fg="black",bg="pink",border=1.1,justify="right")
entry_total.place(x=710, y=35 ,width=250 ,height=60)

    #ปุ่มรันโปรแกรม
botton_cpu = Button(text="Run", font=("arial",15,"bold"),fg="black",bg="#C7E7FD",border=0,command = Cpu_benchmark)
botton_cpu.place(x=200, y=175 ,width=100 ,height=50)

botton_memory = Button(text="Run", font=("arial",15,"bold"),fg="black",bg="#C7E7FD",border=0 ,command = Memory_benchmark)
botton_memory.place(x=200, y=275 ,width=100 ,height=50)

botton_disk = Button(text="Run", font=("arial",15,"bold"),fg="black",bg="#C7E7FD",border=0,command = Disk_benchmark)
botton_disk.place(x=200, y=375 ,width=100 ,height=50)


    #กำหนดขนาดหน้าจอ
root.geometry("1000x500")
root.mainloop()
