import csv


def Constants():
    ss_values = []

    with open('Proses_Constants.csv', 'r') as csvfile:
        ss = csv.reader(csvfile, delimiter=',')

        for row in ss:
            ss_values.append(float(row[1]))

    return ss_values
