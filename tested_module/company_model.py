class Department(object):

    def __init__(self, name, members=None):
        if not members:
            members = []
        self.name = name
        self.members = members

    def __str__(self):
        return self.name

    def add_member(self, name):
        assert name not in self.members
        self.members.append(name)

    def remove_member(self, name):
        assert name in self.members

    @property
    def count(self):
        return len(self.members)

    def __len__(self):
        return self.count


class CompanyModel(object):
    def __init__(self, name):
        self.name = name
        self.users = []
        self.departments = {}

    def __str__(self):
        return self.name

    def add_user(self, name, deparment):
        if name not in self.users:
            if deparment not in self.departments:
                self.departments[deparment] = Department(deparment)
            self.departments[deparment].add_member(name)
        else:
            print(f"User does not found {name}")

    def count_persons_per_department(self):
        pass

    def get_headcount_for(self, department):
        return self.departments[department].count

