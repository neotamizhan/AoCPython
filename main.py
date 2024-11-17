import importlib


def import_process_function(year, day_number):
    # Format the module name based on the day number
    module_name = f'AoC{year}.Day{day_number}.Run'

    # Dynamically import the module
    module = importlib.import_module(module_name)

    # Retrieve the 'process' function from the module
    process_function = module.process

    return process_function
  
day_number = '02'  # Replace with the desired day number
process = import_process_function('2015', day_number)
process(day_number)

#if __name__ == "__main__":
#  process()
