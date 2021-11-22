import csv


class Csv_writer:
    iterator = 0

    def __init__(self):
        self.file = open('simulation_data.csv', 'w', encoding='utf-8', newline='')
        self.file2 = open('simulation_individuality_1.csv', 'w', encoding='utf-8', newline='')
        self.file3 = open('simulation_individuality_1.csv', 'w', encoding='utf-8', newline='')
        self.indiv_1_data = list()
        self.indiv_2_data = list()
        for x in range(800):
            self.indiv_1_data.append([[], [], [], [], []])
            self.indiv_2_data.append([[], [], [], []])

    # def write_to_file(self, secotrs_data):
    #
    #     fieldnames = ['i', 'j', 'forest_type', 'is_fire_source', 'temperature', 'air_humidity', 'litter_moisture',
    #                   'wind_speed', 'wind_directory', 'CO2', 'pm25', 'sector_state', 'ffdi', 'on_fire']
    #     csvwriter = csv.writer(self.file)
    #
    #     row_list = list()
    #
    #     if Csv_writer.iterator == 0:
    #         csvwriter.writerow(fieldnames)
    #         # csvwriter.writerow(['Iteracja numer:', str(Csv_writer.iterator)])
    #     else:
    #         for key, values in secotrs_data.items():
    #             for key2, values2 in values.items():
    #                 row_list.append(str(values[key2]))
    #
    #             csvwriter.writerow(row_list)
    #             row_list.clear()
    #
    #     if Csv_writer.iterator > 0:
    #         csvwriter.writerow([''])
    #         csvwriter.writerow([''])
    #
    #     Csv_writer.iterator += 1

    def wrtie_indiv_1(self, sectors_data):
        i = 0

        for key, values in sectors_data.items():
            if Csv_writer.iterator == 0:
                self.indiv_1_data[i][0].append('Sektor: ' + str(key))
                self.indiv_1_data[i][1].append('Temperatura')
                self.indiv_1_data[i][2].append('Wilgotność powietrza')
                self.indiv_1_data[i][3].append('Wilgotność Ściółki')
                self.indiv_1_data[i][4].append('Prędkość Wiatru')

            self.indiv_1_data[i][1].append(values['temperature'])
            self.indiv_1_data[i][2].append(values['air_humidity'])
            self.indiv_1_data[i][3].append(values['litter_moisture'])
            self.indiv_1_data[i][4].append(values['wind_speed'])
            i += 1

    def wrtie_indiv_2(self, sectors_data):
        i = 0
        for key, values in sectors_data.items():
            if Csv_writer.iterator == 0:
                self.indiv_2_data[i][0].append('Sektor: ' + str(key))
                self.indiv_2_data[i][1].append('Prędkość Wiatru')
                self.indiv_2_data[i][2].append('Stężenie CO2')
                self.indiv_2_data[i][3].append('Stężenie PM2.5')

            self.indiv_2_data[i][1].append(values['wind_speed'])
            self.indiv_2_data[i][2].append(values['co2'])
            self.indiv_2_data[i][3].append(values['pm25'])
            i += 1

    def save_to_file(self):

        csvwriter = csv.writer(self.file2)
        csvwriter_2 = csv.writer(self.file3)
        header = list()
        header.append('Nr iteracji')

        for i in range(Csv_writer.iterator):
            header.append(i+1)
        csvwriter.writerow(header)
        csvwriter_2.writerow(header)

        for x in self.indiv_1_data:
            csvwriter.writerows(x)


        for x in self.indiv_2_data:
            csvwriter_2.writerows(x)

    def close_file(self):
        self.file.close()
        self.file2.close()
        print("Liczba iteracji: " + str(Csv_writer.iterator))
        Csv_writer.iterator = 0
