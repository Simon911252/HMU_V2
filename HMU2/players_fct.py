from operator import add
import random
import uuid

def random_name(nationality):
    if nationality in ['Canada', 'United-States']:
        first_names = ['Lukas', 'Cristian','Valentin', 'Ronan', 'Brenton', 'Davon', 'Cohen',
                    'Rolando', 'Seamus', 'Roderick', 'Toby', 'Bernard', 'Grant', 'Ernest',
                    'Warren', 'Jaydon', 'Martin', 'Simon', 'Michael', 'Daniel', 'Chris',
                    'Hugh', 'Philippe', 'Frank', 'Richard', 'Wayne', 'Cyril', "John", "Carter",
                    "Hunter", "Joshua", "John", "William", "Matthew", "Christopher", "Liam", "Logan",
                    "Mason", "Ethan", "Alexis", "Jérémy", "Samuel", "Zachary", "Tristan", "Cameron", "Noah",
                    "Owen", "Ryan", "Cole", "Jack", "Sean", "Max", "Seth", "Kyle"]
        last_names = ['Price', 'Clements', 'Arroyo', 'Bautista', 'Long', 'Randall', 'Strickland',
                    'Edwards', 'Thomas', 'Maddox', 'Johnston', 'Park', 'Sanchez', 'Graham',
                    'Jarvis', 'Booker', 'Prince', 'Mccoy', 'Andrews', 'Walton', 'Forbes', 'Beltran',
                    'Marks', 'Chapman', 'Baldwin', 'Porter', 'Gregory', 'Arnold', 'Stark',
                    'Barnes', 'Cruz', 'Bradley', 'Dickerson', 'Keller', "Smith", "Brown", "Martin", "Lee",
                    "Wilson", "Roy", "Johnson", "Campbell", "Anderson", "Jones", "Leblanc", "Côté", "Williams",
                    "Miller", "White", "Morin", "Wong", "Young", "Lavoie", "Stewart", "Robinson", "Morre", "Chan"]
    elif nationality == 'Russia':
        first_names = ['Artemi', 'Alexi', "Alexander", "Vlad", "Vladmir", "Maxim", "Andrei",
                    "Nik", "Nikit", "Nikita", "Nikolay", "Pav", "Pavel", "Spartak", "Peter", "Pete", "Sergei",
                    "Yury", "Yak", "Yakov", "Spar", "Spartak", "Spartan", "Taras", "Tara", "Trof", "Trofim",
                    "Oz", "Osip", "Oleg", "Oli", "Olin", "Olan", "Olaf", "Artur", "Artemis", "Arty", "Abram"]
        last_names = ['Argemetov', "Putin", "Vasilevsky", "Larionov", "Kucherov", "Smirnoff", "Volkov", "Semenov",
                    "Lenkov", "Alexeev", "Alekhin", "Vasiliev", "Popov", "Kozlov", "Novikov", "Novikoff", "Turgenev",
                    "Barinov", "Gurkin", "Gurk", "Laskin", "Lask", "Levin", "Lev", "Levi", "Litvin", "Livi", "Litiv",
                    "Zaitsev", "Zait", "Sevi", "Sev", "Pasternak", "Pasten", "Nak", "Past", "Pask", "Paner",
                    "Preobrazhensky", "Golubev", "Golub", "Gev", "Golu", "Golev", "Sokolov"]
    elif nationality in ['Sweden', 'Norway', "Denmark"]:
        first_names = ['Soren', 'Bjorn', 'Boe', "Jesse", "Bjorson", "Luca", "Lucas", "Jan", "Ole", "Einar", "Gunnar",
                    "Anders", "Arvid", "Arvi", "Ander", "Andi", "Eirik", "Absjorn", "Alf", "Ali", "Alfi", "Vegard",
                    "Vegar", "Vega", "Vidar", "Svien", "Christoph", "Sindre", "Torb", "Toby", "Tor", "Ovyind",
                    "Ovystien", "Ovy", "Stien", "Sten", "Ovys", "Jorn", "Kristoff", "Dimitri"]
        last_names = ['Osness', 'Tolbjorn', "Torbjorn", "Hansen", "Sen", "Olsen", "Ols", "Lar", "Larsen", "John", "Joh",
                    "Johan", "Johansen", "Han", "Haj", "Karllson", "Sonn", "Kar", "Sson", "Nil", "Nilsson", "Nils",
                    "Karl", "Ander", "Anderson", "Ande", "Andi", "Derson", "Erson", "Jansson", "Jonsson", "Mag",
                    "Magon", "Magnu", "Magnusson", "Maug", "Nuss", "Lindber", "Len", "Lin", "Lind", "Linder",
                    "Linderberg", "Lini", "Lide", "Linde", "Lindstrom", "Anderson", "Derg", "Ber", "Berg", "Svensson",
                    "Kristoffson"]
    elif nationality in ['Germany', 'Switzerland']:
        first_names = ["Conrad", "Bruno", "Elias", "Gerfried", "Hans", "Julian", "Koloman", "Xerdan", "Josep",
                    "Pierrick", "Mezut", "Hansel", "Ernst", "Friedrich", "Hans", "Heinrich", "Hermann", "Karl",
                    "Otto", "Paul", "Walter", "Wilhelm", "Dieter", "Günter", "Horst", "Jürgen", "Klaus", "Manfred",
                    "Peter", "Uwe", "Wolfgang", "Finn", "Jan", "Jannik", "Jonas", "Leon", "Luca", "Lukas", "Niklas",
                    "Tim", "Tom", ]
        last_names = ['Merkel', 'Gertrudel', 'Ozen', "Hischyer", "Müller", "Fischer", "Klein", "Hermann", "Friedrich",
                    "Weber", "Schmidt", "Schneider", "Meyer", "Becker", "Bauer", "Wagner", "Wolf", "Schröder",
                    "Zimmerman", "Schmitz", "Meier", "Walter", "Colvert", "Kraus", "König", "Huber", "Fuchs",
                    "Stein", "Peters", "Roth", "Gunter", "Schubert", "Ludwig", "Otto"]
    elif nationality == 'France':
        first_names = ["Pierre", "Éric", "Jean-Pierre", "Pierrick", "Jean", "Philippe", "François", "Pierre-Édouard",
                    "Édouard", "Thomas", "Laurent", "Jules", "Julien", "Antoine", "Marc", "Martin", "Emmanuel"]
        last_names = ['Bellemare', "Gauthier", "Charland", "Labrecque", "Drouin", "Petitgros", "Marcdargent",
                    "Fontaine", "Belkaçim", "Angel", "Tremblay", "Bellefeuille", "D'Anjou", "Dirac", "Tadelle",
                    "Anthony", "Té", "Charon"]
    elif nationality in ['Czechia', 'Slovakia', 'Slovenia']:
        first_names = ["Anton", "Peter", "Matus", "Yan", "Novak", "Tomàs", "Adam", "Daniel", "Tobias", "Michal",
                    "Jachym", "Filip", "Petr", "Vaclav", "Radek", "Matej", "Marek", "Viktor", "Jaroslav",
                    "Frantisek", "Patrik", "Denis", "Josef", "Alexander", "Alex", "Krystof", "Jiri", "Yannick",
                    "Maxim", "Roman", "Jakub", "Lukas", "Zdeno", "Zdenek", "Tadeas", "Hugo", "Vito"]
        last_names = ["Novak", "Svoboda", "Novotny", "Stasny", "Svoboda", "Novotny", "Dvorak", "Cerny", "Kuchera",
                    "Veselka", "Horak", "Krejci", "Marek", "Pokorna", "Pospisil", "Hajek", "Benes", "Fialova",
                    "Zemanova", "Kral", "Zeman", "Dolezalova", "Sedlacek", "Dolezal", "Navratil", "Urban", "Cermak",
                    "Jelinek", "Nemec", "Kopecka", "Blazek", "Musil", "Kriz", "Vlcek", "Koneckny"]
    elif nationality == 'Finland':
        first_names = ["Antti", "Aaro", "Jami", "Jesse", "Samu", "Jaako", "Joona", "Aleksi", "Juho", "Miika", "Arttu",
                    "Juuso", "Leevi", "Elias", "Sami", "Joonatan", "Tuomas", "Mirko", "Simo", "Pekka", "Otto",
                    "Aino", "Mikael", "Timo", "Veikko"]
        last_names = ["Korhonen", "Virtanen", "Mäkinen", "Nieminen", "Mäkelä", "Hämäläinen", "Laine", "Heikkinen",
                    "Koskinen", "Järvinen", "Lehtonen", "Saarinen", "Salminen", "Heinonen", "Niemi", "Kinnunen",
                    "Salonen", "Turunen"]

    else:
        first_names = ['Simon']
        last_names = ['Gauthier']
    return f'{first_names[random.randint(0, len(first_names) - 1)]} {last_names[random.randint(0, len(last_names) - 1)]}'


