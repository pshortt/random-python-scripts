f1 = open('SurrondingNodes bladefem.txt', 'r')
f2 = open('SurrondingNodes bladefem_Java_List_Ready.txt', 'w')

for line in f1:
    f2.write('l.add(' + line[:-1] + ');\n')

f1.close()
f2.close()
