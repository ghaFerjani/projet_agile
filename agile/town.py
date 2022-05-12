from dataclasses import dataclass
from country import Country


@dataclass
class Town:
    country: Country
    name: str = 'Paris'
    gdp_per_habitat: int = 38
    nb_habitats: int = 2_000_000

    # bidirectional
    def set_country(self, country):
        if self.country.name != country.name:
            self.country.towns.remove(self)
            self.country = country

    def gdp_town(self):
        return self.gdp_per_habitat * self.nb_habitats

