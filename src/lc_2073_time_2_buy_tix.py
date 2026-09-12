class TimeToBuyTix():

    def __init__(self):
        pass

    def solve(self, tickets, k):

        counter     = index = 0
        

        while (len(tickets) > 0):

            modulo_num  = len(tickets)
            #i = counter % modulo_num
            i = index % modulo_num

            tickets[i] -= 1

            if ( tickets[i] == 0):

                tickets.pop(i)

                if (i == k):
                    print(f"DEBUG: k = {k}")
                    return counter + 1

                if (i < k):
                    k -= 1

                #Reset index
                index = i - 1

            counter += 1
            index += 1

            pass

        return counter
