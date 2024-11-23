import importlib


def import_process_function(year, day_number):
    # Format the module name based on the day number
    module_name = f'AoC{year}.day{day_number}.Run'

    # Dynamically import the module
    module = importlib.import_module(module_name)

    # Retrieve the 'process' function from the module
    process_function = module.process

    return process_function

year = '2015'
day = 7 #Replace with the desired day number
process = import_process_function(year, day)
process(day)

#if __name__ == "__main__":
#  process()
