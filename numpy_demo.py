import numpy as np

dien_list = [8.5, 7.0, 9.2, 5.5, 5.5]  # list Python thuần
dien_array = np.array(dien_list)       # chuyển sang mảng NumPy (array)

print(type(dien_list), type(dien_array))


dien_cong_then = dien_array + 0.5
print(dien_cong_then)


dien_cong_then_list = [dien + 0.5 for dien in dien_list]
print(dien_cong_then_list)

print("Trung binh:", np.mean(dien_array))
print("Lon nhat:", np.max(dien_array))
print("Nho nhat:", np.min(dien_array))
print("Do lech chuan:", round(np.std(dien_array), 2))

ma_tran = np.array([[1, 2, 3], [4, 5, 6]])
print("Ma tran:\n", ma_tran)
print("Kich thuoc (shape):", ma_tran.shape)
print("Ma tran nhan 2:\n", ma_tran * 2)