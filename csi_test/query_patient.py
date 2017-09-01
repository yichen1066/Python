from mini_plot_tool import MiniPlotTool
from csi_soap_test import *

if __name__ == "__main__":
    baseConfig = {
       # 'figsize' : (6,8),
       # 'axis': [0,10,0,10],
       'title' : 'query patient',
       'ylabel' : 'time(s)',
       'grid': True,
        'xaxis_locator' : 2,
        #'yaxis_locator' : 0.1,
       # 'legend_loc' : 'upper right'
    }
    tool_query_patient = MiniPlotTool(baseConfig)

    csoap_test = CsiSoapTest("d:\\csi_use_csoap.log")
    gsopa_test = CsiSoapTest("d:\\csi_use_gsoap.log")

    X = [i for i in range(20)]
    Y1 = csoap_test.queryPatient()
    Y2 = gsopa_test.queryPatient()

    lineConf = {
       'X': X,
       'Y': Y1,
       # 'marker' : 'x',
       # 'color' : 'b',
       # 'markerfacecolor' : 'r',
       'label' : 'use_csoap',
       # 'linewidth' : 3,
       # 'linestyle' : '--'
    }
    lineConf2 = {
       'X': X,
       'Y': Y2,
       'marker': 'o',
       'color': 'b',
       'markerfacecolor': 'r',
       'label': 'use_gsoap',
       'linewidth': 3,
       'linestyle': '--'
    }
    # tool.plotSingleLine(lineConf)
    tool_query_patient.addline(lineConf)
    tool_query_patient.addline(lineConf2)

    # print tool.removeline(1)
    tool_query_patient.plot()
    tool_query_patient.show()
