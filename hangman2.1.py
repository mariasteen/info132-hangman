def correct_guess(solution, attemps,proposal):
    right_guess =""
    proposal= input("Write a input here")

    #Tenkte å sjekke anagramma om det du har gjetta er samme som solution
    if sorted(right_guess) == sorted(solution):
        print("you win")

    else:
    #Viss lengda på antall bokstaver du har gjetta er lengre enn hemmelige ordet
        if len(attemps) > len(solution):
            print("sorry you loose")
            return
        else:
            #Her sjekker den om brukeren kun taster inn 1 bokstav.
            if len(proposal)> 0 and len(proposal)<2:

                #Viss bokstaven er allerede gjetta
                if proposal in attemps:
                    print(proposal,"dette har du prøvd før, du har", len(attemps),"igjen")
                    #Legger til ein inkrement på lenge på gjetta bokstaver (for å avslutte loop)
                    attemps = attemps + proposal
                    correct_guess(solution,attemps,proposal)
                    return None
                else:

                    #Viss det er riktig bokstav i ordet og ikkje gjetta fra før av
                    if proposal in solution:
                        #legger til i ein string av riktige bokstaver
                        right_guess = right_guess + proposal
                        #Legger til i lista allerede gjetta bokstaver
                        attemps = attemps + proposal
                        print (right_guess , "dette er riktig")
                        print("dette har du prøv",attemps)
                        print(count)
                        correct_guess(solution,attemps,proposal)
                        return True

                    #Viss bokstaven er heilt feil
                    elif proposal not in solution:
                        attemps = attemps + proposal
                        print (proposal, "finnes ikkje i ordet")
                        print("detta har du prøvd no", attemps)
                        print(count)
                        correct_guess(solution,attemps,proposal)
                        return False
                    
            #viss brukeren skriver inn fleire enn 1 bokstav        
            else:
                print("Skriv inn ein bokstav")
                correct_guess(solution,attemps,proposal)
                return None

#Kjører funksjonen
def main():
    correct_guess("hei","",">")
    
    
if __name__ == "__main__":
    main()
