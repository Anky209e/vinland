import torch
import torch.nn as nn
import numpy as np

model = nn.Sequential(
    
    nn.Linear(5,10),
    nn.ReLU(),
    nn.Linear(10,1),
    nn.Sigmoid()
)
# ['age','sex','cp','trtbps','chol']
def predict_heartattack(ar):
    inputs = np.array(ar)
    inputs_tensor = torch.from_numpy(inputs.astype(np.float32))

    model.load_state_dict(torch.load("weights/heart_75.pth",map_location="cpu"))
    

    preds = model(inputs_tensor)
    result = "Cant Check not Enough Data!"
    cures = "Congrats! You don't need any cure"
    if preds.item() >= 0.5:
        result = "You have high Chance of heart attack!"
        cures = "Visit a Doctor and Do Some Cardinal Exercise!"
    elif preds.item() < 0.5:
        result = "Your Heart is Healthy!"
    acc = round(preds.item(),2)*100

    return {"acc":acc,"result":result,"cures":cures}


    

if __name__=="__main__":
    ins = [0,1,0,1,1]
    print(predict_heartattack(ins))