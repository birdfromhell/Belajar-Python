import gdown as gdown

url = "https://drive.google.com/drive/folders/1NdJP0fyaXn20oCNicLycLU5zKOehJrf_?usp=share_link"
gdown.download_folder(url=url, output=r'D:\Programming\Code\Python\Belajar-Python\100 Day Of Code\Day 13', quiet=False)
