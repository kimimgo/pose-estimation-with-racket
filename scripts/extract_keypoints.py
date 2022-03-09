import json
import pandas as pd

wpath = '/home/imgyu/workspace/projects/modu/AlphaPose'
path = f'{wpath}/airiss-data'

f = open(f'{path}/data.json', encoding="UTF-8")

data=json.loads(f.read())

 = pd.read_json(f)