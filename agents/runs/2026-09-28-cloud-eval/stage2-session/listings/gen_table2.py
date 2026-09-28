import json, os
S=os.path.dirname(os.path.abspath(__file__))
A=json.load(open(S+"/analysis.json"))
cfgs=[]
for tag,R in A.items():
    if tag.endswith("_Jext"): continue
    for Jk,ent in R["J"].items():
        J,plane=Jk.split("_")
        if plane!="h": continue
        if R["seed"]!=7 and J!="-1": continue
        cfgs.append({"tag":tag,"m":R["m"],"N":R["N"],"seed":R["seed"],"J":int(J),"amp":ent["rule"]["mean1_in_cell2"],"bias":R["bias"],"kind":"matched"})
    if R["seed"]==7 and R["N"]==240:
        for a in (4e-3,7e-3,1.1e-2,1.7e-2,2.4e-2):
            cfgs.append({"tag":tag,"m":R["m"],"N":R["N"],"seed":7,"J":None,"amp":a,"bias":R["bias"],"kind":"ladder"})
json.dump(cfgs,open(S+"/table2_cfgs.json","w"),indent=1)
print(len(cfgs),"table2 jobs")
