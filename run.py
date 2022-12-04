if __name__ == "__main__":
        try:
                __import__("RUN").cek_lisen_aktif()
        except Exception as e:
                exit(str(e))
