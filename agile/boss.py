from dataclasses import dataclass


@dataclass
class Boss:
    name: str
    company: str

    def change_company(self, company):
        self.company = company

    def get_company(self):
        return self.company
