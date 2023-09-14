input()
votes = list(map(int , input().split(' ')))

need_to_buy = 0
zeos_votes = votes.pop(0)
votes.sort(reverse=True)
votes.append(-1)

for votes_of_each_god in votes.copy():
    if votes_of_each_god >= zeos_votes:
        tmp = ((votes_of_each_god - zeos_votes)//2) + 1
        zeos_votes += tmp
        need_to_buy += tmp

    votes.pop(0)
    if zeos_votes > votes[0]:
        break

print(need_to_buy)

