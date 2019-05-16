class MatchPair:

    def __init__(self, request_model, pair_factory, pair_repository):
        self.student = request_model.student
        self.project = request_model.project
        self.pair_factory = pair_factory
        self.pair_repository = pair_repository

    def execute(self):
        pair = self.pair_factory.create(self.student, self.project)
        self.pair_repository.add(pair)


class MatchPairRequestModel:

    def __init__(self, student, project):
        self.student = student
        self.project = project


class UnmatchPairByProject:

    def __init__(self, request_model, pair_repository):
        self.project = request_model.project
        self.pair_repository = pair_repository

    def execute(self):
        self.pair_repository.remove_by_project(self.project)


class UnmatchPairByProjectRequestModel:

    def __init__(self, project):
        self.project = project