# Warm-Starting Service
![Tests passed](https://github.com/UST-QuAntiL/warm-starting-service/actions/workflows/test.yml/badge.svg)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

The warm-starting service enables the classical pre-computation of quantum circuit parameters and initial states.
Using these as inputs can speed up to overall computation time due to the faster convergence of circuit parameters, and can improve the result's precision.

## Running the Service

The easiest way to get start is using a pre-built Docker image:

``docker run -p 5077:5077 planqk/warm-starting-service``

Alternatively, the service can be built manually:
1. Clone the repository using ``git clone https://github.com/UST-QuAntiL/warm-starting-service.git``
2. Navigate to the corresponding folder within the cloned repository ``cd warm-starting-service``
3. Build the Docker container: ``docker build -t warm-starting-service .``
4. Run the Docker container: ``docker run -p 5077:5077 warm-starting-service``

Then the service can be accessed via: [http://127.0.0.1:5077](http://127.0.0.1:5077).

## API Documentation

The warm-starting service provides a Swagger UI, specifying the request schemas and showcasing exemplary requests for all API endpoints.
 * Swagger UI: [http://127.0.0.1:5077/api/swagger-ui](http://127.0.0.1:5077/api/swagger-ui).

## Developer Guide

### Setup (exemplary for ubuntu 18.04): 
```shell
git clone https://github.com/UST-QuAntiL/Quokka.git
cd warm-starting-service

# if virtualenv is not installed
sudo -H pip install virtualenv

# create new virtualenv called 'venv'
virtualenv venv

# activate virtualenv; in Windows systems activate might be in 'venv/Scripts'
source venv/bin/activate

#install application requirements.
pip install -r requirements.txt
```

### Execution:
* Run the application with: ``flask run --port=5077``
* Test with: ``python -m unittest discover``
* Coverage with: ``coverage run --branch --include 'app/*' -m unittest discover; coverage report``

### Codestyle: 
``black .`` OR ``black FILE|DIRECTORY``

## Disclaimer of Warranty
Unless required by applicable law or agreed to in writing, Licensor provides the Work (and each Contributor provides its Contributions) on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied, including, without limitation, any warranties or conditions of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A PARTICULAR PURPOSE. You are solely responsible for determining the appropriateness of using or redistributing the Work and assume any risks associated with Your exercise of permissions under this License.

## Haftungsausschluss
Dies ist ein Forschungsprototyp. Die Haftung für entgangenen Gewinn, Produktionsausfall, Betriebsunterbrechung, entgangene Nutzungen, Verlust von Daten und Informationen, Finanzierungsaufwendungen sowie sonstige Vermögens- und Folgeschäden ist, außer in Fällen von grober Fahrlässigkeit, Vorsatz und Personenschäden, ausgeschlossen.
