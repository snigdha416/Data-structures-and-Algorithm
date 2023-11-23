class Solution:
    def numRescueBoats(self, people, limit):
        size = len(people)
        people.sort()
        boats = 0
        i = 0
        j = size - 1
        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
            boats += 1
        return boats
        
