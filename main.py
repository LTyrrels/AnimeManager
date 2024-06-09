import os

class AnimeManager:
    def __init__(self, filename):
        self.filename = filename
        self.categories = self.load_animes()

    def load_animes(self):
        if not os.path.exists(self.filename):
            return {}
        with open(self.filename, 'r', encoding='utf-8') as file:
            content = file.read()

        categories = {}
        current_category = None
        for line in content.split('\n'):
            line = line.strip()
            if line and not line.startswith('-'):
                current_category = line
                categories[current_category] = []
            elif line.startswith('-'):
                if current_category:
                    categories[current_category].append(line[2:])
        return categories
    
    def save_animes(self):
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                for category, animes in self.categories.items():
                    file.write(f"{category}\n")
                    for anime in animes:
                        file.write(f"- {anime}\n")
            print("Les données ont été sauvegardées avec succès.")
        except Exception as e:
            print(f"Erreur lors de la sauvegarde des données : {e}")

    def add_category(self, category):
        if category not in self.categories:
            self.categories[category] = []
            self.save_animes()
    
    def add_anime(self, category, anime):
        if category not in self.categories:
            self.categories[category] = []
        self.categories[category].append(anime)
        self.save_animes()
    
    def display_animes(self):
        for category, animes in self.categories.items():
            print(f"{category}")
            for anime in animes:
                print(f"- {anime}")

    def list_categories(self):
        for i, category in enumerate(self.categories.keys(), 1):
            print(f"{i}. {category}")

    def get_category_by_number(self, number):
        categories = list(self.categories.keys())
        if 1 <= number <= len(categories):
            return categories[number - 1]
        return None

if __name__ ==  "__main__":
    manager = AnimeManager('list.txt')

    while True:
        print("\n#######################################")
        print("##                                   ##")
        print("##             Options               ##")
        print("##                                   ##")
        print("##     [1] Afficher les animés       ##")
        print("##     [2] Ajouter une catégorie     ##")
        print("##     [3] Ajouter un animé          ##")
        print("##     [4] Credits                   ##")
        print("##     [5] Quitter                   ##")
        print("##                                   ##")
        print("#######################################")
        print(" ")

        choice = input("Choississez une option: ")

        if choice == '1':
            manager.display_animes()
        elif choice == '2':
            category = input("Entrer le nom d'une nouvelle catégorie: ")
            manager.add_category(category)
        elif choice == '3':
            print("\nCatégories disponibles:")
            manager.list_categories()
            category_number = int(input("Choisissez le numéro de la catégorie: "))
            category = manager.get_category_by_number(category_number)
            if category:
                anime = input("\nEntrez le nom de l'animé: ")
                manager.add_anime(category, anime)
            else:
                print("Numéro de catégorie invalide.")
        elif choice == '4':
            print("\nMade by jamy: \n  Telegram: @jamy667\n  Discord: asdfghjkdlzxjamy")
        elif choice == '5':
            break
        else:
            print("Option invalide. Veuillez réessayer.")