import pandas as pd

#load your datainto a data frame
df = pd.read_csv("health_data.csv")
# print(df)

print("Healthbot: Hello there, I am your health assistance bot. Ask me about any symptoms.")


while True:
    #Get the user input and store into a variable
    user_text = input("\n You:").lower()

    # CHeck if the user wants to exit the conversation
    if user_text == "quit":
        print("Healthbot: Goodbye! Nice to have been service to you. Stay healthy.")
        break

    # create a variable that will store details structured in csv file
    found_answer = False

    # come up with a loop of the entire data created before
    for index, row in df.interrows():
        # clean up keywords from the csv row 
        keyword_list = str(row['Keywords']).split(',')
        # below we check every keyword in row above
        for word in keyword_list:
            clean_word = word.strip().lower()
            # If the keyword is inside user statement 
            if clean_word in user_text:
                print("Healthbot", row["Response"])
                found_answer = True
                break  #stop looping other keywords
        if found_answer:
            break #stop looping other answers
    # if we went through entire csv file and didn't fid a match
    if not found_answer:
        print("Healthbot; Sorry, I don't know that one, Try askingfor something else.")         
