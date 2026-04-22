f = open('test.txt', 'w')
for i in range(1, 6):
    data = f'Line {i}\n'
    f.write(data)
f.close()
print('Da ghi 5 dong vao test.txt')
