import random


def gift_randomizer(file_name: str, persons: list):
    pairs = ''
    donors = persons[::-1]
    for i in range(len(donors)):
        donor = donors[i]
        while True:
            random_i = random.randint(0, len(persons) - 1)
            if donor == persons[random_i]:
                continue
            recipient = persons.pop(random_i)
            break
        pair = f'{donor} makes gift to {recipient}\n'
        pairs += pair
        
    with open(file_name, 'a+') as fd:
        fd.writelines(pairs)

        
    print('Pairs created /...')


def main():
    
    persons = ['Olexiy', 'Kate Do.', 'Yulia', 'Pypok', 'Nadia', 'Andriy', 'Rodion', 'Sashka', 'Ihor', 'Kate Ro.']
    file_name = 'gift_pairs.txt'
    gift_randomizer(file_name, persons)
    
    
if __name__ == '__main__':
    main()