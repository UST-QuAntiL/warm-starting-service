import marshmallow as ma


class InitialStateMaxCutResponse:
    def __init__(self, bitstring, value):
        super().__init__()
        self.bitstring = bitstring
        self.value = value

    def to_json(self):
        json_warm_starting_response = {
            "bitstring": self.bitstring,
            "value": self.value,
        }
        return json_warm_starting_response


class InitialStateMaxCutResponseSchema(ma.Schema):
    bitstring = ma.fields.Str()
    value = ma.fields.Int()


class FixedParametersRegularGraphMaxCutResponse:
    def __init__(self, betas, gammas, approximation_ratio):
        super().__init__()
        self.betas = betas
        self.gammas = gammas
        self.approximation_ratio = approximation_ratio

    def to_json(self):
        json_warm_starting_response = {
            "betas": self.betas,
            "gammas": self.gammas,
            "approximationRatio": self.approximation_ratio,
        }
        return json_warm_starting_response


class FixedParametersRegularGraphMaxCutResponseSchema(ma.Schema):
    betas = ma.fields.List(ma.fields.Float())
    gammas = ma.fields.List(ma.fields.Float())
    approximationRatio = ma.fields.Float()
