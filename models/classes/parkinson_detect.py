import torch
import torch.nn as nn
import numpy as np

model = nn.Sequential(
    
    nn.Linear(5,10),
    nn.ReLU(),
    nn.Linear(10,1),
    nn.Sigmoid()
)
# [fo_hz,fhi_hz,flo_hz,jitter,jitter_abs]
def predict_parkinson(ar):
    inputs = np.array(ar)
    inputs_tensor = torch.from_numpy(inputs.astype(np.float32))

    model.load_state_dict(torch.load("weights/parkinson_82.pth",map_location="cpu"))
    

    preds = model(inputs_tensor)
    result = "Cant Check"
    cures = "Congrats! You don't need any cure"
    if preds.item() >= 0.5:
        result = "Parkinson Detected"
        cures = "Visit a Docotor,Most treatment includes Deep brain simulation and medicines!"
    elif preds.item() < 0.5:
        result = "NO Parkinson Detected"
    acc = round(preds.item(),2)*100

    return {"acc":acc,"result":result,"cures":cures}


    

if __name__=="__main__":
    ins = [119.992,157.302,74.997,0.00784,0.00007]
    print(predict_parkinson(ins))