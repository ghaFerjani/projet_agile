Feature: Give head quarter

    étant donnée une Holding
    je veux pouvoir retrouver la maison mere étant donnée une entreprise ou un PDG
    Afin de pouvoir faire des comparaisons

    Scenario: Retourner maison mere
        Given une filiale Louis Vuitton
        When demande la maison mere
        Then la maison mere

    Scenario Outline: Retourner Vrais
    Given une entreprise <filiale> de <mere>
    When demande la maison
    Then retourner la maison mere <mere>

    Examples:
        | filiale         | mere  |
        | Louis Vuitton   | LVMH  |
        | Fendi           | LVMH  |




