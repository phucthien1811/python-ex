
with open('input.inp','r') as fileInp:
    ten = fileInp.readline().rstrip('\n')
    tuoiHienTai= int(fileInp.readline().rstrip('\n'))
    
with open('output.out','w') as fileOut:
    fileOut.write('Hai muoi nam nua , tuoi cua {} se la {}'.format(ten, tuoiHienTai + 20))

