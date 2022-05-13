from dataclasses import dataclass, field


@dataclass
class Country:
    name: str = 'France'
    tax_rate: int = 0.2
    towns: list = field(default_factory=list)

    def __init__(self):
        self.surface = None
        self.population = None

    def gdp_country(self):
        total_gdp = 0
        for town in self.towns:
            total_gdp += town.gdp_town()
        return total_gdp

    def add_towns(self, towns):
        for town in towns:
            town.country = self
            self.towns.append(town)

    def set_population_and_surface(self, population, surface):
        self.population = population
        self.surface = surface

    def calculate_density(self):
        return self.population / self.surface

    def get_tax_rate(self):
        return self.tax_rate
