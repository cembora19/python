from operator import mod


PATH="day24IntermediateFilesDirectoriesPaths\\"

#BİLGİLENDİRME: OPEN FONKSİYONLARINDA MODLAR VAR
# A MODU APPEND YANİ DOSYAYA EKLEMME YAPIYOR(İLAVE)
# W MODU WRİTE İÇİNDEKİ HER ŞEYİ SİLİP VERİLEN DEĞERİ GİRİYOR VE EĞER HİÇ OKUŞTURULMAMIŞ BİR DOSYAYI WRITE MODUNDA ÇALIŞTIRMAYA ÇALIŞIRSAN SENİN İÇİN OTOMATİKMAN YENİ BİR DOSYA OLUŞTURUYOR
# R READ MODU ONU ZATEN BİLİYORUZ

# with open(f"{PATH}my_file.txt") as file:
#     contents=file.read()
#     print(contents)

# with open(f"{PATH}my_file.txt", mode="w") as file:
#     file.write("deneme1")

with open(f"{PATH}my_file.txt", mode="a") as file:
    file.write("\nappend yaptik bakalim")

with open(f"{PATH}new_file.txt", mode="w") as file:
    file.write("new file opened.")