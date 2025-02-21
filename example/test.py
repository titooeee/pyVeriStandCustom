from niveristand import nivs_rt_sequence, NivsParam, realtimesequencetools
from niveristand.clientapi import *
from niveristand.library import wait
from configClass import config_1


@nivs_rt_sequence
def test():
    var3 = DoubleValue(0)
    var3.value = config_1.max_val.value

if __name__ == "__main__":
    realtimesequencetools.save_py_as_rtseq(test,r"C:\Users\Public\Documents\dynoSoftwareSuite\pythonSource\37nivspython")