code=input("işlem yapılacak kodu giriniz: ").upper()
if len(code)!=4:  #burada alınan kodun hane sayı kontrolü yapılıyor.
    print("gecerli bir kod degil.(4 haneli kod giriniz.)")
    exit()

hex = "0123456789ABCDEF"
for i in code :
    if i not in hex: # alınan kodun hex kodu kontrolü.
        print("gecerli bir kod degil.(hex kodu gecersiz)")
        exit()

opcode = code[0]
register=code[1]
address =code[2:4] #alınan kodu parçalara ayırılması.

match opcode: # case yapısı ile op code bölümlerine ayrılıyor.
    case "1":
        print("{} adresindeki bellek hücresinin içeriğini , {} numaralı kaydediciye yükle.".format(address,register))

    case "2":
        print("{} sabit değerini doğrudan {} numaralı kaydediciye yükle.".format(address,register))

    case "3":
        print ("{} kaydedicinin içeriğini {} adresine yaz.".format(register,address))

    case "4":
        print("{} numaralı kaydedicinin içeriğini, {} numaralı kaydediciye kopyala".format(address[0],register))
    
    case "5":
        print("{} ve {} numaralı kaydedicilerin içeriğini topla, sonucu {} numaralı kaydedicide sakla.".format(register,address[0],register))

    case "6":
        print("{} numaralı kaydediciden, {} numaralı kaydedicinin içeriğini çıkar ve sonucu {} numaralı kaydedicide sakla.".format(register,address[0],register))

    case "7":
        print("{} ve {} numaralı kaydedicilerin bit düzeyinde VE (AND) işlemini yap, sonucu {} numaralı kaydedicide saklai".format(register,address[0],register))

    case "8":
        print("{} ve {} numaralı kaydedicilerin bit düzeyinde VEYA (OR) işlemini yap, sonucu {} numaralı kaydedicide saklai".format(register,address[0],register))

    case "9":
        print("{} ve {} numaralı kaydedicilerin bit düzeyinde ÖZEL VEYA (XOR) işlemini yap, sonucu {} numaralı kaydedicide sakla.".format(register,address[0],register))

    case "A":
        print("{} numaralı kaydedicinin içeriğini {} bit kadar döndür.".format(register,address[1]))

    case "B":
        print("programın bir sonraki çalışacağı komutu {} adresine atla.".format(address))

    case "C":
        print("Programın çalışmasını durdur.")

    case _:
        print("Gecerli bir kod değili(Tanımsız opcode girdiniz.)")
