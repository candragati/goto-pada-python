def tembaklagi():
    pilihan={0:'A. Yes',1:'B. Tidak',2:'C. Diemin aja'}
    for i in range(len(pilihan)):
        print [i], pilihan[i]
    pilih = input("Will you marry me? ")
   
    if pilih == 0:
        print pilihan[0]
    else:
        tembaklagi()
tembaklagi()