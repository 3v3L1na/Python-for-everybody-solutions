def computegrade (temp_score):
     if 0.0 <= temp_score <= 1.0:
        if temp_score >= 0.9:
            return 'A'
        if temp_score>=0.8:
            return 'B'
        if temp_score>=0.7:
           return 'C'
        if temp_score>=0.6:
           return 'D'
        if temp_score<0.6:
            return 'F'
        
            return 'Bad score'
           

    
