def plan_subtopics(question: str, clarification: list) -> list:
    if "бизнес" in question.lower():
        return ["Целевая аудитория", "Инвестиции и стартовый капитал", "Локальный спрос", "Конкуренция", "Операционные риски"]
    else:
        return ["Аспект 1", "Аспект 2", "Аспект 3", "Аспект 4"]
