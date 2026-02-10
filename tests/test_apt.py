import unittest,sys,os
sys.path.insert(0,os.path.join(os.path.dirname(__file__),"..","src"))
from apt_attack.core import KillChain,MITREMapper

class TestKillChain(unittest.TestCase):
    def test_advance(self):
        kc=KillChain()
        r=kc.advance("recon phase")
        self.assertEqual(r["phase"],"recon")

class TestMITRE(unittest.TestCase):
    def test_map(self):
        m=MITREMapper()
        t=m.map_technique("T1566")
        self.assertEqual(t["name"],"Phishing")
    def test_report(self):
        m=MITREMapper()
        r=m.generate_report(["T1566","T1059","T1003"])
        self.assertEqual(len(r["techniques"]),3)

if __name__=="__main__": unittest.main()
