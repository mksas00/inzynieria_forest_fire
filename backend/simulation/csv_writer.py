import csv


class Csv_writer:
    iterator: int = 0

    def __init__(self):
        self.file = open('simulation_data.csv', 'w', encoding='utf-8', newline='')

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

        if Csv_writer.iterator>0:
            csvwriter.writerow([''])
            csvwriter.writerow([''])

        Csv_writer.iterator += 1

    def close_file(self):
        self.file.close()
        print("Liczba iteracji: " + str(Csv_writer.iterator))
        Csv_writer.iterator = 0
