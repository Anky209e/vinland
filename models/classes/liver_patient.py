import torch
import torch.nn as nn
import numpy as np

model = nn.Sequential(
    
    nn.Linear(6,9),
    nn.ReLU(),
    nn.Linear(9,12),
    nn.ReLU(),
    nn.Linear(12,1),
    nn.Sigmoid()
)

def predict_liver_failure(ar):
    inputs = np.array(ar)
    inputs_tensor = torch.from_numpy(inputs.astype(np.float32))

    model.load_state_dict(torch.load("weights/liver_patient_75.pth",map_location="cpu"))
    

    preds = model(inputs_tensor)
    result = "Cant Check not Enough Data!"
    cures = "Congrats! You don't need any cure"
    if preds.item() >= 0.5:
        result = "You have high Chance of Liver Failure!"
        cures = "Visit a Doctor and Stop Consuming alcohol if you are a addict! "
    elif preds.item() < 0.5:
        result = "Your Liver is Healthy!"
    acc = round(preds.item(),2)*100

    return {"acc":acc,"result":result,"cures":cures}

