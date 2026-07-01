print("====================================")
print("     MOVIE RECOMMENDATION SYSTEM")
print("====================================")

print("\nAvailable Categories")
print("1. Action")
print("2. Comedy")
print("3. Horror")
print("4. Romance")

choice = input("\nEnter your favourite category: ")

if choice.lower() == "action":
    print("\nRecommended Movies:")
    print("• Avengers")
    print("• John Wick")
    print("• Mission Impossible")

elif choice.lower() == "comedy":
    print("\nRecommended Movies:")
    print("• Home Alone")
    print("• Mr. Bean")
    print("• Jumanji")

elif choice.lower() == "horror":
    print("\nRecommended Movies:")
    print("• The Conjuring")
    print("• Annabelle")
    print("• Insidious")

elif choice.lower() == "romance":
    print("\nRecommended Movies:")
    print("• Titanic")
    print("• The Notebook")
    print("• Me Before You")

else:
    print("\nSorry! Category not available.")
