# ვქმნით ცვლადს სახელად password და ვანიჭებთ მას მნიშვნელობას "SecretWord"
password = "SecretWord"

# ვთხოვთ მომხმარებელს შეიყვანოს პაროლი და შედეგს ვინახავთ guess ცვლადში
guess = input("შეიყვანეთ პაროლი: ")

# სანამ მომხმარებლის შეყვანილი პაროლი არ ემთხვევა სწორ პაროლს
while guess != password:
    # კვლავ ვთხოვთ მომხმარებელს შეყვანას
    guess = input("არასწორია, სცადეთ თავიდან: ")

# თუ პაროლი სწორად შეიყვანა, ვბეჭდავთ შეტყობინებას
print("წვდომა მიღებულია")