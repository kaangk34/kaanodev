import pandas as pd 

  

data = { 

 'Bolunme': [1, 2, 3, 4, 5, 6, 7, 8], 

 'Sol': ['Maas=Normal', 'Maas=Yuksek', 'Maas=Dusuk', 'Deneyım=Yok', 'Deneyım=Orta',   'Deneyım=Iyı', 'Gorev=Uzman', 'Gorev=Yonetıcı'],   

'Sağ': ['Maas={Dusuk,Yuksek}', 'Maas={Dusuk,Normal}', 'Maas={Normal,Yuksek}', 'Normal={Orta,Iyı}', 'Normal={Yok,Iyı}', 'Deneyım={Yok,Orta', 'Gorev=Yonetıcı', 'Gorev=Normal'] 

} 

df = pd.DataFrame(data) 

print(df) 


data ={
    'Personel': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 

    'Maas': ['Normal', 'Yuksek', 'Dusuk', 'Yuksek', 'Dusuk', 'Yuksek', 'Dusuk', 'Yuksek', 'Dusuk', 'Yuksek', 'Dusuk'], 

    'Deneyım ': ['Orta', 'Yok', 'Yok', 'Orta', 'Orta', 'Iyı', 'Iyı', 'Orta', 'Orta', 'Iyı', 'Iyı'],

    'Gorev': ['Uzman', 'Uzman', 'Yonetıcı', 'Yonetıcı', 'Yonetıcı', 'Yonetıcı', 'Yonetıcı', 'Uzman', 'Uzman', 'Uzman', 'Uzman'], 

    'MEMNUN': ['Evet', 'Evet', 'Evet', 'Evet', 'Evet', 'Evet', 'Evet', 'Hayır', 'Hayır', 'Hayır', 'Hayır'] 
}

df = pd.DataFrame(data) 
data = { 

    'Bolunme': [1, 2, 3, 4, 5, 6, 7, 8], 

    'BSol': [1, 5, 5, 2, 5, 4, 6, 5], 

    'PSol': [0.09, 0.45, 0.45, 0.18, 0.45, 0.36, 0.55, 0.45], 

    'Sınıf': [1, 3, 3, 2, 3, 2, 2, 5], 

    'SınıfHayır': [0, 2, 2, 0, 2, 2, 4, 0], 

    'P(Evet|TSol)': [1, 0.6, 0.6, 1, 0.6, 0.5, 0.33, 1], 

    'P(Hayır|TSol)': [0, 0.4, 0.4, 0, 0.4, 0.5, 0.67, 0] 

} 

  

dafr = pd.DataFrame(data) 

print("Sol Tarafta Olasılıksal Degerler:") 

print(dafr) 

  

data = { 

    'Bolunme': [1, 2, 3, 4, 5, 6, 7, 8], 

    'BSag': [10, 6, 6, 9, 6, 7, 5, 6], 

    'PSag': [0.91, 0.55, 0.55, 0.82, 0.55, 0.64, 0.45, 0.55], 

    'SınıfEvet': [6, 4, 4, 5, 4, 5, 5, 2], 

    'SınıfHayır': [4, 2, 2, 4, 2, 2, 0, 4], 

    'P(Evet|TSag)': [0.6, 0.67, 0.67, 0.56, 0.67, 0.71, 1, 0.33], 

    'P(Hayır|TSag)': [0.4, 0.33, 0.33, 0.44, 0.33, 0.29, 0, 0.67] 

} 

  

dafr2 = pd.DataFrame(data) 

print("\nSag Tarafta Olasılıksal Degerler:") 

print(dafr2) 
data = { 

    'Bolunme': [1, 2, 3, 4, 5, 6, 7, 8], 

    'PSol': [0.09, 0.45, 0.45, 0.18, 0.45, 0.36, 0.55, 0.45], 

    'PSag': [0.91, 0.55, 0.55, 0.82, 0.55, 0.64, 0.45, 0.55], 

    '2PSolPSag': [0.17, 0.5, 0.5, 0.3, 0.5, 0.46, 0.5, 0.5], 

    'ᶲ(B|d)': [0.13, 0.07, 0.07, 0.26, 0.07, 0.2, 0.66, 0.66] 

} 

  

dafr3 = pd.DataFrame(data) 

print(dafr3) 

  

max_uygunluk = dafr3['ᶲ(B|d)'].max() 

max_bolum = dafr3[dafr3['ᶲ(B|d)'] == max_uygunluk]['Bolunme'].values[0] 

  

print("\nEn yuksek uygunluk degerıne sahıp bolunme:", max_bolum) 

data = { 

    'Bölünme': [1, 2, 3, 4, 5, 6, 7, 8], 

    'Psol': [0.09, 0.45, 0.45, 0.18, 0.45, 0.36, 0.55, 0.45], 

    'Psağ': [0.91, 0.55, 0.55, 0.82, 0.55, 0.64, 0.45, 0.55], 

    '2PsolPsağ': [0.17, 0.5, 0.5, 0.3, 0.5, 0.46, 0.5, 0.5], 

    'ᶲ(B|d)': [0.13, 0.07, 0.07, 0.26, 0.07, 0.2, 0.66, 0.66] 

} 

  

dafr4 = pd.DataFrame(data) 

print(dafr4) 

  

max_uygunluk = dafr4['ᶲ(B|d)'].max() 

max_bolum = dafr4[dafr4['ᶲ(B|d)'] == max_uygunluk]['Bölünme'].values[0] 

  

print("\nEn yüksek uygunluk değerine sahip bölünme:", max_bolum) 

  

sol_oznitelik = dafr4[dafr4['Bölünme'] == max_bolum]['Psol'].values[0] 

sag_oznitelik = dafr4[dafr4['Bölünme'] == max_bolum]['Psağ'].values[0] 

  

print("Bölünme niteliği:") 

if sol_oznitelik > sag_oznitelik: 

    print("Sol nitelik: Psol") 

else: 

    print("Sol nitelik: PSağ") 