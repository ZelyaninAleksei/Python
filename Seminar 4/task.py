import fileinput

with open('wp.txt') as f:
    text = f.read().lower().strip().replace('.', '').replace(',', '').replace(':', '').replace(';', '').replace('?', '').replace('!', '').split()

print(len(text))