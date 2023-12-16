import random


def gift_randomizer(persons: list):
    donors = persons[::-1]
    for i in range(len(donors)):
        donor = donors[i]
        while True:
            random_i = random.randint(0, len(persons) - 1)
            if donor == persons[random_i]:
                continue
            recipient = persons.pop(random_i)
            break
        print(f'{donor} дарує {recipient}')
    print('_' * 20)


def main():
    
    persons = ['Олексій', 'Катя До.', 'Юля', 'Настя', 'Надя', 'Андрій', 'Родіон', 'Саня']
    gift_randomizer(persons)
    
    
if __name__ == '__main__':
    main()