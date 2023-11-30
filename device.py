class Device:
    def __init__(self, model, memory_type, color, manufacturer):
        self._model = model
        self._memory_type = memory_type
        self._color = color
        self._manufacturer = manufacturer

    




class Phone(Device):
    def __init__(self, model, memory_type, color, manufacturer, is_smartphone):
        super().__init__(model, memory_type, color, manufacturer)
        self._is_smartphone = is_smartphone

    def display_info(self):
        smartphone_info = "Smartphone" if self._is_smartphone else "Not a smartphone"
        return f"{self._manufacturer} {self._model}, {self._color}, {self._memory_type} memory. {smartphone_info}"