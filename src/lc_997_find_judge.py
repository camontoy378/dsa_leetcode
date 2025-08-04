class FindJudge():

    def __init__(self, n, trust):
        self.n      = n
        self.trust  = trust

    def solve(self):

        person_status_list  = ["u"] * (self.n + 1)

        judge_set        = set()
        judge_dict       = {}

        if self.n == 1:
            return self.n

        for item in self.trust:

            person  = item[0]
            judge   = item[1]
                
            #Determine how many people trust the judge
            if judge not in judge_dict:
                judge_dict[judge] = 1
            else:
                judge_dict[judge] += 1

            #States:
            #u(undetermined status)-> p(person) -x j(Established person cannot be judge. Skip this state)-> n (Definetely Not the judge)
            #u(undetermined status)-> j(judge)  -> n (Definetely Not the judge)

            if person_status_list[judge] == "u":

                person_status_list[judge] = "j"
                judge_set.add(judge)

            if person_status_list[person] == "j":

                person_status_list[person] = "n"
                judge_set.remove(person)

            if person_status_list[person] == "u":
                person_status_list[person] = "p"

            if person_status_list[judge] == "p":

                person_status_list[judge] = "n"
                judge_dict[judge] -= 1

        if len(judge_set) != 1:
            return -1
        
        found_judge = judge_set.pop()

        #Does everyone trust the judge?
        if judge_dict[found_judge] != (self.n - 1):
            return -1

        else:
            return found_judge