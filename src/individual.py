class Individual():
    def __init__(self, id_number):
        self.id_number = id_number
        self.preference_list = []
        self.available_proposals = []
        self.partner = None

    def get_priority(self, other):
        return self.preference_list.index(other)

    def get_list_id(self, instance_list):
        id_list = []
        for i in instance_list:
            id_list.append(i.id_number if i else None)
        return id_list

    def __str__(self):
        output = ('id_number={0} preference_list={1} available_proposals={2} '
                  'partner={3}'.format(
                      self.id_number,
                      self.get_list_id(self.preference_list),
                      self.get_list_id(self.available_proposals),
                      self.partner.id_number if self.partner else None))
        return output
