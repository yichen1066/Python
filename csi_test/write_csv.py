from csi_soap_test import CsiSoapTest
import csv

if __name__ == "__main__":
    csoap_test = CsiSoapTest("d:\\csi_use_csoap.log")
    gsopa_test = CsiSoapTest("d:\\csi_use_gsoap.log")

    n = [i+1 for i in range(20)]
    row = [''] + n
    out = open('d:\\test_result.csv', 'a', newline="")
    csv_write = csv.writer(out, dialect='excel')
    csv_write.writerow(row)

    csoap_query_patient = ['csoap query patient(s)'] + csoap_test.queryPatient()

    csv_write.writerow(csoap_query_patient)
    gsoap_query_patient = ['gsoap_query_patient(s)'] + gsopa_test.queryPatient()
    csv_write.writerow(gsoap_query_patient)

    all_patient = csoap_test.allPatient()
    list_objects = csoap_test.listObjects()

    for patient in all_patient:
        row = [patient] + list_objects.get(patient)
        csv_write.writerow(row)

    list_objects1 = gsopa_test.listObjects()

    for patient in all_patient:
        row = [patient] + list_objects1.get(patient)
        csv_write.writerow(row)

    all_id = csoap_test.getPresentation()
    presentationstate1 = csoap_test.allPresentationId()
    presentationstate2 = gsopa_test.allPresentationId()

    for id in all_id:
        row = [id] + all_id.get(id)
        csv_write.writerow(row)
    for id in all_id:
        row = [id] + all_id.get(id)
        csv_write.writerow(row)

