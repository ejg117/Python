with open('W11team\hr_system.txt') as file:
    for line in file:
            parts = line.split(" ")
            name = parts[0]
            id_number = parts[1].strip()
            job_title = parts[2]
            salary = float(parts[3].strip())
            print(line.strip())
            salary = salary / 24
            if job_title == 'Engineer':
                salary += 1000
                print(f'Name: {name} (ID: {id_number}), Title: {job_title} - ${salary: .2f}')