def random_position():
    positions = ['LW', 'C', 'RW', 'LD', 'RD', 'LW', 'C', 'RW', 'LD', 'RD',
                 'LW', 'C', 'RW', 'LD', 'RD', 'LW', 'C', 'RW', 'G', 'G']
    return positions[random.randint(0, len(positions) - 1)]


def random_archetype(position):
    defensive_archetypes = ['Shutdown Defenceman', 'Two-way Defenceman', 'Offensive Defenceman']
    if position in ['RW', 'C', 'LW']:
        attacking_archetypes = ['Playmaker', 'Sniper', 'Net Front Presence', 'Two-Way Forward']
        return attacking_archetypes[random.randint(0, len(attacking_archetypes) - 1)]
    elif position in ['LD', 'RD']:
        return defensive_archetypes[random.randint(0, len(defensive_archetypes) - 1)]
    else:
        return None


def random_playing_styles(position):
    amount_defensive_styles = [1, 1, 1, 2, 2, 2, 2]
    defensive_playing_styles = ['Physical', 'Puck Moving', 'PowerPlay', 'Penalty Kill']
    if position in ['RW', 'C', 'LW']:
        return _extracted_from_random_playing_styles_2()
    elif position in ['LD', 'RD']:
        number = amount_defensive_styles[random.randint(0, len(amount_defensive_styles) - 1)]
        return _extracted_from_random_playing_styles_16(number, defensive_playing_styles)

    else:
        return []


