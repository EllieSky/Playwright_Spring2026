import random


class Weapon:
    def __init__(self, name, power, wtype):
        self.name = name
        self.power = power
        self.wtype = wtype  # e.g., "Bow", "Staff", "Sword"

    def __str__(self):
        return f"{self.name} ({self.wtype}, Power: {self.power})"


class Character:
    def __init__(self, name, hp, base_dmg, preferred_weapon):
        self.name = name
        self.hp = hp
        self.base_dmg = base_dmg
        self.preferred_weapon = preferred_weapon
        self.weapon = None  # Composition: Character HAS-A Weapon

    def equip(self, weapon):
        self.weapon = weapon
        print(f"--- {self.name} equipped {weapon.name} ---")

    def unequip(self):
        print(f"--- {self.name} dropped their weapon ---")
        self.weapon = None

    def calculate_damage(self):
        if not self.weapon:
            return self.base_dmg

        damage = self.base_dmg + self.weapon.power

        # Composition Interaction: Check if the weapon type matches character preference
        if self.weapon.wtype == self.preferred_weapon:
            damage = int(damage * 1.5)
            print(f"[BONUS] Proficiency match! Damage increased to {damage}.")

        return damage

    def status(self):
        w_status = self.weapon if self.weapon else "Unarmed"
        print(f"STATUS: {self.name} | Type: {self.__class__.__name__} | HP: {self.hp} | Weapon: {w_status}")


# --- Specialized Classes (Inheritance) ---

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, hp=150, base_dmg=15, preferred_weapon="Sword")


class Mage(Character):
    def __init__(self, name):
        super().__init__(name, hp=80, base_dmg=5, preferred_weapon="Staff")


class Archer(Character):
    def __init__(self, name):
        super().__init__(name, hp=110, base_dmg=10, preferred_weapon="Bow")
        self.crit_chance = 0.15

    def calculate_damage(self):
        # Call the parent logic (including weapon power and proficiency)
        damage = super().calculate_damage()

        # Add Archer-specific unique logic (Critical Hit)
        if random.random() < self.crit_chance:
            damage *= 2
            print(f"[CRITICAL] Massive hit! Damage doubled to {damage}.")

        return damage


# --- Testing the System ---

if __name__ == "__main__":
    # Create Weapons
    excalibur = Weapon("Excalibur", 25, "Sword")
    oak_staff = Weapon("Oak Staff", 15, "Staff")
    great_bow = Weapon("Great Bow", 20, "Bow")

    # Create Characters
    player1 = Archer("Legolas")
    player2 = Warrior("Thorin")

    # Scenario 1: Archer using the WRONG weapon
    player1.equip(excalibur)
    player1.status()
    print(f"Damage dealt: {player1.calculate_damage()}\n")

    # Scenario 2: Archer using the RIGHT weapon (Proficiency Bonus)
    player1.equip(great_bow)
    player1.status()
    print(f"Damage dealt: {player1.calculate_damage()}\n")

    # Scenario 3: Warrior using their preferred weapon
    player2.equip(excalibur)
    player2.status()
    print(f"Damage dealt: {player2.calculate_damage()}\n")
