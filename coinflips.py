import random
import matplotlib.pyplot as plt

def main():
    chance_heads = 50
    chance_tails = 50
    count_heads = 0
    count_tails = 0
    flip_list_heads = [0]
    flip_list_tails = [0]
    diff_heads_tails =[0]

    flips = int(input("Enter the number of coin flips --> "))
    if (int(input("Want to rig the coin? (1 - yes, 0 - no) -->  "))):
        chance_heads = int(input("Enter percent for coin to flip heads -->  %"))
        chance_tails = 100 - chance_heads
        print(f"Chance of Heads: {chance_heads}%\tChance of Tails: {chance_tails}%")

    for flip in range(flips):
        randInt = random.randint(0, 100)
        if randInt < chance_heads:
            count_heads += 1
            flip_list_heads.append(1 + flip_list_heads[flip])
            flip_list_tails.append(flip_list_tails[flip])
        else:
            count_tails += 1
            flip_list_heads.append(flip_list_heads[flip])
            flip_list_tails.append(1 + flip_list_tails[flip])
        diff_heads_tails.append(flip_list_heads[flip] - flip_list_tails[flip])
    print(len(flip_list_heads))
    print(len(flip_list_tails))
    print(f"Total Head Count: {count_heads} out of {flips} flips ({100 * float(count_heads) / flips})%.\nTotal Tails Count: {count_tails} out of {flips} flips ({100 * float(count_tails) / flips})%")
    plt.plot(range(0,flips + 1), flip_list_heads, label = "# of Heads")
    plt.plot(range(0,flips + 1), flip_list_tails, label = "# of Tails")
    plt.plot(range(0,flips+1), diff_heads_tails, label = "# of more heads than tails")
    plt.xlabel("Roll #")
    plt.ylabel("Outcome Count")
    plt.legend()

if __name__ == '__main__':
    main()