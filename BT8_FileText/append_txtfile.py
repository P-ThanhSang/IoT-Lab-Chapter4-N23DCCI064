f = open('test.txt', 'a')  # Che do append
for i in range(6, 11):
    data = f'Added Line {i}!\n'
    f.write(data)
f.close()
print('Da ghep them 5 dong.')
