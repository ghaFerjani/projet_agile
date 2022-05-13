Feature: Avoir la density du pays

  Etant donne un pays
  Si je lui affecte une population et une surface
  j obtiens sa density
  Scenario: Affecter une population et une surface au pays
    Given country France
    When j affecte a France sa population
    And sa surface
    Then j obtiens sa density

  Scenario Outline: Affecter une population et une surface au pays
    Given le pays <country>
    When  je set <population>
    And   je set <surface>
    Then elle me renvoie <density>
    Examples:
      | country | population | surface | density |
      | "France" | 67390000  | 543904  | 105.5   |
