import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from pathlib import Path

def build_dataset():
    #Exp7.1: sweep DC
    exp1=pd.DataFrame([
        {"DC(%)":6.1,"Speed(r/min)":47,"Torque(Nm)":0.13},
        {"DC(%)":48.2,"Speed(r/min)":530,"Torque(Nm)":1.07},
        {"DC(%)":93.7,"Speed(r/min)":1127,"Torque(Nm)":1.08},
    ])

    exp2=pd.DataFrame([
        {"DC(%)":30.2,"Speed(r/min)":383,"Torque(Nm)":0.01},
        {"DC(%)":30.2,"Speed(r/min)":290,"Torque(Nm)":1.13},
        {"DC(%)":30.2,"Speed(r/min)":202,"Torque(Nm)":1.81},
        {"DC(%)":30.2,"Speed(r/min)":199,"Torque(Nm)":1.8},
    ])

    exp3=pd.DataFrame([
        {"DC(%)":50.3,"Speed(r/min)":663,"Torque(Nm)":0.01},
        {"DC(%)":50.3,"Speed(r/min)":575,"Torque(Nm)":1.08},
        {"DC(%)":50.3,"Speed(r/min)":488,"Torque(Nm)":1.93},
        {"DC(%)":50.3,"Speed(r/min)":208,"Torque(Nm)":1.95},
    ])
    return exp1,exp2,exp3
def plot_exp1