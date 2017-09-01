import re
import numpy as np
import pylab as pl
from mini_plot_tool import MiniPlotTool

regrex = re.compile(":.*")
class CsiSoapTest:
    def __init__(self, path):
        self.path = path

    def queryPatient(self):
        query_patient = []
        with open(self.path, 'r') as csoap_data:
            content = csoap_data.readlines()

        for line in content:
            if self.findStr(line, "query patient"):
                time = re.findall(regrex, line)[0][2:-1]
                query_patient.append(float(time))
        return query_patient

    def listObjects(self):
        list_objects = {}

        with open(self.path, 'r') as csoap_data:
            content = csoap_data.readlines()
        for line in content:
            if self.findStr(line, "list objects"):
                patient_name = re.findall(r'patient.*\)', line)[0][8:-1]

                if patient_name not in list_objects.keys():
                    list_objects[patient_name] = []

                time = re.findall(regrex, line)[0][2:-1]
                list_objects[patient_name].append(float(time))
        return list_objects

    def getPresentation(self):
        list_objects = {}

        with open(self.path, 'r') as csoap_data:
            content = csoap_data.readlines()
        for line in content:
            if self.findStr(line, "GetPreseationStateInfo"):
                id = re.findall(r'id.*\)', line)[0][5:-1]

                if id not in list_objects.keys():
                    list_objects[id] = []

                time = re.findall(regrex, line)[0][2:-1]
                list_objects[id].append(float(time))
        return list_objects

    def findStr(self, string1, string2):
        if string2 in string1:
            return True
        else:
            return False

    def allPatient(self):
        patient_list = []
        with open(self.path, 'r') as csoap_data:
            content = csoap_data.readlines()

        for line in content:
            if self.findStr(line, "list objects"):
                patient_name = re.findall(r'patient.*\)', line)[0][8:-1]
                if patient_name not in patient_list:
                    patient_list.append(patient_name)
        return patient_list

    def allPresentationId(self):
        id_list = []
        with open(self.path, 'r') as csoap_data:
            content = csoap_data.readlines()

        for line in content:
            if self.findStr(line, "GetPreseationStateInfo"):
                id = re.findall(r'id.*\)', line)[0][5:-1]
                if id not in id_list:
                    id_list.append(id)
        return id_list
