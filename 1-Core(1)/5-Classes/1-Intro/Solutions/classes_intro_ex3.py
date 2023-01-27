# enter code for Athlete class here
class Athlete:
    counter = 0
    gold_medal_totals = {}
    silver_medal_totals = {}
    bronze_medal_totals = {}

    def __init__(self, name, country):
        self.name = name
        self.gold_medals = 0
        self.silver_medals = 0
        self.bronze_medals = 0
        self.country = country
        Athlete.counter += 1
        Athlete.gold_medal_totals[self.country] = 0
        Athlete.silver_medal_totals[self.country] = 0
        Athlete.bronze_medal_totals[self.country] = 0
        

    def award_medal(self,medal):
        if medal == 'gold':
            self.gold_medals+=1
            Athlete.gold_medal_totals[self.country] += 1
        elif medal == 'silver':
            self.silver_medals+=1
            Athlete.silver_medal_totals[self.country] += 1
        elif medal == 'bronze':
            self.bronze_medals+=1
            Athlete.bronze_medal_totals[self.country] += 1
        elif medal == 'none':
            print ('please try harder next time')
        else:
            print('please input either gold, silver, bronze or none.')


# Simon = Athlete('GB')
# Pierre = Athlete('FR')
# Xavi = Athlete('ESP')
# Simon.award_medal('gold')
# Pierre.award_medal('silver')
# Xavi.award_medal('bronze')

# print('gold:',Athlete.gold_medal_count)
# print('silver:',Athlete.silver_medal_count)
# print('bronze:',Athlete.bronze_medal_count)