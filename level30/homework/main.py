items = ["ვაშლი", "მატყუარა", "პითონი", "ლეპტოპი", "მზე"]

index = int(input("შეიყვანე ინდექსი (რიცხვი): "))

if index >= len(items):
    print("გურამი error")
else:
    print("შენი ელემენტია:", items[index])


