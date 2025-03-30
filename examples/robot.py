# Пример для робота с "эмоциями"
class Robot:
    def __init__(self):
        self.protocols = {
            "joy": "DOG_EMOTION_12",
            "sad": "HUMAN_FEEDBACK_3"
        }
    
    def react(self, emotion: str) -> str:
        """Реакция с пояснением протокола."""
        if emotion in self.protocols:
            return f"[Активирован протокол {self.protocols[emotion]}] Виляю хвостом!" 
        return "[Система]: Режим ожидания."

# Тест
robot = Robot()
print(robot.react("joy"))
# Вывод: [Активирован протокол DOG_EMOTION_12] Виляю хвостом!
