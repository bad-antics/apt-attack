"""APT Simulation Core"""
import json,os,time,hashlib
from datetime import datetime

class KillChain:
    PHASES=["recon","weaponize","deliver","exploit","install","c2","actions"]
    
    def __init__(self):
        self.current_phase=0
        self.log=[]
    
    def advance(self,details=""):
        if self.current_phase>=len(self.PHASES): return False
        phase=self.PHASES[self.current_phase]
        entry={"phase":phase,"time":datetime.now().isoformat(),"details":details}
        self.log.append(entry)
        self.current_phase+=1
        return entry
    
    def status(self):
        return {"current_phase":self.PHASES[min(self.current_phase,len(self.PHASES)-1)],
                "progress":f"{self.current_phase}/{len(self.PHASES)}","log":self.log}

class MITREMapper:
    TECHNIQUES={
        "T1566":{"name":"Phishing","tactic":"initial-access"},
        "T1059":{"name":"Command and Scripting Interpreter","tactic":"execution"},
        "T1053":{"name":"Scheduled Task/Job","tactic":"persistence"},
        "T1548":{"name":"Abuse Elevation Control","tactic":"privilege-escalation"},
        "T1070":{"name":"Indicator Removal","tactic":"defense-evasion"},
        "T1003":{"name":"OS Credential Dumping","tactic":"credential-access"},
        "T1018":{"name":"Remote System Discovery","tactic":"discovery"},
        "T1021":{"name":"Remote Services","tactic":"lateral-movement"},
        "T1005":{"name":"Data from Local System","tactic":"collection"},
        "T1041":{"name":"Exfiltration Over C2","tactic":"exfiltration"},
    }
    
    def map_technique(self,technique_id):
        return self.TECHNIQUES.get(technique_id,{"name":"Unknown","tactic":"unknown"})
    
    def generate_report(self,techniques_used):
        report={"techniques":[],"tactics_covered":set()}
        for tid in techniques_used:
            t=self.map_technique(tid)
            report["techniques"].append({"id":tid,**t})
            report["tactics_covered"].add(t["tactic"])
        report["tactics_covered"]=list(report["tactics_covered"])
        report["coverage"]=f"{len(report['tactics_covered'])}/11 tactics"
        return report

class ThreatIntel:
    APT_GROUPS={"APT28":{"aliases":["Fancy Bear","Sofacy"],"origin":"Russia","targets":["government","military"]},
                "APT29":{"aliases":["Cozy Bear"],"origin":"Russia","targets":["government","think-tanks"]},
                "APT41":{"aliases":["Winnti"],"origin":"China","targets":["technology","healthcare"]},
                "Lazarus":{"aliases":["Hidden Cobra"],"origin":"North Korea","targets":["finance","crypto"]}}
    
    def get_group_info(self,name):
        return self.APT_GROUPS.get(name,{"error":"Unknown APT group"})
    
    def match_ttps(self,observed_techniques):
        matches={}
        return matches
