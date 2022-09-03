import torch
import torch.nn as nn
import numpy as np

model = nn.Sequential(
    
    nn.Linear(8,16),
    nn.ReLU(),
    nn.Linear(16,10),
    nn.ReLU(),
    nn.Linear(10,1),
    nn.Sigmoid()
)

def predict_diabetes(ar):
    inputs = np.array(ar)
    inputs_tensor = torch.from_numpy(inputs.astype(np.float32))

    model.load_state_dict(torch.load("weights/diabetes_80.pth",map_location="cpu"))
    

    preds = model(inputs_tensor)
    result = "Cant Check not Enough Data!"
    cures = "Congrats! You don't need any cure"
    if preds.item() >= 0.5:
        result = "You have Diabetes"
        cures = "Visit a Doctor Exercise Reguraly to contro your blood sugar level!"
    elif preds.item() < 0.5:
        result = "You Don't Have Diabetes!"
    acc = round(preds.item(),2)*100

    return {"acc":acc,"result":result,"cures":cures}


    
