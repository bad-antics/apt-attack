from apt_attack.core import KillChain,MITREMapper
kc=KillChain()
for detail in ["OSINT gathering","Craft exploit","Spear phishing","CVE-2024-XXX","Persistence","C2 beacon","Data exfil"]:
    r=kc.advance(detail)
    if r: print(f"Phase {r['phase']}: {detail}")
m=MITREMapper()
r=m.generate_report(["T1566","T1059","T1053","T1003","T1041"])
print(f"\nCoverage: {r['coverage']}")
