

def get_xpaths():
    
    xpaths = {

    #create account page
    """title""" : """//*[@id="Title-input"]""",
    """first_name""" : """//*[@id="FirstName-input"]""",
    """last_name""" : """//*[@id="LastName-input"]""",
    """dob_field""" : """//*[@id="BirthDate-input"]""",
    """country_of_residence""" : """//*[@id="Country-input"]""",
    """email_address""" : """//*[@id="Email-input"]""",
    """password_field""" : """//*[@id="Password-input"]""",
    """confirm_password_field""" : """//*[@id="ConfirmPassword-input"]""",
    """register_btn""" : """/html/body/div[2]/main/div/div[5]/div/div[2]/div/div/div/div/div/div/div/div[2]/div[12]/div/div/div[1]/a""",



    #landing page
    """add_driver""" : """// *[ @ id = "ember295"]""",
    """add_driver_alt""": """// *[ @ id = "ember296"]""",
    """add_driver_class""" : """player-slot__header__icon""",



    #Driver select
    """driver_card""" : """lineup-picker__card__body""",


    #Constructor Select
    """driver_next""" : """lineup-picker__sidebar__next-button""",


    #Turbo driver
    """turbo_driver""" : """player-slot__checkbox""",
    """turbo_next""" : """modal__footer__use-action""",

    #fav team
    """fav_team""" : """teams-favourite-picker__list__row--value-1""",
    """fav_team_next""" : """modal__footer__use-action"""
    }
    return xpaths



