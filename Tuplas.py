hierbas = {'cilantro', 'perejil', 'hierbabuena'}
especias = {'cilantro', 'perejil', 'pimienta'}
print(especias & hierbas)
print(especias | hierbas)
print(especias - hierbas)
print(hierbas - especias)
print(hierbas ^ especias)
hierbas.remove('cilantro')
print(hierbas)
