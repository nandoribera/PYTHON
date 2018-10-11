beb_frias = {'tonica', 'trina', 'cerveza'}
beb_calientes = {'te', 'cafe', 'colacao'}
beb_alcohol = {'cerveza', 'vino', 'ron'}
beb = beb_frias | beb_calientes
print(beb)
beb_frias_alcohol = beb_frias & beb_alcohol
print(beb_frias_alcohol)
beb_frias_alcohol = beb_frias ^ beb_alcohol
print(beb_frias_alcohol)