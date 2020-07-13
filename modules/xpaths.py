

def get_xpaths():
    
    xpaths = {

    #username
        "username" : "txtLogin",
        "password" : "txtPassword",

        "sign_in_btn" : "#loginform > div:nth-child(4) > button:nth-child(2)",

        "swap_driver_1" : "player-slot__header",
        "next_1" : """.//div[text()='Next'] """,
        "done" :   """.//div[text()='Done'] """,

        "x" : "/html/body/div[9]/div/div/aside/header/button/div[2]",

        "expose_list" : """/html/body/main/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/header/div[1]/button[2]/div[1]""",


        """driver_card""": """lineup-picker__card__body""",
    }
    return xpaths



