from fastapi import FastAPI
from dataclasses import dataclass, asdict
from typing import List, Dict

app = FastAPI(title="KEMETIX // Vanguard Core Directive", version="1.0.0")


@dataclass
class VanguardOperative:
    callsign: str
    role: str
    subsystem_access: List[str]
    status: str = "ONLINE"


class VanguardCoreEngine:
    def __init__(self, squad_name: str = "Vanguard Squad"):
        self.squad_name = squad_name
        self.operatives: Dict[str, VanguardOperative] = {}
        self._initialize_squad()

    def _initialize_squad(self) -> None:
        roster = [
            VanguardOperative(
                callsign="CodeWeaver",
                role="Systems Architect / Logic Orchestration",
                subsystem_access=["kernel", "automation", "fastapi_bridge"],
            ),
            VanguardOperative(
                callsign="Aurixa Prime",
                role="Quantum Phasing / Execution Specialist",
                subsystem_access=["runtime", "pipeline_dispatch"],
            ),
            VanguardOperative(
                callsign="Echo Engineer",
                role="Replication & Task Automation",
                subsystem_access=["n8n_webhooks", "async_queue"],
            ),
        ]
        for unit in roster:
            self.operatives[unit.callsign] = unit

    def get_manifest(self) -> dict:
        return {
            "squad": self.squad_name,
            "units": [asdict(op) for op in self.operatives.values()],
            "system_state": "OPTIMAL",
        }


engine = VanguardCoreEngine()


@app.get("/")
def read_root():
    return {
        "status": "[VANGUARD SYSTEM READY]",
        "directive": "KEMETIX DIVISION ARCHITECTURE PROTOCOL APPROVED",
        "manifest": engine.get_manifest(),
    }
