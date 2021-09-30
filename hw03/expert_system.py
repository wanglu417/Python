# define my_function() function to ask user what their symptoms are and take input from the user
def my_function():
    user_aching = input(
        "Do you have aching bones or aching joints?(yes or no)"+'\n').lower()
    if user_aching == 'yes':  # user has aching bones or aching joints
        print("Possibilities include viral infection.")
    else:  # user does not have aching bones or aching joints
        user_rash = input("Do you have a rash?(yes or no)"+'\n').lower()
        if user_rash == 'yes':  # user has a rash, but still cannot diagnose
            print("Insufficient information to list possibilities.")
        else:  # user does not have a rash
            user_sore_throut = input(
                "Do you have a sore throut?(yes or no)"+'\n').lower()
            if user_sore_throut == 'yes':  # user has sore throut may have a throut infection
                print("Possibilities include a throut infection.")
            else:  # user does not have sore throut
                user_backpain = input(
                    "Do you have back pain just above the waist with chills and fever?(yes or no)"+'\n').lower()
                if user_backpain == 'yes':  # user has back pain may have kidney infection
                    print("Possibilities include kidney infection.")
                else:  # user does not have back pain
                    user_pain_urinating = input(
                        "Do you have pain urinating or are urinating more often?(yes or no)"+'\n').lower()
                    if user_pain_urinating == 'yes':  # user has pain urinating may have a urinary tract infection
                        print("Possibilities include a urinary tract infection.")
                    else:  # user does not have pain urinating
                        user_sun = input(
                            "Have you spent the day in the sun or in hot conditions?(yes or no)"+'\n').lower()
                        if user_sun == 'yes':  # user spents the day in the sun or in hot conditions may have sunstroke or heat exhaustion
                            print("Possibilities sunstroke or heat exhaustion.")
                        else:  # users does not spend the day in the sun, the system cannot diagnose
                            print("Insufficient information to list possibilities.")


user_coughing = input("Are you coughing? (yes or no)"+'\n').lower()

if user_coughing == 'yes':
    user_breath = input(
        "Are you short of breath or wheezing or coughing up phlegm?(yes or no)" + '\n').lower()
    if user_breath == 'yes':  # user is short of breath may have pneunomia or infection of airways
        print("Possibilities include pneumonia or infection of airways.")
    else:
        user_headache = input("Do you have a headache?(yes or no)"+'\n')
        if user_headache == 'yes':  # user has a headache may have viral infection
            print("Possibilities include viral infection.")
        # if user types "no",run the my_function() function
        else:
            my_function()

else:
    user_headache = input("Do you have a headache?(yes or no)" + '\n').lower()
    if user_headache == 'yes':
        user_pain_nausea = input('''Are you experiencing any of the following:pain when bending your head forward, nausea or vomiting,
bright light hurting your eyes,drowsiness or confusion?(yes or no)'''+'\n').lower()
        if user_pain_nausea == 'yes':  # user experiences the above may have menigitis
            print("Possibilities include menigitis.")
        else:
            user_vomiting = input(
                "Are you vomiting or had diarrhea?(yes or no)"+'\n').lower()
            if user_vomiting == 'yes':  # user who experiences the above may have digestive tract infection
                print("Possibilities include digestive tract infection.")
            else:
                my_function()
    # if user types "no",run the my_function() function
    else:
        my_function()
