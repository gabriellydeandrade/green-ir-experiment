import csv

import toml


def kwatts(duration_hours: float, watt: float):
    conversion = (watt / 1000)
    return conversion / duration_hours #‘the energy consumed at a rate of one kilowatt for one hour’.


def hours(duration_seconds: float):
    return duration_seconds / 3600


def calculate_watts():
    data = {}
    with open("emissions.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            experiment = row[1]
            duration_seconds = float(row[3])
            duration_hours = hours(duration_seconds)

            emissions = float(row[4])

            cpu_power = float(row[6])
            gpu_power = float(row[7])
            ram_power = float(row[8])
            power = cpu_power + gpu_power + ram_power

            data[experiment] = {"name": experiment, "carbon_emission": emissions/duration_hours} 
    export = {"experiment": []}
    for k, v in data.items():
        export["experiment"].append(v)
    print(toml.dumps(export))


if __name__ == '__main__':
    calculate_watts()
