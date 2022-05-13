from boss import *
from country import *


@dataclass
class Subsidiary:
    parent: str
    subsidiary: str
    pdg: Boss
    parent_subsidiary_country: Country
    subsidiary_country: Country

    def is_subsidiary(self, pdg):
        return self.parent == Boss.get_company(self.pdg)

    def detect_fiscal_optimisation(self) -> bool:
        return self.parent_subsidiary_country.get_tax_rate() != self.subsidiary_country.get_tax_rate()
