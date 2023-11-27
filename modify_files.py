def write_file(path, text):
    try:
        with open(path, 'a') as file:
            file.write(text + '\n')
    except Exception as e:
        print('Ocurrio un error')

def get_max(path):
    try:
        with open(path, 'r') as file:
            lines = file.readlines()
            numbers = [int(num) for line in lines for num in line.split()]
            record_number = max(numbers)
            return record_number
    except FileNotFoundError:
        print(f'File not found')
    except Exception as e:
        print('Ocurrio un error')