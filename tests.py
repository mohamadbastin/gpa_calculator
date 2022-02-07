import csv


def check_has_three_and_types(line):
    if len(line) != 3 and len(line) != 0:
        print(len(line))
        raise Exception(f'wrong length {line}')
    if len(line) > 0:
        if int(line[1]) not in [1, 2, 3]:
            raise Exception(f'wrong number of units in {line}')

        if line[2] not in ["A", "B", "C", "D", "F"]:
            raise Exception(f'wrong mark {line}')


def check_sum(lines, total_units):
    summa = 0
    for line in lines:
        if len(line) > 0:
            summa += int(line[1])
    if summa != int(total_units):
        raise Exception(f"sum of all units dont match the total. sum={summa}, total={total_units}")


file = open("gpa.csv")
csv_header = csv.reader(file)
# header = next(csv_header)
data = []
for row in csv_header:
    check_has_three_and_types(row)
    if len(row) > 0:
        data.append(row)
# file.close()
second_file = open("total.csv")
total = csv.reader(second_file)
total_number_of_units = int(next(total)[0])
check_sum(data, total_number_of_units)
file.close()
second_file.close()
##################
print("input is correct.\n")
sum_of_gpa = 0
As = []
Bs = []
Cs = []
Ds = []
Fs = []


def get_mark(mark_):
    if mark_ == "A":
        return 4
    elif mark_ == "B":
        return 3
    elif mark_ == "C":
        return 2
    elif mark_ == "D":
        return 1
    elif mark_ == "F":
        return 0


for row in data:
    units = int(row[1])
    mark = get_mark(row[2])

    sum_of_gpa += mark * units

    if mark == 0:
        Fs.append(row)
    elif mark == 1:
        Ds.append(row)
    elif mark == 2:
        Cs.append(row)
    elif mark == 3:
        Bs.append(row)
    elif mark == 4:
        As.append(row)

gpa = sum_of_gpa / total_number_of_units

print("total GPA: ", gpa)
print()
print(f"A's: {sum([int(i[1]) for i in As])}")
print([i[0] for i in As])
print()
print(f"B's: {sum([int(i[1]) for i in Bs])}")
print([i[0] for i in Bs])
print()
print(f"C's: {sum([int(i[1]) for i in Cs])}")
print([i[0] for i in Cs])
print()
print(f"D's: {sum([int(i[1]) for i in Ds])}")
print([i[0] for i in Ds])
print()
print(f"F's: {sum([int(i[1]) for i in Fs])}")
print([i[0] for i in Fs])
