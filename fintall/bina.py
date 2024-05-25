def caracterbinario(car):
    bites = format(ord(car), '08b')
    return bites
def palabra_binario(palabra):
    bites = ' '.join(format(ord(car), '08b') for car in palabra)
    return bites
def binario_palabra(byte):
   ascii = chr(int(byte, 2))
   return ascii 