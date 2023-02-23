# 1. Ask for user input -> ditto
# 2. Create a dynamic URL based on step 1
# 3. Fetch the data from the url in step 2
# 4. Convert JSON to a dictionary
# 5. Print out pokemon data


import requests


while True:

    pokeName = input("Choose a pokemon: ")
    pokeName = pokeName.lower() 

    url = f"https://pokeapi.co/api/v2/pokemon/{pokeName}"

    req = requests.get(url)
    if req.status_code == 200:
        data = req.json()
        

        print(f"You choosed:\t{data['name']}\n")
       

        abilityNames = []

        for ability in data.get('abilities'):
            abilityNames.append(ability['ability']['name'])

        print("Base Experience: ", data.get('base_experience'))
        print("Height:\t", data.get('height'))
        print("Order:\t", data.get('order'))
        print("Abilities: ")
        for ability in abilityNames:
            print(ability)
        continue
    elif pokeName.lower() == "quit":
        break
    else:
        print("Pokemon does not exist! Please try another one!")
        continue
