# ******************************************************************************
#  Copyright (c) 2020 University of Stuttgart
#
#  See the NOTICE file(s) distributed with this work for additional
#  information regarding copyright ownership.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
# ******************************************************************************

from app import warm_starting_service
from flask_smorest import Blueprint
from app.model.warm_starting_request import (
    InitialStateMaxCutRequestSchema,
    InitialStateMaxCutRequest,
    FixedParametersRegularGraphMaxCutRequestSchema,
    FixedParametersRegularGraphMaxCutRequest,
)
from app.model.warm_starting_response import (
    FixedParametersRegularGraphMaxCutResponseSchema,
    InitialStateMaxCutResponseSchema,
)

blp = Blueprint(
    "warmstarting",
    __name__,
    description="Warm-Starting techniques for quantum algorithms",
)


@blp.route("/initialStateMaxCut", methods=["POST"])
@blp.arguments(
    InitialStateMaxCutRequestSchema,
    example={
        "graph": [
            [0, 3, 3, 6, 9, 1],
            [3, 0, 4, 4, -8, 4],
            [3, 4, 0, 3, -7, 1],
            [6, 4, 3, 0, -7, 6],
            [9, -8, -7, -7, 0, -5],
            [1, 4, 1, 6, -5, 0],
        ],
        "classicalAlgorithm": "GW",
        "repetitions": "10",
        "rounded": "true",
    },
)
@blp.response(200, InitialStateMaxCutResponseSchema)
def compute_initial_state_maxcut(json: dict):
    """Precompute classical MaxCut solution."""
    print("request", json)
    return warm_starting_service.compute_initial_state_maxcut(
        InitialStateMaxCutRequest(**json)
    )


@blp.route("/initialParametersRegularGraphMaxCut", methods=["POST"])
@blp.arguments(
    FixedParametersRegularGraphMaxCutRequestSchema,
    example={
        "qaoaDepth": 2,
        "graph": [
            [0, 3, 3, 6, 9, 1],
            [3, 0, 4, 4, -8, 4],
            [3, 4, 0, 3, -7, 1],
            [6, 4, 3, 0, -7, 6],
            [9, -8, -7, -7, 0, -5],
            [1, 4, 1, 6, -5, 0],
        ],
    },
)
@blp.response(200, FixedParametersRegularGraphMaxCutResponseSchema)
def compute_fixed_parameters_regular_graph_maxcut(json: dict):
    """Execute a given quantum circuit on a specified quantum computer."""
    print("request", json)
    return warm_starting_service.compute_initial_parameters__regular_graph_maxcut(
        FixedParametersRegularGraphMaxCutRequest(**json)
    )
