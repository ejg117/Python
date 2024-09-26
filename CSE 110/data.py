import time
year_choice = input('Enter the year of interest:')
year_choice = int(year_choice)
with open('life-expectancy.csv') as lifeexpec:
        header = next(lifeexpec)
        overall_max_lifex = float('-inf')
        overall_min_lifex = float('inf')
        max_country= ""
        min_country= ""
        max_year= ""
        min_year= ""
        total=0
        count=0
        for line in lifeexpec:
            Lnlst = line.strip().split(",")
            Country = Lnlst[0]
            Year = int(Lnlst[2])
            lifex = float(Lnlst[3])
            if lifex > overall_max_lifex:
                overall_max_lifex = lifex
                max_country = Country
                max_year = Year
            if lifex < overall_min_lifex:
                overall_min_lifex = lifex
                min_country = Country
                min_year = Year

        lifeexpec.seek(0)
        next(lifeexpec)
        ymaxle = float('-inf')
        yminle = float('inf')
        ymaxc = ''
        yminc = ''

        total_year = 0
        count_year = 0

        for line in lifeexpec:
            Lnlst =line.strip().split(",")
            Country = Lnlst[0]
            Year = int(Lnlst[2])
            lifex = float(Lnlst[3])
            if Year == year_choice:
                year_found = True
                total_year += lifex
                count_year += 1
                if lifex > ymaxle:
                     ymaxle = lifex
                     ymaxc = Country
                if lifex < yminle:
                    yminle = lifex
                    yminc = Country

        avg_lifex_year = total_year / count_year if count_year != 0 else 0

        print(f'The overall max life expectancy is: {overall_max_lifex} from {max_country} in {max_year}')
        print(f'The overall min life expectancy is: {overall_min_lifex} from {min_country} in {min_year}')
if year_found:
        print('')
        print(f'For the year {year_choice}:')
        print(f'The average life expectancy across all countries was{avg_lifex_year: .2f}')
        print(f'The max life expectancy was in {ymaxc} with {ymaxle}')
        print(f'The min life expectancy was in {yminc} with {yminle}')
else:
        print('The year you put does not exist in the data set')
ask=input('Would you like to see the data set? ')
if ask == 'yes':
    with open('life-expectancy.csv') as lifeexpec:
        interval = .01
        while True:
            print("\033[5;33;40m\n")
            for line in lifeexpec:
                print(line.strip())
                time.sleep(interval)
else:
    print("\033[5;31;40m\n")
    print('')
    print('If not yes then I guess this is goodbye')