# TODO Rename this here and in `random_playing_styles`
def _extracted_from_random_playing_styles_16(number, arg1):
    defensive_style = []
    for _ in range(number):
        defensive_style += defensive_style + [arg1[random.randint(0, len(arg1) - 1)]]
    return list(dict.fromkeys(defensive_style))


# TODO Rename this here and in `random_playing_styles`
def _extracted_from_random_playing_styles_2():
    amount_attacking_styles = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3]
    number = amount_attacking_styles[random.randint(0, len(amount_attacking_styles) - 1)]
    attacking_playing_styles = ['Grinder', 'Pure Skill', 'Defensive Minded', 'Counterattack',
                                'Physical', 'PowerPlay', 'Penalty Kill']
    return _extracted_from_random_playing_styles_16(number, attacking_playing_styles)


def random_skills(position):
    skills = []
    for i in range(20):
        skills += [random.randint(15, 110)]
    if position == 'RW' or position == 'LW':
        skills[2] = skills[2] + 15  # skating
        skills[5] = skills[5] + 10  # agility
        skills[6] = random.randint(5, 75)  # shot blocking
        skills[7] = random.randint(5, 75)  # def stickwork
        skills[10] = random.randint(15, 75)  # faceoffs
        skills[13] = skills[13] + 10  # creativity
        skills[15] = skills[15] + 20  # stick handling
        skills[16] = skills[16] + 10  # wrist shot
    if position == 'C':
        skills[4] = skills[4] + 10  # workrate
        skills[9] = skills[9] + 20  # def positioning
        skills[10] = skills[10] + 25  # faceoffs
        skills[11] = skills[11] + 10  # IQ
        skills[14] = skills[14] + 10  # passing
    if position == 'LD' or position == 'RD':
        skills[0] = skills[0] + 10  # strength
        skills[6] = skills[6] + 20  # shot blocking
        skills[7] = skills[7] + 15  # stick work
        skills[8] = skills[8] + 20  # gap control
        skills[9] = skills[9] + 5  # def positioning
        skills[10] = random.randint(15, 45)  # faceoffs
        skills[18] = random.randint(45, 90)  # slap shots
        skills[19] = random.randint(15, 65)  # deflections
    if position == 'G':
        skills = []
        for i in range(11):
            skills += [random.randint(15, 110)]
        skills[1] = random.randint(45, 90)
        if skills[3] < 45:
            skills[5] = random.randint(45, 120)
        if skills[5] < 45:
            skills[3] = random.randint(45, 120)
    return skills


