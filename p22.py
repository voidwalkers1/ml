import csv
def loadcsv(filename):
    lines = csv.reader(open(filename, "rt"))
    dataset = list(lines)
    return dataset
def learn():
    datasets=loadcsv("2.csv")
    print(datasets)
    specific_h = ['sunny','warm','normal','strong','warm','same']
    print("initialization of specific_h and general_h")
    print(specific_h)
    general_h = [["?" for i in range(len(specific_h))] for i in range(len(specific_h))]
    print(general_h)
    for i in range(len(datasets)):
        if datasets[i][-1] == "Y":
            for x in range(len(specific_h)):
                if datasets[i][x] != specific_h[x]:
                    specific_h[x] = '?'
                    general_h[x][x] = '?'

        if datasets[i][-1] == "N":
            for x in range(len(specific_h)):
                if datasets[i][x] != specific_h[x]:
                    general_h[x][x] = specific_h[x]
                else:
                    general_h[x][x] = '?'
        print(" steps of Candidate Elimination Algorithm",i+1)
        print(specific_h)
        print(general_h)
    indices = [i for i, val in enumerate(general_h) if val == ['?', '?', '?', '?', '?', '?']]
    for i in indices:
        general_h.remove(['?', '?', '?', '?', '?', '?'])
    return specific_h, general_h
s_final, g_final = learn()
print("Final Specific_h:", s_final, sep="\n")
print("Final General_h:", g_final, sep="\n")
