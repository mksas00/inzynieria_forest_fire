import csv


class Csv_writer:
    iterator: int = 0

    def __init__(self):
        self.file = open('simulation_data.csv', 'w', encoding='utf-8', newline='')
        self.file2 = open('simulation_indiduality_1.csv', 'w', encoding='utf-8', newline='')
        self.indiv_1_data = list()
        for x in range(800):
            self.indiv_1_data.append([['Sektor'], ['Temperatura'], ['Wigotoność powietrza'], ['Wilgotoność Ściółki'],
                                      ['Prędkość Waitru']])

    def write_to_file(self, secotrs_data):

        fieldnames = ['i', 'j', 'forest_type', 'is_fire_source', 'temperature', 'air_humidity', 'litter_moisture',
                      'wind_speed', 'wind_directory', 'CO2', 'pm25', 'sector_state', 'ffdi', 'on_fire']
        csvwriter = csv.writer(self.file)

        row_list = list()

        if Csv_writer.iterator == 0:
            csvwriter.writerow(fieldnames)
            # csvwriter.writerow(['Iteracja numer:', str(Csv_writer.iterator)])
        else:
            for key, values in secotrs_data.items():
                for key2, values2 in values.items():
                    row_list.append(str(values[key2]))

                csvwriter.writerow(row_list)
                row_list.clear()

        if Csv_writer.iterator > 0:
            csvwriter.writerow([''])
            csvwriter.writerow([''])

        Csv_writer.iterator += 1

    def wrtie_indiv_1(self,sectors_data):
        i = 0
        for key, values in sectors_data.items():
            # print("XDDDDDDDDDDDDDDDDD")
            # print(values['temperature'])
            self.indiv_1_data[i][1].append(values['temperature'])
            self.indiv_1_data[i][2].append(values['air_humidity'])
            self.indiv_1_data[i][3].append(values['litter_moisture'])
            self.indiv_1_data[i][4].append(values['wind_speed'])
            i += 1

    def save_to_file(self):

        # xd = [
        #     [[1, 2], [1, 2], []],
        #     [[3, 4], [3, 4], []]
        # ]

        csvwriter = csv.writer(self.file2)
        for x in self.indiv_1_data:
            csvwriter.writerows(x)


    def close_file(self):
        self.file.close()
        self.file2.close()
        print("Liczba iteracji: " + str(Csv_writer.iterator))
        Csv_writer.iterator = 0

