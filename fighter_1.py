from base_component import BaseComponent

class Fighter(BaseComponent):
    def __init__(self, hp: int, defence: int, power: int):
        self.max_hp = hp
        self._hp = hp
        self.defence = defence
        self.power = power

    @property
    def hp(self) -> int:
        return self._hp
    
    @hp.setter
    def hp(self, value: int) -> None:
        self._hp = max(0, min(value, self.max_hp))