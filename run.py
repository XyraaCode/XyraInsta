import os
if __name__ == "__main__":
        try:
                __import__("RUN.so").cek_lisen_aktif()
        except Exception as e:
                exit(str(e))
