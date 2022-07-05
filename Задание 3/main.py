from pprint import pprint
file_1 = "1.txt"
file_2 = "2.txt"
file_3 = "3.txt"

def line_count(file):
    with open(file, 'r', encoding='utf-8') as counting_file:
        count=0
        for line in counting_file:
            count +=1
        return count

list_file = [file_1, file_2, file_3]
list_file.sort(key=line_count)
fin_file = []

for save_file in list_file:
    with open(save_file, 'r', encoding='utf-8') as counting_file:
        fin_file.append(save_file)
        fin_file.append(line_count(save_file))
        fin_file.append(counting_file.read())


for line in fin_file:
    line = str(line )
    with open ( "fin_file.txt", 'a', encoding='utf-8') as document:
        document.write(f'{line}\n')
