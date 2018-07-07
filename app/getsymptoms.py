from PriaidDiagnosisClient import DiagnosisClient
import os
from pprint import pprint

user = os.environ['DC_USER']
password = os.environ['DC_PASSWORD']
authServiceURL = "https://sandbox-authservice.priaid.ch/login"
healthServiceURL = "https://sandbox-healthservice.priaid.ch"
language = "en-gb"

dc = DiagnosisClient(username=user, password=password,
                    authServiceUrl=authServiceURL,
                    language=language,
                    healthServiceUrl=healthServiceURL)

data = dc.loadSymptoms()
pprint(data)