# 생성자 : 인스턴스를 만들 때 호출되는 메서드

class Monster:
    def init(self, health, attack, speed):
        self.health = health
        self.attack = attack
        self.speed = speed

    def decrease_health(self, num):
        self.health -= num

    def get_health(self):
        return self.health

# 고블린 인스턴스 생성
goblin = Monster(800, 120, 300)
goblin.decrease_health(100)
print(goblin.get_health())

# 늑대 인스턴스 생성
wolf = Monster(1900, 220, 800)
wolf.decrease_health(600)
print(f"늑대의 남은 체력 {wolf.get_health()}")