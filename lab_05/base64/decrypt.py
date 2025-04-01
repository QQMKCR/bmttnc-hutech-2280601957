import base64

def main():
    try:
        with open('data.txt', 'r') as file:
            encoded_string = file.read().strip()

        decoded_bytes = base64.b64decode(encoded_string)
        decoded_string = decoded_bytes.decode('utf-8')

        print("Chuỗi sau khi giải mã:", decoded_string)
    except FileNotFoundError:
        print("File không tồn tại. Vui lòng kiểm tra lại đường dẫn.")

if __name__ == "__main__":
    main()
    