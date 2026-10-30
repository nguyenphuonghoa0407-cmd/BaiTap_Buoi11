import pandas as pd

df = pd.read_csv('dien_sinh_vien.csv')
print("--- 5 DÒNG ĐẦU ---")
print(df.head())
print("\n--- ĐIỂM TRUNG BÌNH THEO MÔN ---")
print(df.groupby("mon_hoc")["diem"].mean())
print("\n--- ĐIỂM TRUNG BÌNH TỪNG SINH VIÊN ---")
dien_tb_sv = df.groupby("ho_ten")["diem"].mean().round(2)
print(dien_tb_sv)
print("\n--- SINH VIÊN ĐẠT (>= 5.0) ---")
print(dien_tb_sv[dien_tb_sv >= 5.0])