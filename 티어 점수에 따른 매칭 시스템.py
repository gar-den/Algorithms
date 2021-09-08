"""
티어 점수에 따른 매칭 시스템
"""

def matchingCount(users, n):
    allowedTierScores = [0]
    matchingGroups = [[users[0]]]

    matching = 0
    
    i = 1
    while i < len(users):
        j = 0
        deleted = False
        
        while j < len(matchingGroups):
            if matchingGroups[j][0] - allowedTierScores[j] <= users[i] <= matchingGroups[j][0] + allowedTierScores[j]:
                # if new user is matched to the group
                matchingGroups[j].append(users[i])

                if len(matchingGroups[j]) == n:  # matched users are enough in group
                    del allowedTierScores[j]
                    del matchingGroups[j]

                    deleted  = True
                    matching += 1

                break
            
            elif allowedTierScores[j] < 24:
                allowedTierScores[j] += 2
            
            j += 1

        if j == len(matchingGroups):  # if not matched, make new group
            matchingGroups.append([users[i]])
            allowedTierScores.append(0)

        if deleted:  # add rest of allow tier scores
            for k in range(j, len(allowedTierScores)):
                if allowedTierScores[k] < 24:
                    allowedTierScores[k] += 2
        else:
            for k in range(j + 1, len(allowedTierScores)):
                if allowedTierScores[k] < 24:
                    allowedTierScores[k] += 2

        i += 1
        

    return matching


users = [0,5,11,7,13,22,14,19,25,22] 
n = 3

print(matchingCount(users, n))  # has to be 2


users = [11,6,6,13,23,33,19,18,19,5]
n = 3

print(matchingCount(users, n))  # has to be 3, but the result is 2.

users = [0,5,11,7,13,22,14,19,25,22]
n = 2

print(matchingCount(users, n))  # has to be 4
