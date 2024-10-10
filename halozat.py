hálózat = []
with open('hálózat.txt', 'r', encoding='utf-8') as forras, \
     open('hálózat_adat.txt', 'w', encoding='utf-8') as cel:
    fejletc = forras.readline()
    
    for sor in forras:
        adat = sor.strip().split(',')
        
    for elem in hálózat:
        if len(adat) >= 5:
            haló = {
                'szerzo': adat[0],
                'cm': adat[1],
                'kiads': adat[2],
                'ISBN': adat[3],
                'alapot': adat[4],
            }
            hálózat.append(haló)
    
    
        print(elem, file=cel)
print(hálózat)
