class FoodDeliverySystem:
    def __init__(self):
        self.users = [
            {"name": "Rahul", "phone": "9876543210"},
            {"name": "Anjali", "phone": "9876501234"},
            {"name": "Abhi", "phone": "9876540000"}
        ]

        self.foods = [
            {"name": "Burger", "restaurant": "Food Hub", "price": 120},
            {"name": "Pizza", "restaurant": "Pizza World", "price": 350},
            {"name": "Dosa", "restaurant": "South Spice", "price": 80},
            {"name": "Dosa", "restaurant": "Food Hub", "price": 90}
        ]

        self.restaurants = [
            {"name": "Food Hub", "location": "Kochi"},
            {"name": "Pizza World", "location": "Ernakulam"},
            {"name": "South Spice", "location": "Kochi"}
        ]

    def search_food(self):
        food_name = input("Enter food name: ").strip().lower()

        found = False
        for food in self.foods:
            if food_name in food["name"].lower():
                print(f"\nFood: {food['name']}")
                print(f"Restaurant: {food['restaurant']}")
                print(f"Price: ₹{food['price']}")
                found = True

        if not found:
            print("Food not found.")

    def search_restaurants(self):
        restaurant_name = input("Enter restaurant name: ").strip().lower()

        found = False
        for restaurant in self.restaurants:
            if restaurant_name in restaurant["name"].lower():
                print(f"\nRestaurant: {restaurant['name']}")
                print(f"Location: {restaurant['location']}")
                found = True

        if not found:
            print("Restaurant not found.")

    def nearby_restaurants(self):
        gps = input("Turn on GPS? (y/n): ").lower()

        if gps == "y":
            print("\nNearby Restaurants:")
            for restaurant in self.restaurants:
                print(f"- {restaurant['name']} ({restaurant['location']})")
        else:
            print("GPS is required.")

    def register_user(self):
        name = input("Enter name: ").strip()
        phone = input("Enter phone number: ").strip()

        for user in self.users:
            if user["name"].lower() == name.lower() and user["phone"] == phone:
                print("User already exists.")
                return

        self.users.append({"name": name, "phone": phone})
        print("Registration successful.")

    def user_login(self):
        name = input("Enter name: ").strip()
        phone = input("Enter phone number: ").strip()

        for user in self.users:
            if user["name"].lower() == name.lower() and user["phone"] == phone:
                print(f"Welcome {user['name']}!")
                return

        print("User not found.")
        choice = input("Do you want to register? (y/n): ").lower()

        if choice == "y":
            self.register_user()

    def admin_menu(self):
        username = input("Admin username: ")
        password = input("Admin password: ")

        if username != "admin" or password != "admin123":
            print("Invalid admin credentials.")
            return

        while True:
            print("\n===== ADMIN MENU =====")
            print("1. Add Food")
            print("2. Update Food")
            print("3. Delete Food")
            print("4. Add Restaurant")
            print("5. Update Restaurant")
            print("6. Delete Restaurant")
            print("7. View Users")
            print("8. Back")

            choice = input("Enter choice: ")

            if choice == "1":
                self.foods.append({
                    "name": input("Food name: "),
                    "restaurant": input("Restaurant: "),
                    "price": float(input("Price: "))
                })
                print("Food added.")

            elif choice == "2":
                name = input("Food name to update: ")
                for food in self.foods:
                    if food["name"].lower() == name.lower():
                        food["price"] = float(input("New price: "))
                        print("Food updated.")
                        break
                else:
                    print("Food not found.")

            elif choice == "3":
                name = input("Food name to delete: ")
                for food in self.foods:
                    if food["name"].lower() == name.lower():
                        self.foods.remove(food)
                        print("Food deleted.")
                        break
                else:
                    print("Food not found.")

            elif choice == "4":
                self.restaurants.append({
                    "name": input("Restaurant name: "),
                    "location": input("Location: ")
                })
                print("Restaurant added.")

            elif choice == "5":
                name = input("Restaurant name to update: ")
                for restaurant in self.restaurants:
                    if restaurant["name"].lower() == name.lower():
                        restaurant["location"] = input("New location: ")
                        print("Restaurant updated.")
                        break
                else:
                    print("Restaurant not found.")

            elif choice == "6":
                name = input("Restaurant name to delete: ")
                for restaurant in self.restaurants:
                    if restaurant["name"].lower() == name.lower():
                        self.restaurants.remove(restaurant)
                        print("Restaurant deleted.")
                        break
                else:
                    print("Restaurant not found.")

            elif choice == "7":
                print("\nRegistered Users:")
                for user in self.users:
                    print(f"{user['name']} - {user['phone']}")

            elif choice == "8":
                break

            else:
                print("Invalid choice.")

    def account(self):
        print("\nPlease login to access your account.")
        self.user_login()

    def main_menu(self):
        while True:
            print("\n===== ONLINE FOOD DELIVERY =====")
            print("1. Search Food")
            print("2. Search Restaurants")
            print("3. Nearby Restaurants")
            print("4. Account")
            print("5. Login")
            print("6. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.search_food()

            elif choice == "2":
                self.search_restaurants()

            elif choice == "3":
                self.nearby_restaurants()

            elif choice == "4":
                self.account()

            elif choice == "5":
                print("\n1. User Login")
                print("2. Admin Login")

                login_choice = input("Enter choice: ")

                if login_choice == "1":
                    self.user_login()
                elif login_choice == "2":
                    self.admin_menu()
                else:
                    print("Invalid choice.")

            elif choice == "6":
                print("Thank you for using the system.")
                break

            else:
                print("Invalid choice.")


if __name__ == "__main__":
    system = FoodDeliverySystem()
    system.main_menu()
