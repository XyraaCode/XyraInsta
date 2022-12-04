if __name__ == "__main__":
        try:
                __import__("enc_uu").cek_lisensi_aktif()
        except Exception as e:
                exit(str(e))
