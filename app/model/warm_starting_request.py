import marshmallow as ma


class InitialStateMaxCutRequest:
    def __init__(
        self,
        graph,
        classicalAlgorithm="gw",
        repetitions=1,
        rounded=False,
    ):
        self.graph = graph
        self.classical_algorithm = classicalAlgorithm.lower()
        self.repetitions = repetitions
        self.rounded = rounded


class InitialStateMaxCutRequestSchema(ma.Schema):
    graph = ma.fields.List(ma.fields.List(ma.fields.Int()), required=True)
    classicalAlgorithm = ma.fields.Str(required=False)
    repetitions = ma.fields.Int(required=False)
    rounded = ma.fields.Bool(required=False)


class FixedParametersRegularGraphMaxCutRequest:
    def __init__(self, qaoaDepth, regularity=None, graph=None):
        super().__init__()
        self.regularity = regularity
        self.qaoa_depth = qaoaDepth
        self.graph = graph


class FixedParametersRegularGraphMaxCutRequestSchema(ma.Schema):
    qaoaDepth = ma.fields.Int(required=True)
    regularity = ma.fields.Int(required=False)
    graph = ma.fields.List(ma.fields.List(ma.fields.Float()), required=False)
