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

import json
import os
import config
from app.model.warm_starting_response import (
    InitialStateMaxCutResponse,
    FixedParametersRegularGraphMaxCutResponse,
)
from app.model.warm_starting_request import (
    InitialStateMaxCutRequest,
    FixedParametersRegularGraphMaxCutRequest,
)
from app.service_functions.gw_algorithm import best_gw_cuts


# Classically approximating a graphs Maximum cut
def compute_initial_state_maxcut(request: InitialStateMaxCutRequest):
    if request.classical_algorithm in ["gw", "goemans-williamson"]:
        string, value = best_gw_cuts(request.graph, request.repetitions)
        return InitialStateMaxCutResponse(string, value)
    else:
        return "This requested classical algorithm is not available"


# Retrieving fixed angles with a guaranteed approximation ratio as shown in: https://arxiv.org/pdf/2107.00677.pdf
def compute_initial_parameters__regular_graph_maxcut(
    request: FixedParametersRegularGraphMaxCutRequest,
):
    if request.graph:
        import networkx as nx
        import numpy as np

        try:
            np_graph_array = np.array(request.graph)
            nx_graph = nx.from_numpy_matrix(np_graph_array)
            if nx.is_regular(nx_graph):
                n1 = nx.utils.arbitrary_element(nx_graph)
                request.regularity = nx_graph.degree(n1)
        except Exception:
            return "Graph must be regular for this method to be used"
    if request.regularity is None:
        return 'Request must contain a value for "regularity" or a valid regular graph'

    def get_angles(p: int, conn: int) -> tuple:
        try:
            data_p = data[str(conn)][str(p)]
            return data_p["gamma"], data_p["beta"], data_p["AR"]
        except KeyError:
            print("Angles not found!")

    # Opening JSON file
    angles_path = os.path.join(config.basedir, "resources", "fixedAngles.json")
    with open(angles_path) as json_file:
        data = json.load(json_file)
        gamma, beta, approximation_ratio = get_angles(
            request.qaoa_depth, request.regularity
        )
        return FixedParametersRegularGraphMaxCutResponse(
            beta, gamma, approximation_ratio
        ).to_json()
