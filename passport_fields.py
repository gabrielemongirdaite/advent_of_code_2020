import re

class passport:
    def __init__(self, entry):
        self.entry = entry
        self.birth_year = 'byr'
        self.issue_year = 'iyr'
        self.expiration_year = 'eyr'
        self.height = 'hgt'
        self.hair = 'hcl'
        self.eye = 'ecl'
        self.pid = 'pid'

    def check_items(self):
        self.list_features = [self.birth_year, self.issue_year, self.expiration_year, self.height, self.hair, self.eye, self.pid]
        return set(self.list_features).issubset(self.entry)

    def check_birth_year(self):
        if 1920<=int(self.entry[self.birth_year])<=2002:
            return True
        else:
            return False

    def check_issue_year(self):
        if 2010<=int(self.entry[self.issue_year])<=2020:
            return True
        else:
            return False

    def check_expiry_year(self):
        if 2020<=int(self.entry[self.expiration_year])<=2030:
            return True
        else:
            return False

    def check_height(self):
        if self.entry[self.height][-2:] == 'cm':
            if 150<=int(self.entry[self.height][:-2])<=193:
                return True
            else:
                return False
        elif self.entry[self.height][-2:] == 'in':
            if 59<=int(self.entry[self.height][:-2])<=76:
                return True
            else:
                return False
        else:
            return False

    def check_hair(self):
        if self.entry[self.hair][0] == '#':
            if len(self.entry[self.hair][1:]) == 6 and bool(re.compile('^[a-f0-9]+$').match(self.entry[self.hair][1:])):
                return True
            else:
                return False
        else:
            return False

    def check_eyes(self):
        return self.entry[self.eye] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    def check_passport_id(self):
        if len(self.entry[self.pid]) == 9 and bool(re.compile('^[0-9]+$').match(self.entry[self.pid])):
            return True
        else:
            return False