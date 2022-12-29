import unittest
import os, sys
import json

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)
from app import create_app


class FlaskClientTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        self.app_context.pop()

    def test_initial_state_maxcut(self):
        response = self.client.post(
            "/initialStateMaxCut",
            data=json.dumps(
                {
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
                }
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        print(response.get_json())

    def test_initial_parameters_regular_graph_maxcut(self):
        response = self.client.post(
            "/initialParametersRegularGraphMaxCut",
            data=json.dumps({"regularity": 3, "qaoaDepth": 2}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.get_json()["approximationRatio"])
        print(response.get_json())

    def test_initial_parameters_regular_graph_maxcut_via_graph(self):
        response = self.client.post(
            "/initialParametersRegularGraphMaxCut",
            data=json.dumps(
                {
                    "regularity": 3,
                    "qaoaDepth": 2,
                    "graph": [
                        [0, 3, 3, 6, 9, 1],
                        [3, 0, 4, 4, -8, 4],
                        [3, 4, 0, 3, -7, 1],
                        [6, 4, 3, 0, -7, 6],
                        [9, -8, -7, -7, 0, -5],
                        [1, 4, 1, 6, -5, 0],
                    ],
                }
            ),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.get_json()["approximationRatio"])
        print(response.get_json())
