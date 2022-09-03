import torch
import torch.nn as nn
import numpy as np

model = nn.Sequential(
    nn.Linear(3,7),
    nn.LeakyReLU(0.2),
    nn.Linear(7,1),
    nn.Sigmoid()
)

def predict_pcos(ar):
    inputs = np.array(ar)
    inputs_tensor = torch.from_numpy(inputs.astype(np.float32))

    model.load_state_dict(torch.load("weights/pcos_68.pth",map_location="cpu"))
    

    preds = model(inputs_tensor)
    result = "Can't Check not Enough Data!"
    cures = "Congrats! You don't need any cure"
    if preds.item() >= 0.5:
        result = "You have high Chances of PCOS"
        cures = "Consult a Doctor for medicine! Try losing weight if you are overweight!"
    elif preds.item() < 0.5:
        result = "You Don't have any danger of PCOS"
    acc = round(preds.item(),2)*100

    return {"acc":acc,"result":result,"cures":cures}


    

