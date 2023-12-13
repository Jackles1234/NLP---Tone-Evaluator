from transformers import pipeline
def to_string(sig_words, other_sig_words, emotion):
    sig_string = ("Most Promient Emotion: " +  str(emotion) + "\nWords that Determined this: " +  str(sig_words))
    o_sig_string = ""
    temp1 = "Other significant words: \n"
    temp2 = ""
    for i in other_sig_words:
        temp2 = temp2 + str(i) + "\n"
    o_sig_string = temp1 + temp2
    return sig_string, o_sig_string



def classifier(input):
    classifier2 = pipeline("sentiment-analysis", model="SamLowe/roberta-base-go_emotions")

    #text = "I hope you are doing well. My name is Jack Welsh and I am the President of the Weightlifting in Fitness Club. Our hours for the athlete's gym start tomorrow, and I was wondering if you had the 2023-2024 waivers to use the athlete's gym. I plan on sending the link out to our members, so they aren't all trying to sign-up at the same time tomorrow."
    #ext2 = "I hope you are doing well. Unfortunately, our club advisor, Kevin Carlson, has stopped teaching here at Drake. We have found a new advisor for this year, and I plan to get all the necessary signatures from our new advisor and make sure he is on board.  However, when I was registering for the club last semester, I put down Keving Carlson as the advisor for this year. Is there a way I can make this amendment in the club registration or will just getting the necessary paperwork be enough."
    #text3 = "I hope you are doing well. Unfortunately, I will need to leave your class around 4:15 to help setup for the activities fair. I will obviously review the Panopto video, as well as any things I have missed on Collab. I apologize for my inconsistency with the class this first week and I appreciate your understanding. This behavior will not be consistent with the rest of the semester. Thanks"

    classiefied = classifier2(input)

    text3_split = input.split()
    sig_words = []
    other_sig_words = []
    for i in text3_split:
        temp_class = classifier2(i)
        if temp_class[0]['label'] == classiefied[0]['label']:
            sig_words.append(i)
        elif(temp_class[0]['label'] != 'neutral'):
            other_sig_words.append({i : temp_class[0]['label']})
            

    sig_string, o_sig_string = to_string(sig_words, other_sig_words, classiefied[0]['label'])
    return sig_string, o_sig_string

