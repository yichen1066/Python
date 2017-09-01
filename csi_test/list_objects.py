from csi_soap_test import CsiSoapTest
from mini_plot_tool import MiniPlotTool

if __name__ == "__main__":
    baseConfig = {
       # 'figsize' : (6,8),
       # 'axis': [0,10,0,10],
       'title' : 'list objects',
       'ylabel' : 'time(s)',
       'grid': True,
        'xaxis_locator' : 2,
       # 'yaxis_locator' : 1,
       # 'legend_loc' : 'upper right'
    }
    csoap_test = CsiSoapTest("d:\\csi_use_csoap.log")
    gsopa_test = CsiSoapTest("d:\\csi_use_gsoap.log")

    tool_list_objects = MiniPlotTool(baseConfig)
    all_patients = csoap_test.allPatient()

    patient_data_csoap = csoap_test.listObjects()
    patient_data_gsoap = gsopa_test.listObjects()

    line_data_csoap = []
    line_data_gsoap = []

    X = [i for i in range(20)]

    for i in range(len(all_patients)):
        line_data_csoap.append(patient_data_csoap.get(all_patients[i]))
    for i in range(len(all_patients)):
        line_data_gsoap.append(patient_data_gsoap.get(all_patients[i]))
    lineconf1 = {
       'X': X,
       'Y': line_data_csoap[0],
       # 'marker' : 'x',
       # 'color' : 'b',
       # 'markerfacecolor' : 'r',
       'label' : 'use_csoap(' + all_patients[0] + ')',
       # 'linewidth' : 3,
       # 'linestyle' : '--'
    }
    lineconf1_ = {
       'X': X,
       'Y': line_data_gsoap[0],
       'marker': 'o',
       'color': 'b',
       'markerfacecolor': 'r',
       'label': 'use_gsoap(' + all_patients[0] + ')',
       'linewidth': 3,
       'linestyle': '--'
    }

    lineconf2 = {
       'X': X,
       'Y': line_data_csoap[1],
        'marker' : 'o',
       # 'color' : 'b',
       'markerfacecolor' : 'r',
       'label' : 'use_csoap(' + all_patients[1] + ')',
       # 'linewidth' : 3,
       # 'linestyle' : '--'
    }
    lineconf2_ = {
       'X': X,
       'Y': line_data_gsoap[1],
        'marker' : 'x',
       # 'color' : 'b',
       'markerfacecolor' : 'r',
       'label' : 'use_cgoap(' + all_patients[1] + ')',
       # 'linewidth' : 3,
       # 'linestyle' : '--'
    }

    tool_list_objects.addline(lineconf1)
    tool_list_objects.addline(lineconf1_)
    tool_list_objects.addline(lineconf2)
    tool_list_objects.addline(lineconf2_)

    tool_list_objects.plot()
    tool_list_objects.show()
