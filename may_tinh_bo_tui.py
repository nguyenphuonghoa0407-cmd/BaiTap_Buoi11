def main():
    print("== MÁY TÍNH BỎ TÚI ==")
    while True:
        bieu_thuc = input("Nhập phép tính (vd: 5 + 3) hoặc 'thoat': ").strip()
        if bieu_thuc.lower() == "thoat":
            break
        try:
            a, phep, b = bieu_thuc.split()
            a, b = float(a), float(b)
            if phep == "+": res = a + b
            elif phep == "-": res = a - b
            elif phep == "*": res = a * b
            elif phep == "/": res = "Lỗi chia cho 0" if b == 0 else a / b
            else: res = "Phép tính không hợp lệ"
            print("Kết quả:", res)
        except:
            print("Định dạng sai! Ví dụ đúng: 5 + 3")

if __name__ == "__main__":
    main()