def calculate_REC(position, skills, REC=0, off_or_def=None):
    winger_REC_coefficients = [0.4, 0.3, 0.6, 0.2, 0.4, 0.6, 0.1, 0.2, 0.2, 0.3,
                               0.1, 0.5, 0.4, 0.6, 0.6, 0.7, 0.7, 0.2, 0.3, 0.6]
    center_REC_coefficients = [0.4, 0.5, 0.4, 0.4, 0.6, 0.3, 0.3, 0.4, 0.2, 0.5,
                               0.5, 0.7, 0.3, 0.5, 0.6, 0.4, 0.5, 0.2, 0.3, 0.5]  # total 8.5
    defenceman_REC_coefficients = [0.5, 0.4, 0.6, 0.6, 0.3, 0.3, 0.6, 0.7, 0.7, 0.7,
                                   0.0, 0.4, 0.5, 0.2, 0.2, 0.3, 0.1, 0.5, 0.1, 0.3]
    goalie_REC_coefficients = [0.3, 0.1, 0.6, 0.8, 0.6, 0.8, 0.3, 0.6, 0.4, 0.4, 0.1]
    if off_or_def == 'off':
        winger_REC_coefficients = [0.4, 0.1, 0.6, 0.1, 0.2, 0.6, 0.0, 0.0, 0.0, 0.0,
                                   0.0, 0.5, 0.4, 0.6, 0.8, 1.0, 1.0, 0.4, 0.5, 0.8]
        center_REC_coefficients = [0.4, 0.1, 0.4, 0.1, 0.5, 0.3, 0.0, 0.0, 0.0, 0.0,
                                   0.4, 0.7, 0.4, 0.7, 1.0, 0.8, 0.8, 0.4, 0.7, 0.8]  # total 8.5
        defenceman_REC_coefficients = [0.4, 0.3, 0.9, 0.1, 0.1, 0.5, 0.0, 0.0, 0.0, 0.0,
                                       0.0, 0.7, 0.2, 0.8, 1.2, 0.5, 0.4, 0.8, 0.1, 1.0]
    if off_or_def == 'def':
        winger_REC_coefficients = [0.8, 0.3, 0.7, 0.9, 0.3, 0.2, 0.5, 0.9, 0.5, 1.6,
                                   0.3, 0.6, 0.3, 0.0, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0]
        center_REC_coefficients = [0.7, 0.5, 0.6, 0.8, 0.8, 0.2, 1.0, 0.6, 0.5, 1.6,
                                   0.6, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]  # total 8.5
        defenceman_REC_coefficients = [0.7, 0.1, 0.2, 1.2, 0.3, 0.2, 1.3, 1.4, 1.4, 1.0,
                                       0.0, 0.2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    if position == 'RW' or position == 'LW':
        for i in range(20):
            REC += skills[i] * winger_REC_coefficients[i]
    if position == 'C':
        for i in range(20):
            REC += skills[i] * center_REC_coefficients[i]
        REC = REC * 0.94117  # coefficient d'ajustement
    if position == 'RD' or position == 'LD':
        for i in range(20):
            REC += skills[i] * defenceman_REC_coefficients[i]
    if position == 'G':
        for i in range(11):
            REC += skills[i] * goalie_REC_coefficients[i] * 1.6  # le 1.6 est ajustement entre 'G' et le reste
    REC = (REC - 187.33) / 114.33
    if REC < 0.01:
        REC = 0.01
    return round(REC, 2)


def calculate_offensive_REC(skills, REC):
    total_skills = sum(skills)
    off_skills = sum(skills[12:]) + sum(skills[0:3])*0.5 + skills[4]*0.5 + skills[5]*0.5 + skills[10]*0.5 + skills[11]*0.5
    return REC * (off_skills / total_skills)


def calculate_defensive_REC(skills, REC):
    total_skills = sum(skills)
    def_skills = sum(skills[6:11]) + skills[3] + sum(skills[0:3])*0.5 + skills[4]*0.5 + skills[5]*0.5 + skills[10]*0.5 + skills[11]*0.5
    return REC * (def_skills / total_skills)


def random_skill_peaks(position, player_potential):  # [physical, defensive, mental, offensive]
    # [physical, mental, control] for goalies
    skill_peaks = []
    skill_peaks += [random.randint(1, 6)]  # physical
    skill_peaks += [random.randint(1, 4)]  # defensive
    skill_peaks += [random.randint(1, 4)]  # mental
    skill_peaks += [random.randint(1, 6)]  # offensive
    winger_bonus = [1, 0, 0, 2]
    center_bonus = [1, 0, 1, 1]
    dman_bonus = [1, 2, 0, 0]
    if player_potential > 5 and position == 'RW' or player_potential > 5 and position == 'LW':
        skill_peaks = list(map(add, skill_peaks, winger_bonus))
    if player_potential > 5 and position == 'C':
        skill_peaks = list(map(add, skill_peaks, center_bonus))
    if player_potential > 5 and position == 'RD' or player_potential > 5 and position == 'LD':
        skill_peaks = list(map(add, skill_peaks, dman_bonus))
    for i in range(4):
        if i == 0 or i == 3:
            if skill_peaks[i] > 6:
                skill_peaks[i] = 6
        if i == 1 or i == 2:
            if skill_peaks[i] > 4:
                skill_peaks[i] = 4
    if position == 'G':
        skill_peaks = []
        skill_peaks += [random.randint(1, 3)]  # physical
        skill_peaks += [random.randint(1, 4)]  # mental
        skill_peaks += [random.randint(1, 4)]  # control
        if player_potential > 5:
            skill_peaks = list(map(add, skill_peaks, [0, 1, 1]))
        if skill_peaks[1] > 4:
            skill_peaks[1] = 4
        if skill_peaks[2] > 4:
            skill_peaks[2] = 4
    return skill_peaks


def random_nationality():
    list_of_countries = ['Canada'] * 7 + ['United-States'] * 6 + ['Russia', 'Sweden'] * 4 + \
                        ['Czechia', 'Slovakia', 'Finland'] * 2 + ['Switzerland', 'Slovenia', 'Denmark',
                                                                  'Germany', 'Norway', 'France']
    nationality = list_of_countries[random.randint(0, len(list_of_countries) - 1)]
    return nationality


def random_size(position):
    feet = ['5'] * 4 + ['6'] * 7
    feet = feet[random.randint(0, len(feet) - 1)]
    inches = ['00'] * 3 + ['01'] * 6 + ['02'] * 5 + ['03'] * 5 + ['04'] * 2 + ['05'] * 1 + ['06'] * 1
    if feet == '5':
        inches = ['11'] * 11 + ['10'] * 8 + ['09'] * 3 + ['08'] * 2 + ['07'] * 1 + ['06'] * 1
    inches = inches[random.randint(0, len(inches) - 1)]
    if position == 'RW' or position == 'LW':
        inches = str(int(inches) - 1)
    if position == 'RD' or position == 'LD':
        inches = str(int(inches) + 1)
    if position == 'G':
        inches = str(int(inches) + 2)
    if int(inches) == -1:
        feet = str(int(feet) - 1)
        inches = '11'
    if int(inches) == 12:
        feet = str(int(feet) + 1)
        inches = '00'
    if int(inches) == 13:
        feet = str(int(feet) + 1)
        inches = '01'
    return f"{feet}'{inches}"


def random_weight(size):  # in pounds, at 2.739 pounds/inch
    number = 0
    if len(size) == 3:
        number = int(size[0]) * 12 + int(size[2])
    if len(size) == 4:
        number = int(size[0]) * 12 + int(size[2:4])
    weight = number * 2.739 + random.randint(-20, 20)
    return round(weight)


def random_routine(years):
    return round(15 + (years - 18) * 3.1) + 0.1*random.randint(-20,20)


def calculate_REC_routine(REC, routine):
    coefficient = 1 + routine / 650
    REC_routine = REC * coefficient
    return round(REC_routine, 2)


def random_bloom(years):
    bloomer_type = [17, 17, 17, 18, 18, 19, 19, 17, 17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22]  # early, normal or late
    bloomer_type = bloomer_type[random.randint(0, len(bloomer_type) - 1)]
    stage_of_bloom = years - bloomer_type
    if stage_of_bloom < 0:
        stage_of_bloom = 'Not bloomed'
        if bloomer_type == 17:
            stage_of_bloom += ' - early bloomer'
        if bloomer_type == 18 or bloomer_type == 19:
            stage_of_bloom += ' - normal bloomer'
        if bloomer_type == 20 or bloomer_type == 21 or bloomer_type == 22:
            stage_of_bloom += ' - late bloomer'
    elif stage_of_bloom == 1:
        stage_of_bloom = 'Starting to bloom'
    elif stage_of_bloom == 2:
        stage_of_bloom = 'In the middle of his bloom'
    elif stage_of_bloom == 3:
        stage_of_bloom = 'In his late bloom'
    else:
        stage_of_bloom = 'Bloomed'
    return stage_of_bloom