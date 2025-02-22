import random
import recognizer

class Launcher:

    def __init__(self):
        pass

    def heads_or_tails(self):
        flip = random.choice(["heads", "tails"])
        return flip

    def importer(self, result):
        if result == "heads":
            try:
                import rando
                print("Импортирован модуль rando")
                return rando
            except ImportError:
                print("Ошибка импорта модуля rando!")
                return None
        else:
            try:
                import toep
                print("Импортирован модуль toep")
                return toep
            except ImportError:
                print("Ошибка импорта модуля toep!")
                return None

launcher = Launcher()

flip_result = launcher.heads_or_tails()

imported_module = launcher.importer(flip_result)

if imported_module:
    print("Запуск 'recognizer'...")
    recognizer_instance = recognizer.Recognizer()
    if recognizer_instance.matrix is not None:
        result_reco = recognizer_instance.reco()
        print(result_reco)
    else:
        print("Ошибка: 'matrix.npy' не загружен.")
    print("-" * 30)
else:
    print("Ошибка: не найдены модули 'rando' и 'toep'!")
    print("-" * 30)


