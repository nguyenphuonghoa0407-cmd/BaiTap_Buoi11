import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('dien_sinh_vien.csv')


tb_mon = df.groupby("mon_hoc")["diem"].mean()
plt.figure(figsize=(6, 4))
plt.bar(tb_mon.index, tb_mon.values, color="skyblue")
plt.title("Diem trung binh theo mon hoc")
plt.savefig("bieu_do_cot.png")
plt.show()


plt.figure(figsize=(6, 4))
plt.plot([1, 2, 3], [6.5, 7.5, 8.5], marker="o", color="green")
plt.title("Xu huong diem qua cac lan kiem tra")
plt.savefig("bieu_do_duong.png")
plt.show()
print("Đã tạo xong 2 file ảnh biểu đồ!")