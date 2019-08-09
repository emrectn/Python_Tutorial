from glob import glob
# Programın çalıştığı yerde bütün ".py" dosyalarını bulmak
tmp = glob("./*.py")

# Klasördeki "module" ile başlayan kelimeleri bulmak
tmp = glob("./module*.py")

# Verilen pathte sadece 1 karakterin farklı olması
tmp = glob("./module_?s.py")

# Range vererek arama yapma örnek olarak alfabetik range
tmp = glob("./module_[a-g]*.py")
print(tmp)