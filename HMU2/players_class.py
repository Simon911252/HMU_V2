from operator import add
import random
import uuid
import players_fct


class Player():
    def __init__(self, name='random', player_id='random', club_id='NA', position='random',
                archetype='random', playing_styles='random', skills='random',
                injury_proneness='random', years='random', months='random', player_potential='random',
                skill_peaks='random', work_ethic='random', nationality='random',
                size='random', weight=None, shoots='random', routine='random', discipline='random',
                bloom='random', TI_history=None, leadership='random', scout_report='random'):
        self.name = name
        self.player_id = player_id
        self.club_id = club_id
        self.position = position
        self.archetype = archetype
        self.playing_styles = playing_styles
        self.skills = skills
        self.injury_proneness = injury_proneness
        self.years = years
        self.months = months
        self.player_potential = player_potential
        self.skill_peaks =skill_peaks
        self.work_ethic = work_ethic
        self.nationality = nationality
        self.size = size
        self.weight = weight
        self.shoots = shoots
        self.routine = routine
        self.discipline = discipline
        self.bloom = bloom
        self.TI_history = TI_history
        self.leadership = leadership
        self.scout_report = scout_report

        if self.TI_history is None:
            self.TI_history = []
        if self.nationality == 'random':
            self.nationality = players_fct.random_nationality()
        if self.name == 'random':
            self.name = players_fct.random_name(self.nationality)
        if self.years == 'random':
            self.years = random.randint(17, 38)
        if self.months == 'random':
            months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
            self.months = months[random.randint(0, len(months) - 1)]
        if self.player_id == 'random':
            self.player_id = uuid.uuid1()
        if self.position == 'random':
            self.position = players_fct.random_position()
        if self.archetype == 'random':
            self.archetype = players_fct.random_archetype(self.position)
        if self.playing_styles == 'random':
            self.playing_styles = players_fct.random_playing_styles(self.position)
        if self.skills == 'random':
            self.skills = players_fct.random_skills(self.position)
        if self.routine == 'random':
            self.routine = players_fct.random_routine(self.years)
        self.REC = players_fct.calculate_REC(self.position, self.skills)
        if self.position != 'G':
            self.off_REC = players_fct.calculate_offensive_REC(self.skills, self.REC)
            self.def_REC = players_fct.calculate_defensive_REC(self.skills, self.REC)
            self.REC_routine = players_fct.calculate_REC_routine(self.REC, self.routine)
        if self.position != 'G':
            self.off_REC_routine = players_fct.calculate_REC_routine(self.off_REC, self.routine)
            self.def_REC_routine = players_fct.calculate_REC_routine(self.def_REC, self.routine)
        if self.injury_proneness == 'random':  # out of /10
            self.injury_proneness = (random.randint(1, 10))
        if self.player_potential == 'random':  # measured out of /10
            self.player_potential = random.randint(1, 10)
        if self.skill_peaks == 'random':
            self.skill_peaks = players_fct.random_skill_peaks(self.position, self.player_potential)
        if self.work_ethic == 'random':
            self.work_ethic = random.randint(1, 10)  # measured out of /10
        if self.size == 'random':
            self.size = players_fct.random_size(self.position)
        if self.weight is None:
            self.weight = players_fct.random_weight(self.size)
        if self.shoots == 'random':
            options = ["Left", "Right"]
            self.shoots = options[random.randint(0, 1)]
        if self.discipline == 'random':
            self.discipline = random.randint(1, 10)  # measured out of /10
        if self.bloom == 'random':
            self.bloom = players_fct.random_bloom(self.years)
        if self.leadership == 'random':
            self.leadership = random.randint(1, 10)
        #if self.scout_report == 'random':
            #self.scout_report = ScoutReports.create_scout_report(dictionary_of_player)
        
    def __str__(self):
        centering_spaces_1 = 13 - round(len(self.name)/2)
        centering_spaces_1 = ' '*centering_spaces_1
        centering_spaces_2 = 17 - round(len(self.nationality)/2)
        centering_spaces_2 = ' '*centering_spaces_2
        player_rec = str(self.REC)
        stars, halfs, number = int(player_rec[0]), int(player_rec[2]), 0
        halfs = 0 if halfs < 5 else 5
        REC = f'{stars}.{halfs}*'
        skill = self.skills
        skills = list(skill)
        for i in range(len(skills)):
            skills[i] = round(skills[i])
        if len(str(skills[1])) in {3, 2}:
            for i in range(len(skills)):
                skills[i] = f'  {str(skills[i])}  '
                if len(skills[i]) == 7:
                    skills[i] = skills[i][:6]
                if len(skills[i]) == 5:
                    skills[i] = f'{skills[i]} '
        start, end = [], ['\033[0m\033[0m']*20
        for i in skills:
            if int(i) >= 100:
                start += ['\033[102m\033[30m']
            elif 75 <= int(i) < 100:
                start += ['\033[106m\033[30m']
            elif 50 <= int(i) < 75:
                start += ['\033[103m\033[30m']
            elif 24 < int(i) < 50:
                start += ['\033[105m\033[30m']
            else:
                start += ['\033[101m\033[30m']
        last_5_TI = ''.join(f'{str(i)}, ' for i in self.TI_history[-5:])
        last_5_TI = last_5_TI[:-2]
        if self.position == 'G':
            return f"""
                {centering_spaces_1}\033[1m   {self.name}\033[0m ({self.position})
                    {REC}
                {centering_spaces_2}{self.nationality}
                    _________________
                    |                 |       Speed   |{start[0]}{skills[0]}{end[0]}| Reflexes         |{start[3]}{skills[3]}{end[3]}|
                    |                 |       Stamina |{start[1]}{skills[1]}{end[1]}| One v One        |{start[4]}{skills[4]}{end[4]}|
                    |      \  /       |       Agility |{start[2]}{skills[2]}{end[2]}| Glove            |{start[5]}{skills[5]}{end[5]}|
                    |      |  |       |                      | Stick            |{start[6]}{skills[6]}{end[6]}|
                    |      _____      |                      | Pads             |{start[7]}{skills[7]}{end[7]}|
                    |     /     \     |                      | Angles           |{start[8]}{skills[8]}{end[8]}|
                    |                 |                      | Rebound Control  |{start[9]}{skills[9]}{end[9]}|
                    |                 |                      | Puck Handling    |{start[10]}{skills[10]}{end[10]}|
                    |                 |                                             
                    |_________________|                                             
                    Player ID = {str(self.player_id)[:8]}
                    Routine = {self.routine}

                    Age = {self.years}.{self.months}
                    Size = {self.size}
                    Weight = {self.weight} lbs
                    Catches = {self.shoots}
                    Last 5 TIs = {last_5_TI}
                    """

        else:
            style = 'Playing Styles:' if len(self.playing_styles) > 1 else 'Playing Style:'
            playing_styles = ''.join(f'{i}, ' for i in self.playing_styles)
            playing_styles = playing_styles[:len(playing_styles) - 2]
            return f"""
                {centering_spaces_1}\033[1m   {self.name}\033[0m ({self.position})
                            {REC}
                {centering_spaces_2}{self.nationality}
                        _________________
                        |                 |       Strength         |{start[0]}{skills[0]}{end[0]}| Faceoffs         |{start[10]}{skills[10]}{end[10]}|
                        |                 |       Stamina          |{start[1]}{skills[1]}{end[1]}| Hockey IQ        |{start[11]}{skills[11]}{end[11]}|
                        |                 |       Skating          |{start[2]}{skills[2]}{end[2]}| Hand-eye         |{start[12]}{skills[12]}{end[12]}|
                        |       |   |     |       Physicality      |{start[3]}{skills[3]}{end[3]}| Creativity       |{start[13]}{skills[13]}{end[13]}|
                        |    \________/   |       Workrate         |{start[4]}{skills[4]}{end[4]}| Passing          |{start[14]}{skills[14]}{end[14]}|
                        |                 |       Agility          |{start[5]}{skills[5]}{end[5]}| Stick Handling   |{start[15]}{skills[15]}{end[15]}|
                        |                 |       Shot Blocking    |{start[6]}{skills[6]}{end[6]}| Wrist Shot       |{start[16]}{skills[16]}{end[16]}|
                        |                 |       Def. Stickwork   |{start[7]}{skills[7]}{end[7]}| Slap Shot        |{start[17]}{skills[17]}{end[17]}|
                        |                 |       Gap Control      |{start[8]}{skills[8]}{end[8]}| Deflections      |{start[18]}{skills[18]}{end[18]}|
                        |_________________|       Def. Positioning |{start[9]}{skills[9]}{end[9]}| Off. Positioning |{start[19]}{skills[19]}{end[19]}|
                        Player ID = {str(self.player_id)[:8]}
                        Routine = {self.routine}

                        Player Archetype : {self.archetype}
                        {style} : {playing_styles}
                        Age = {self.years}.{self.months}
                        Size = {self.size}
                        Weight = {self.weight} lbs
                        Shoots = {self.shoots}
                        Last 5 TIs = {last_5_TI}
                        """
