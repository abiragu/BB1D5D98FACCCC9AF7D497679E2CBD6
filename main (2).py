class Player:
  def play(self):
    print("The player is playing cricket.")
    class Batsman(Player):
      def play(self):
        print("The bowler is bowling.")
        #Creating objects of Batsman and bowler classes 
        batsman=Batsman()
        bowler=Bowler()
        #Calling the play()method for each object
        batsman.play()
        bowler.play()