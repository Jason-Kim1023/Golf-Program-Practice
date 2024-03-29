import tkinter as tk
import tkinter.messagebox
import sqlite3

root = tk.Tk()
root.geometry("1920x1080")
root["bg"] = "lightGreen"
root.title("Golf Pro")

conn = sqlite3.connect("User Information.db")
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS user_information (
    username,
    password
    )""")

conn.commit()
conn.close()


#CREATE AN ACCOUNT WINDOW
def createAcc():
    #Defining window settings for the app
    createAccWindow = tk.Toplevel() 
    createAccWindow.title ("Creating an Account")
    createAccWindow.geometry("1920x1080")
    createAccWindow["bg"] = "lightGreen"
    closeBtn = tk.Button (createAccWindow, text = "Close", font = ('Courier', 40), padx = 50, pady = 10, borderwidth = 1, command = createAccWindow.destroy)
    closeBtn.place (x = 300, y = 750)

    def submit():
        #creating a database for golf events for each user created
        conn = sqlite3.connect(newusernameTxt.get() + "golfevent" + ".db")
        c = conn.cursor()

        c.execute("""CREATE TABLE golfeventdata (
            month INTEGER,
            day INTEGER,
            year INTEGER,
            time TEXT,
            ampm TEXT,
            player1 TEXT,
            player2 TEXT,
            player3 TEXT,
            player4 TEXT,
            numberofholes INTEGER
        )""")

        conn.commit()
        conn.close()

        #creating a database for costs for each user created
        conn = sqlite3.connect(newusernameTxt.get() + "costs" + ".db")
        c = conn.cursor()

        c.execute("""CREATE TABLE costsdata (
            monthC INTEGER,
            dayC INTEGER,
            yearC INTEGER,
            cost REAL
        )""")

        conn.commit()
        conn.close()

        #creating a database for scores for each user created
        conn = sqlite3.connect(newusernameTxt.get() + "scores" + ".db")
        c = conn.cursor()

        c.execute("""CREATE TABLE scoresdata (
            monthS INTEGER,
            dayS INTEGER,
            yearS INTEGER,
            par INTEGER,
            strokes INTEGER,
            handicap INTEGER
        )""")

        conn.commit()
        conn.close()


        conn = sqlite3.connect ('User Information.db')
        c = conn.cursor()

        c.execute("INSERT INTO user_information VALUES (:u, :p)", 
                {
                    'u': newusernameTxt.get(),
                    'p': newpasswordTxt.get()
                })

        newusernameTxt.delete(0, 500)
        newpasswordTxt.delete(0, 500)

        conn.commit()
        conn.close


    #def query():  This is for testing purposes

        #conn = sqlite3.connect ('User Information.db')
        #c = conn.cursor()

        #c.execute("SELECT *, oid FROM user_information")
        #records = c.fetchall()
        #print(records)

        #conn.commit()
        #conn.close

    #Labels
    createLabel = tk.Label (createAccWindow, text = "Create an Account!", font = ('Courier', 75))
    uLabel = tk.Label (createAccWindow, text = "Username:", font = ('Courier', 50))
    pLabel = tk.Label (createAccWindow, text = "Password:", font = ('Courier', 50))
        

    #Btns
    createBtn = tk.Button (createAccWindow, text = "Create", font = ('Courier', 40), padx = 50, pady = 10, borderwidth = 1, command = submit)
    #q = tk.Button (createAccWindow, text = "test", padx = 40, pady = 50, command = query)

    #Text boxes to enter
    newusernameTxt = tk.Entry (createAccWindow, font = ('Courier', 50), width = 30)
    newpasswordTxt = tk.Entry (createAccWindow, font = ('Courier', 50), width = 30)

    #Positioning
    newusernameTxt.place (x = 500, y = 300)
    newpasswordTxt.place (x = 500, y = 500)
    createLabel.place (x = 400, y = 50)
    uLabel.place (x = 100, y = 300)
    pLabel.place (x = 100, y = 500)
    createBtn.place (x = 810, y = 750)
    #q.place (x = 400, y = 500)


#MAIN SCREEN WINDOW
def mainScreen():
    #Defining window settings for the app
    mainscreenWindow = tk.Toplevel() 
    mainscreenWindow.title ("Dashboard")
    mainscreenWindow.geometry("1920x1080")
    mainscreenWindow["bg"] = "lightGreen"

    #Labels
    headingLabel = tk.Label (mainscreenWindow, text = "GOLF ORGANIZER", font = ('Courier', 75))
            

    #Buttons
    costSummary = tk.Button (mainscreenWindow, text = "Cost Summary", font = ('Courier', 50), padx = 150, pady = 50, borderwidth = 1, command = costsSummary)
    scoreSummary = tk.Button (mainscreenWindow, text = "Score Summary", font = ('Courier', 50), padx = 150, pady = 50, borderwidth = 1, command = scoresSummary)
    schedule = tk.Button (mainscreenWindow, text = "Schedule", font = ('Courier', 50), padx = 250, pady = 50, borderwidth = 1, command = Schedule)
    newGolf = tk.Button (mainscreenWindow, text = "Add New Golf Event", font = ('Courier', 20), padx = 265, pady = 5, borderwidth = 1, command = addnewgolfEvent)
    newCost = tk.Button (mainscreenWindow, text = "Add New Cost", font = ('Courier', 20), padx = 313, pady = 5, borderwidth = 1, command = addnewCost)
    newScore = tk.Button (mainscreenWindow, text = "Add New Score", font = ('Courier', 20), padx = 305, pady = 5, borderwidth = 1, command = addnewScore)
       
    #Positioning
    costSummary.place (x = 30, y = 275)
    scoreSummary.place (x = 1010, y = 275)
    schedule.place (x = 1010, y = 600)
    newGolf.place (x = 30, y = 600)
    newCost.place (x = 30, y = 680)
    newScore.place (x = 30, y = 760)
    headingLabel.place (x = 515, y = 50)


def login():
    while True:
        usernamecheck = usernameTxt.get()
        passwordcheck = passwordTxt.get()
        
        with sqlite3.connect("User Information.db") as db:
            cursor = db.cursor()
        
        find_user = ("SELECT * FROM user_information WHERE username = ? AND password = ?")
        cursor.execute(find_user, [(usernamecheck), (passwordcheck)])
        results = cursor.fetchall()

        if results:
            for i in results:
                mainScreen()
            break
        else: 
            print("wrong")
            break

#Labels
loginLabel = tk.Label (root, text = "Login Page", font = ('Courier', 75))
uLabel = tk.Label (root, text = "Username:", font = ('Courier', 50))
pLabel = tk.Label (root, text = "Password:", font = ('Courier', 50))
        
#Label positioning
loginLabel.place (x = 653, y = 50)
uLabel.place (x = 100, y = 250)
pLabel.place (x = 100, y = 500)

#Text boxes
usernameTxt = tk.Entry (root, font = ('Courier', 50), width = 30)
passwordTxt = tk.Entry (root, font = ('Courier', 50), width = 30, show = '*')

#Text boxes positioning
usernameTxt.place (x = 500, y = 250)
passwordTxt.place (x = 500, y = 500)   

#Btns
enterBtn = tk.Button (root, text = "Enter", font = ('Courier', 40), padx = 50, pady = 10, borderwidth = 1, command = login)
createaccBtn = tk.Button (root, text = "create an account", font = ('Courier', 10), fg = 'red', padx = 44, pady = 10, borderwidth = 1, command = createAcc)

#Btn positioning
enterBtn.place (x = 810, y = 750)
createaccBtn.place (x = 500, y = 350)

#ADDING A GOLF EVENT WINDOW
def addnewgolfEvent():
    #Defining window settings for the app
    addingnewgolfWindow = tk.Toplevel() 
    addingnewgolfWindow.title ("Add a New Event")
    addingnewgolfWindow.geometry("1920x1080")
    addingnewgolfWindow["bg"] = "lightGreen"

    def addingeventDatabase():
        conn = sqlite3.connect (usernameTxt.get() + "golfevent" + ".db")
        c = conn.cursor()

        c.execute("INSERT INTO golfeventdata VALUES (:month, :day, :year, :time, :ampm, :player1, :player2, :player3, :player4, :numberofholes)", 
                {
                    "month": monthTxt.get(),
                    "day": dayTxt.get(),
                    "year": yearTxt.get(),
                    "time": timeTxt.get(),
                    "ampm": ampmTxt.get(),
                    "player1": playerOne.get(),
                    "player2": playerTwo.get(),
                    "player3": playerThree.get(),
                    "player4": playerFour.get(),
                    "numberofholes": holesTxt.get()
                })

        monthTxt.delete(0, 500)
        dayTxt.delete(0, 500)
        yearTxt.delete(0, 500)
        timeTxt.delete(0, 500)
        ampmTxt.delete(0, 500)
        playerOne.delete(0, 500)
        playerTwo.delete(0, 500)
        playerThree.delete(0, 500)
        playerFour.delete(0, 500)
        holesTxt.delete(0,500)

        conn.commit()
        conn.close
    
    #def query(): This is for testing purposes  

        #conn = sqlite3.connect (usernameTxt.get() + "golfevent" + ".db")
        #c = conn.cursor()

        #c.execute("SELECT *, oid FROM golfeventdata")
        #records = c.fetchall()
        #print(records)

        #conn.commit()
        #conn.close

    #Labels
    addnewLabel = tkinter.Label (addingnewgolfWindow, text = "Add a New Golfing Event!", font = ('Courier', 75))

    dateLabel = tkinter.Label (addingnewgolfWindow, text = "Date:", font = ('Courier', 50))
    monthLabel = tkinter.Label (addingnewgolfWindow, text = "Month (number)", font = ('Courier', 10))
    dayLabel = tkinter.Label (addingnewgolfWindow, text = "Day (number)", font = ('Courier', 10))
    yearLabel = tkinter.Label (addingnewgolfWindow, text = "Year (XXXX)", font = ('Courier', 10))

    timetitleLabel = tkinter.Label (addingnewgolfWindow, text = "Time:", font = ('Courier', 50))
    timeLabel = tkinter.Label (addingnewgolfWindow, text = "(XX:XX or X:XX)", font = ('Courier', 10))
    ampmLabel = tkinter.Label (addingnewgolfWindow, text = "AM or PM", font = ('Courier', 10))

    playersLabel = tkinter.Label (addingnewgolfWindow, text = "Players:", font = ('Courier', 50))
    playeroneLabel = tkinter.Label (addingnewgolfWindow, text = "Player One First Name", font = ('Courier', 10))
    playertwoLabel = tkinter.Label (addingnewgolfWindow, text = "Player Two First Name", font = ('Courier', 10))
    playerthreeLabel = tkinter.Label (addingnewgolfWindow, text = "Player Three First Name", font = ('Courier', 10))
    playerfourLabel = tkinter.Label (addingnewgolfWindow, text = "Player Four First Name", font = ('Courier', 10))

    holesLabel = tkinter.Label (addingnewgolfWindow, text = "# of Holes:", font = ('Courier', 50))

    #Text boxes to enter
    monthTxt = tkinter.Entry (addingnewgolfWindow, font = ('Courier', 50), width = 10)
    dayTxt = tkinter.Entry (addingnewgolfWindow, font = ('Courier', 50), width = 10)
    yearTxt = tkinter.Entry (addingnewgolfWindow, font = ('Courier', 50), width = 10)

    timeTxt = tkinter.Entry (addingnewgolfWindow, font = ('Courier', 50), width = 10)
    ampmTxt = tkinter.Entry (addingnewgolfWindow, font = ('Courier', 50), width = 3)

    playerOne = tkinter.Entry (addingnewgolfWindow, font = ('Courier', 50), width = 8)
    playerTwo = tkinter.Entry (addingnewgolfWindow, font = ('Courier', 50), width = 8)
    playerThree = tkinter.Entry (addingnewgolfWindow, font = ('Courier', 50), width = 8)
    playerFour = tkinter.Entry (addingnewgolfWindow, font = ('Courier', 50), width = 8)

    holesTxt = tkinter.Entry (addingnewgolfWindow, font = ('Courier', 50), width = 3)

    #Buttons
    addBtn = tkinter.Button (addingnewgolfWindow, text = "Add", font = ('Courier', 30), padx = 50, pady = 3, borderwidth = 1, command = addingeventDatabase)
    backBtn = tkinter.Button (addingnewgolfWindow, text = "Back", font = ('Courier', 30), padx = 50, pady = 3, borderwidth = 1, command = addingnewgolfWindow.destroy)
    #q = tk.Button (addingnewgolfWindow, text = "test", padx = 40, pady = 50, command = query) For testing purposes

    #Positioning
    addnewLabel.place (x = 225, y = 50)
    dateLabel.place (x = 100, y = 300)
    timetitleLabel.place (x = 100, y = 450)
    playersLabel.place (x = 100, y = 600)
    holesLabel.place (x = 100, y = 750)

    monthTxt.place (x = 400, y = 300)
    monthLabel.place (x = 540, y = 275)
    dayTxt.place (x = 900, y = 300)
    dayLabel. place (x = 1050, y = 275)
    yearTxt.place (x = 1400, y = 300)
    yearLabel.place (x = 1550, y = 275)

    timeTxt.place (x = 400, y = 450)
    timeLabel.place (x = 540, y = 425)
    ampmTxt.place (x = 900, y = 450)
    ampmLabel.place (x = 930, y = 425)

    playerOne.place (x = 450, y = 600)
    playeroneLabel.place (x = 525, y = 575)
    playerTwo.place (x = 800, y = 600)
    playertwoLabel.place (x = 875, y = 575)
    playerThree.place (x = 1150, y = 600)
    playerthreeLabel.place (x = 1215, y = 575)
    playerFour.place (x = 1500, y = 600)
    playerfourLabel.place (x = 1575, y = 575)

    addBtn.place (x = 510, y = 900)
    backBtn.place (x = 1100, y = 900)

    holesTxt.place (x = 600, y = 750)
    #q.place (x = 400, y = 500) For testing purposes

#ADDING NEW COST WINDOW
def addnewCost():
    #Defining window settings for the app
    addingnewcostWindow = tk.Toplevel() 
    addingnewcostWindow.title ("Add a New Cost")
    addingnewcostWindow.geometry("1920x1080")
    addingnewcostWindow["bg"] = "lightGreen"

    def addingcostDatabase():
        conn = sqlite3.connect (usernameTxt.get() + "costs" + ".db")
        c = conn.cursor()
        
        c.execute("INSERT INTO costsdata VALUES (:monthC, :dayC, :yearC, :cost)", 
                {
                    "monthC": monthTxt.get(),
                    "dayC": dayTxt.get(),
                    "yearC": yearTxt.get(),
                    "cost": costTxt.get(),
                })

        monthTxt.delete(0, 500)
        dayTxt.delete(0, 500)
        yearTxt.delete(0, 500)
        costTxt.delete(0, 500)

        conn.commit()
        conn.close

    
    #def query(): This is for testing purposes
        #conn = sqlite3.connect (usernameTxt.get() + "costs" + ".db")
        #c = conn.cursor()

        #c.execute("SELECT *, oid FROM costsdata")
        #records = c.fetchall()
        #print(records)

        #conn.commit()
        #conn.close
    
    #Labels
    addnewLabel = tkinter.Label (addingnewcostWindow, text = "Add a New Cost!", font = ('Courier', 75))

    dateLabel = tkinter.Label (addingnewcostWindow, text = "Date:", font = ('Courier', 50))
    monthLabel = tkinter.Label (addingnewcostWindow, text = "Month (number)", font = ('Courier', 10))
    dayLabel = tkinter.Label (addingnewcostWindow, text = "Day (number)", font = ('Courier', 10))
    yearLabel = tkinter.Label (addingnewcostWindow, text = "Year (XXXX)", font = ('Courier', 10))

    costLabel = tkinter.Label (addingnewcostWindow, text = "Cost:", font = ('Courier', 50))
    costdescriptionLabel = tkinter.Label (addingnewcostWindow, text = "X.XX, XX.XX, XXX.XX", font = ('Courier', 10))


    #Text boxes to enter
    monthTxt = tkinter.Entry (addingnewcostWindow, font = ('Courier', 50), width = 10)
    dayTxt = tkinter.Entry (addingnewcostWindow, font = ('Courier', 50), width = 10)
    yearTxt = tkinter.Entry (addingnewcostWindow, font = ('Courier', 50), width = 10)
    costTxt = tkinter.Entry (addingnewcostWindow, font = ('Courier', 50), width = 10)


    #Buttons
    addBtn = tkinter.Button (addingnewcostWindow, text = "Add", font = ('Courier', 30), padx = 50, pady = 3, borderwidth = 1, command = addingcostDatabase)
    backBtn = tkinter.Button (addingnewcostWindow, text = "Back", font = ('Courier', 30), padx = 50, pady = 3, borderwidth = 1, command = addingnewcostWindow.destroy)
    #q = tk.Button (addingnewcostWindow, text = "test", padx = 40, pady = 50, command = query) For testing purposes

    #positioning
    addnewLabel.place (x = 500, y = 50)
    dateLabel.place (x = 100, y = 300)

    monthTxt.place (x = 400, y = 300)
    monthLabel.place (x = 540, y = 275)
    dayTxt.place (x = 900, y = 300)
    dayLabel. place (x = 1050, y = 275)
    yearTxt.place (x = 1400, y = 300)
    yearLabel.place (x = 1550, y = 275)

    addBtn.place (x = 510, y = 900)
    backBtn.place (x = 1100, y = 900)
    #q.place (x = 400, y = 500) For testing purposes

    costLabel.place (x = 100, y = 500)
    costTxt.place (x = 400, y = 500)
    costdescriptionLabel.place (x = 520, y = 474)


#ADDING NEW SCORE WINDOW
def addnewScore():
    #Defining window settings for the app
    addingnewscoreWindow = tk.Toplevel() 
    addingnewscoreWindow.title ("Add a New Score")
    addingnewscoreWindow.geometry("1920x1080")
    addingnewscoreWindow["bg"] = "lightGreen"

    def addingscoresDatabase():
        conn = sqlite3.connect (usernameTxt.get() + "scores" + ".db")
        c = conn.cursor()

        c.execute("INSERT INTO scoresdata VALUES (:monthS, :dayS, :yearS, :par, :strokes, :handicap)", 
                {
                    "monthS": monthTxt.get(),
                    "dayS": dayTxt.get(),
                    "yearS": yearTxt.get(),
                    "par": totalparTxt.get(),
                    "strokes": totalstrokesTxt.get(),
                    "handicap": handicapTxt.get()
                })

        monthTxt.delete(0, 500)
        dayTxt.delete(0, 500)
        yearTxt.delete(0, 500)
        totalparTxt.delete(0, 500)
        totalstrokesTxt.delete(0, 500)
        handicapTxt.delete(0, 500)

        conn.commit()
        conn.close

    #def query(): This is for testing purposes
        #conn = sqlite3.connect (usernameTxt.get() + "scores" + ".db")
        #c = conn.cursor()

        #c.execute("SELECT *, oid FROM scoresdata")
        #records = c.fetchall()
        #print(records)

        #conn.commit()
        #conn.close

    #Label
    addnewLabel = tkinter.Label (addingnewscoreWindow, text = "Add a New Score!", font = ('Courier', 75))
    totalparLabel = tkinter.Label (addingnewscoreWindow, text = "Total Par of Course:", font = ('Courier', 50))
    totalstrokesLabel = tkinter.Label (addingnewscoreWindow, text = "Total Strokes:", font = ('Courier', 50))
    handicapLabel = tkinter.Label (addingnewscoreWindow, text = "Handicap:", font = ('Courier', 50))
    dateLabel = tkinter.Label (addingnewscoreWindow, text = "Date:", font = ('Courier', 50))
    monthLabel = tkinter.Label (addingnewscoreWindow, text = "Month (number)", font = ('Courier', 10))
    dayLabel = tkinter.Label (addingnewscoreWindow, text = "Day (number)", font = ('Courier', 10))
    yearLabel = tkinter.Label (addingnewscoreWindow, text = "Year (XXXX)", font = ('Courier', 10))

    #text boxes to enter
    totalparTxt = tkinter.Entry (addingnewscoreWindow, font = ('Courier', 50), width = 10)
    totalstrokesTxt = tkinter.Entry (addingnewscoreWindow, font = ('Courier', 50), width = 10)
    handicapTxt = tkinter.Entry (addingnewscoreWindow, font = ('Courier', 50), width = 10)
    monthTxt = tkinter.Entry (addingnewscoreWindow, font = ('Courier', 50), width = 10)
    dayTxt = tkinter.Entry (addingnewscoreWindow, font = ('Courier', 50), width = 10)
    yearTxt = tkinter.Entry (addingnewscoreWindow, font = ('Courier', 50), width = 10)

    #Buttton
    addBtn = tkinter.Button (addingnewscoreWindow, text = "Add", font = ('Courier', 30), padx = 50, pady = 3, borderwidth = 1, command = addingscoresDatabase)
    backBtn = tkinter.Button (addingnewscoreWindow, text = "Back", font = ('Courier', 30), padx = 50, pady = 3, borderwidth = 1, command = addingnewscoreWindow.destroy)
    #q = tk.Button (addingnewscoreWindow, text = "test", padx = 40, pady = 50, command = query) For testing purposes

    #positioning
    addnewLabel.pack()
    totalparLabel.place (x = 100, y = 450)
    totalparTxt.place (x = 1000, y = 450)
    totalstrokesLabel.place (x = 100, y = 600)
    totalstrokesTxt.place (x = 760, y = 600)
    handicapLabel.place (x = 100, y = 750)
    handicapTxt.place (x = 560, y = 750)
    dateLabel.place (x = 100, y = 300)
    monthTxt.place (x = 400, y = 300)
    monthLabel.place (x = 540, y = 275)
    dayTxt.place (x = 900, y = 300)
    dayLabel. place (x = 1050, y = 275)
    yearTxt.place (x = 1400, y = 300)
    yearLabel.place (x = 1550, y = 275)
    addBtn.place (x = 510, y = 900)
    backBtn.place (x = 1100, y = 900)
    #q.place (x = 400, y = 500) For testing purposes

def Schedule():
    #Defining window settings for the app
    scheduleWindow = tk.Toplevel() 
    scheduleWindow.title ("Schedule")
    scheduleWindow.geometry("1920x1080")
    scheduleWindow["bg"] = "lightGreen"

    def editSchedule():
        global editscheduleWindow
        editscheduleWindow = tk.Toplevel() 
        editscheduleWindow.title ("Edit Schedule")
        editscheduleWindow.geometry("1920x1080")
        editscheduleWindow["bg"] = "lightGreen"

        def save():
            conn = sqlite3.connect (usernameTxt.get() + "golfevent" + ".db")
            c = conn.cursor()

            record_id = deleteTxt.get()
            c.execute("""UPDATE golfeventdata SET
                month = :m,
                day = :d,
                year = :y,
                time = :t,
                ampm = :ap,
                player1 = :p1,
                player2 = :p2,
                player3 = :p3,
                player4 = :p4,
                numberofholes = :noh

                WHERE oid = :oid""",
                {
                    "m": monthTxt_editor.get(),
                    "d": dayTxt_editor.get(),
                    "y": yearTxt_editor.get(),
                    "t": timeTxt_editor.get(),
                    "ap": ampmTxt_editor.get(),
                    "p1": playerOne_editor.get(),
                    "p2": playerTwo_editor.get(),
                    "p3": playerThree_editor.get(),
                    "p4": playerFour_editor.get(),
                    "noh": holesTxt_editor.get(),

                    "oid": record_id
                })

            conn.commit()
            conn.close

            editscheduleWindow.destroy()
        
        #connecting to database
        conn = sqlite3.connect (usernameTxt.get() + "golfevent" + ".db")
        c = conn.cursor()

        record_id = deleteTxt.get()
        c.execute("SELECT * FROM golfeventdata WHERE oid = " + record_id)
        records = c.fetchall()

        #Labels
        editLabel = tkinter.Label (editscheduleWindow, text = "Edit a Golfing Event!", font = ('Courier', 75))

        dateLabel = tkinter.Label (editscheduleWindow, text = "Date:", font = ('Courier', 50))
        monthLabel = tkinter.Label (editscheduleWindow, text = "Month (number)", font = ('Courier', 10))
        dayLabel = tkinter.Label (editscheduleWindow, text = "Day (number)", font = ('Courier', 10))
        yearLabel = tkinter.Label (editscheduleWindow, text = "Year (XXXX)", font = ('Courier', 10))

        timetitleLabel = tkinter.Label (editscheduleWindow, text = "Time:", font = ('Courier', 50))
        timeLabel = tkinter.Label (editscheduleWindow, text = "(XX:XX or X:XX)", font = ('Courier', 10))
        ampmLabel = tkinter.Label (editscheduleWindow, text = "AM or PM", font = ('Courier', 10))

        playersLabel = tkinter.Label (editscheduleWindow, text = "Players:", font = ('Courier', 50))
        playeroneLabel = tkinter.Label (editscheduleWindow, text = "Player One First Name", font = ('Courier', 10))
        playertwoLabel = tkinter.Label (editscheduleWindow, text = "Player Two First Name", font = ('Courier', 10))
        playerthreeLabel = tkinter.Label (editscheduleWindow, text = "Player Three First Name", font = ('Courier', 10))
        playerfourLabel = tkinter.Label (editscheduleWindow, text = "Player Four First Name", font = ('Courier', 10))

        holesLabel = tkinter.Label (editscheduleWindow, text = "# of Holes:", font = ('Courier', 50))

        #Text boxes to enter
        monthTxt_editor = tkinter.Entry (editscheduleWindow, font = ('Courier', 50), width = 10)
        dayTxt_editor = tkinter.Entry (editscheduleWindow, font = ('Courier', 50), width = 10)
        yearTxt_editor = tkinter.Entry (editscheduleWindow, font = ('Courier', 50), width = 10)

        timeTxt_editor = tkinter.Entry (editscheduleWindow, font = ('Courier', 50), width = 10)
        ampmTxt_editor = tkinter.Entry (editscheduleWindow, font = ('Courier', 50), width = 3)

        playerOne_editor = tkinter.Entry (editscheduleWindow, font = ('Courier', 50), width = 8)
        playerTwo_editor = tkinter.Entry (editscheduleWindow, font = ('Courier', 50), width = 8)
        playerThree_editor = tkinter.Entry (editscheduleWindow, font = ('Courier', 50), width = 8)
        playerFour_editor = tkinter.Entry (editscheduleWindow, font = ('Courier', 50), width = 8)

        holesTxt_editor = tkinter.Entry (editscheduleWindow, font = ('Courier', 50), width = 3)

        #Buttons
        saveBtn = tkinter.Button (editscheduleWindow, text = "Save", font = ('Courier', 30), padx = 50, pady = 3, borderwidth = 1, command = save)
        backBtn = tkinter.Button (editscheduleWindow, text = "Back", font = ('Courier', 30), padx = 50, pady = 3, borderwidth = 1, command = editscheduleWindow.destroy)
        

        #Positioning
        editLabel.place (x = 295, y = 50)
        dateLabel.place (x = 100, y = 300)
        timetitleLabel.place (x = 100, y = 450)
        playersLabel.place (x = 100, y = 600)
        holesLabel.place (x = 100, y = 750)

        monthTxt_editor.place (x = 400, y = 300)
        monthLabel.place (x = 540, y = 275)
        dayTxt_editor.place (x = 900, y = 300)
        dayLabel. place (x = 1050, y = 275)
        yearTxt_editor.place (x = 1400, y = 300)
        yearLabel.place (x = 1550, y = 275)

        timeTxt_editor.place (x = 400, y = 450)
        timeLabel.place (x = 540, y = 425)
        ampmTxt_editor.place (x = 900, y = 450)
        ampmLabel.place (x = 930, y = 425)

        playerOne_editor.place (x = 450, y = 600)
        playeroneLabel.place (x = 525, y = 575)
        playerTwo_editor.place (x = 800, y = 600)
        playertwoLabel.place (x = 875, y = 575)
        playerThree_editor.place (x = 1150, y = 600)
        playerthreeLabel.place (x = 1215, y = 575)
        playerFour_editor.place (x = 1500, y = 600)
        playerfourLabel.place (x = 1575, y = 575)

        saveBtn.place (x = 510, y = 900)
        backBtn.place (x = 1100, y = 900)

        holesTxt_editor.place (x = 600, y = 750)

        #looping through results
        for record in records:
            monthTxt_editor.insert(0, record[0])
            dayTxt_editor.insert(0, record[1])
            yearTxt_editor.insert(0, record[2])
            timeTxt_editor.insert(0, record[3])
            ampmTxt_editor.insert(0, record[4])
            playerOne_editor.insert(0, record[5])
            playerTwo_editor.insert(0, record[6])
            playerThree_editor.insert(0, record[7])
            playerFour_editor.insert(0, record[8])
            holesTxt_editor.insert(0, record[9])
        

    #For deleting a record
    def delete():
        conn = sqlite3.connect (usernameTxt.get() + "golfevent" + ".db")
        c = conn.cursor()

        c.execute("DELETE from golfeventdata WHERE oid = " + deleteTxt.get())

        deleteTxt.delete(0, 500)

        conn.commit()
        conn.close
    

    #for pulling the schedule from the database and putting it onto the screen
    def pullSchedule():

        conn = sqlite3.connect (usernameTxt.get() + "golfevent" + ".db")
        c = conn.cursor()

        c.execute("SELECT *, oid FROM golfeventdata")
        records = c.fetchall()
        
        print_records = ""
        for record in records:
                print_records += "#" + str(record [10]) + " " + str(record[0]) + "/" + str(record[1]) + "/" + str(record[2]) + " " + record[3] + record[4] + " " + record[5] + "," + record[6] + "," + record[7] + "," + record [8] + "\n"

        #label and position
        scheduleLbl = tk.Label (scheduleWindow, font = ('Courier', 30), bg = "lightGreen", text = print_records)
        scheduleLbl.place (x = 450, y = 100)

        conn.commit()
        conn.close

    #text box
    deleteTxt = tkinter.Entry (scheduleWindow, font = ('Courier', 45), width = 3)

    #button
    editBtn = tkinter.Button (scheduleWindow, text = "Edit Event #:", font = ('Courier', 10), padx = 38, pady = 2, borderwidth = 1, fg = "red", command = editSchedule)
    backBtn = tkinter.Button (scheduleWindow, text = "Back", font = ('Courier', 20), padx = 30, pady = 10, borderwidth = 1, command = scheduleWindow.destroy)
    pullScheduleBtn = tkinter.Button (scheduleWindow, text = "Check Schedule/Refresh:", font = ('Courier', 20), command = pullSchedule)
    deleteBtn = tkinter.Button (scheduleWindow, text = "Delete Event #:", font = ('Courier', 10), padx = 30, pady = 2, borderwidth = 1, fg = "red", command = delete)

    #positioning
    pullScheduleBtn.pack (pady = 20)
    editBtn.place (x = 50, y = 940)
    backBtn.place (x = 890, y = 900)
    deleteBtn.place (x = 50, y = 900)
    deleteTxt.place (x = 275, y = 900)

def costsSummary():
    #Defining window settings for the app
    costssummaryWindow = tk.Toplevel() 
    costssummaryWindow.title ("Costs Summmary")
    costssummaryWindow.geometry("1920x1080")
    costssummaryWindow["bg"] = "lightGreen"

    def totalSummary():
        totalcostsWindow = tk.Toplevel() 
        totalcostsWindow.title ("Total Summary of Costs")
        totalcostsWindow.geometry("1920x1080")
        totalcostsWindow["bg"] = "lightGreen"

        #Retrieving Necessary Data.  This takes count of how many entries there are in the database.  Then it prints it onto the Lbl
        def pulltimesPlayed():

            conn = sqlite3.connect (usernameTxt.get() + "costs" + ".db")
            c = conn.cursor()

            c.execute("SELECT COUNT(*) FROM costsdata")
            print_records = c.fetchall()

            #label and position
            timesplayedanswwerLbl = tk.Label (totalcostsWindow, font = ('Courier', 15), bg = "lightGreen", text = print_records)
            timesplayedanswwerLbl.place (x = 600, y = 505)

            conn.commit()
            conn.close
        
        def pullT():

            conn = sqlite3.connect (usernameTxt.get() + "costs" + ".db")
            c = conn.cursor()

            c.execute("SELECT SUM(cost) FROM costsdata")
            print_records = c.fetchall()

            #label and position
            tanswwerLbl = tk.Label (totalcostsWindow, font = ('Courier', 15), bg = "lightGreen", text = print_records)
            tanswwerLbl.place (x = 600, y = 305)

            conn.commit()
            conn.close

        #labels
        weeklysummaryLbl = tkinter.Button (totalcostsWindow, text = "Total Costs Summary!", font = ('Courier', 50))

        #Buttons 
        backBtn = tkinter.Button (totalcostsWindow, text = "Back", font = ('Courier', 20), padx = 30, pady = 10, borderwidth = 1, command = totalcostsWindow.destroy)
        tLbl = tkinter.Button (totalcostsWindow, text = "Total Costs So Far:", bg = "lightGreen", font = ('Courier', 15), command = pullT)
        timesPlayedLbl = tkinter.Button (totalcostsWindow, text = "Amount of Times Played:", bg = "lightGreen", font = ('Courier', 15), command = pulltimesPlayed)

        #positioning 
        weeklysummaryLbl.pack()
        tLbl.place (x = 200, y = 300)
        timesPlayedLbl.place (x = 200, y = 500)

        backBtn.place (x = 900, y = 890)

    def editCosts():
        global editcostsWindow
        editcostsWindow = tk.Toplevel() 
        editcostsWindow.title ("Edit Costs")
        editcostsWindow.geometry("1920x1080")
        editcostsWindow["bg"] = "lightGreen"

        def save():
            conn = sqlite3.connect (usernameTxt.get() + "costs" + ".db")
            c = conn.cursor()

            record_id = deleteTxt.get()
            c.execute("""UPDATE costsdata SET
                monthC = :m,
                dayC = :d,
                yearC = :y,
                cost = :c

                WHERE oid = :oid""",
                {
                    "m": monthTxt_editor2.get(),
                    "d": dayTxt_editor2.get(),
                    "y": yearTxt_editor2.get(),
                    "c": costTxt_editor2.get(),

                    "oid": record_id
                })

            conn.commit()
            conn.close

            editcostsWindow.destroy()
        
        #connecting to database
        conn = sqlite3.connect (usernameTxt.get() + "costs" + ".db")
        c = conn.cursor()

        record_id = deleteTxt.get()
        c.execute("SELECT * FROM costsdata WHERE oid = " + record_id)
        records = c.fetchall()

        #Labels
        editLabel = tkinter.Label (editcostsWindow, text = "Edit a Cost!", font = ('Courier', 75))

        dateLabel = tkinter.Label (editcostsWindow, text = "Date:", font = ('Courier', 50))
        monthLabel = tkinter.Label (editcostsWindow, text = "Month (number)", font = ('Courier', 10))
        dayLabel = tkinter.Label (editcostsWindow, text = "Day (number)", font = ('Courier', 10))
        yearLabel = tkinter.Label (editcostsWindow, text = "Year (XXXX)", font = ('Courier', 10))

        costLabel = tkinter.Label (editcostsWindow, text = "Cost:", font = ('Courier', 50))
        costdescriptionLabel = tkinter.Label (editcostsWindow, text = "X.XX, XX.XX, XXX.XX", font = ('Courier', 10))


        #Text boxes to enter
        monthTxt_editor2 = tkinter.Entry (editcostsWindow, font = ('Courier', 50), width = 10)
        dayTxt_editor2 = tkinter.Entry (editcostsWindow, font = ('Courier', 50), width = 10)
        yearTxt_editor2 = tkinter.Entry (editcostsWindow, font = ('Courier', 50), width = 10)
        costTxt_editor2 = tkinter.Entry (editcostsWindow, font = ('Courier', 50), width = 10)


        #Buttons
        saveBtn = tkinter.Button (editcostsWindow, text = "Save", font = ('Courier', 30), padx = 50, pady = 3, borderwidth = 1, command = save)
        backBtn = tkinter.Button (editcostsWindow, text = "Back", font = ('Courier', 30), padx = 50, pady = 3, borderwidth = 1)

        #positioning
        editLabel.place (x = 500, y = 50)
        dateLabel.place (x = 100, y = 300)

        monthTxt_editor2.place (x = 400, y = 300)
        monthLabel.place (x = 540, y = 275)
        dayTxt_editor2.place (x = 900, y = 300)
        dayLabel. place (x = 1050, y = 275)
        yearTxt_editor2.place (x = 1400, y = 300)
        yearLabel.place (x = 1550, y = 275)

        backBtn.place (x = 1100, y = 900)
        saveBtn.place (x = 510, y = 900)

        costLabel.place (x = 100, y = 500)
        costTxt_editor2.place (x = 400, y = 500)
        costdescriptionLabel.place (x = 520, y = 474)

        #looping through results
        for record in records:
            monthTxt_editor2.insert(0, record[0])
            dayTxt_editor2.insert(0, record[1])
            yearTxt_editor2.insert(0, record[2])
            costTxt_editor2.insert(0, record[3])
    
    #For deleting a record
    def delete():
        conn = sqlite3.connect (usernameTxt.get() + "costs" + ".db")
        c = conn.cursor()

        c.execute("DELETE from costsdata WHERE oid = " + deleteTxt.get())

        deleteTxt.delete(0, 500)

        conn.commit()
        conn.close

    #for pulling the schedule from the database and putting it onto the screen
    def pullCosts():

        conn = sqlite3.connect (usernameTxt.get() + "costs" + ".db")
        c = conn.cursor()

        c.execute("SELECT *, oid FROM costsdata LIMIT 15")
        records = c.fetchall()
        
        print_records = ""
        for record in records:
                print_records += "#" + str(record [4]) + " " + str(record[0]) + "/" + str(record[1]) + "/" + str(record[2]) + " " + "$" + str(record[3])  + "\n"

        #label and position
        costssummaryLbl = tk.Label (costssummaryWindow, font = ('Courier', 30), bg = "lightGreen", text = print_records)
        costssummaryLbl.place (x = 700, y = 100)

        conn.commit()
        conn.close

    #text box
    deleteTxt = tkinter.Entry (costssummaryWindow, font = ('Courier', 45), width = 3)

    #Button
    editBtn = tkinter.Button (costssummaryWindow, text = "Edit Cost #:", font = ('Courier', 10), padx = 42, pady = 2, borderwidth = 1, fg = "red", command = editCosts)
    backBtn = tkinter.Button (costssummaryWindow, text = "Back", font = ('Courier', 20), padx = 30, pady = 10, borderwidth = 1, command = costssummaryWindow.destroy)
    pullcostsBtn = tkinter.Button (costssummaryWindow, text = "Check Costs/Refresh:", font = ('Courier', 20), command = pullCosts)
    deleteBtn = tkinter.Button (costssummaryWindow, text = "Delete Event #:", font = ('Courier', 10), padx = 30, pady = 2, borderwidth = 1, fg = "red", command = delete)

    totalSummary = tkinter.Button (costssummaryWindow, text = "Total Summary", font = ('Courier', 20), command = totalSummary)

    #label
    dateLbl = tkinter.Label (costssummaryWindow, text = "", bg = "lightGreen", font = ('Courier', 30))
    costLbl = tkinter.Label (costssummaryWindow, text = "Cost of Golf Round: " + "", bg = "lightGreen", font = ('Courier', 30), fg = "lightGreen")

    editBtn.place (x = 50, y = 940)
    backBtn.place (x = 890, y = 900)
    deleteBtn.place (x = 50, y = 900)
    pullcostsBtn.pack (pady = 20)

    totalSummary.place (x = 1600, y = 50)

    dateLbl.place (x = 400, y = 500)
    costLbl.place (x = 900, y = 500)
    deleteTxt.place (x = 275, y = 900)

    


def scoresSummary():
    #Defining window settings for the app
    scoresummaryWindow = tk.Toplevel() 
    scoresummaryWindow.title ("Score Summmary")
    scoresummaryWindow.geometry("1920x1080")
    scoresummaryWindow["bg"] = "lightGreen"

    def totalsSummary():
        totalscoresWindow = tk.Toplevel() 
        totalscoresWindow.title ("Total Summary of Scores")
        totalscoresWindow.geometry("1920x1080")
        totalscoresWindow["bg"] = "lightGreen"

        #Retrieving Necessary Data.  This takes count of how many entries there are in the database.  Then it prints it onto the Lbl
        def pulltimesPlayed():

            conn = sqlite3.connect (usernameTxt.get() + "scores" + ".db")
            c = conn.cursor()

            c.execute("SELECT COUNT(*) FROM scoresdata")
            print_records = c.fetchall()

            #label and position
            timesplayedanswwerLbl = tk.Label (totalscoresWindow, font = ('Courier', 15), bg = "lightGreen", text = print_records)
            timesplayedanswwerLbl.place (x = 400, y = 500)

            conn.commit()
            conn.close

        def scoresCalculated():
            conn = sqlite3.connect (usernameTxt.get() + "scores" + ".db")
            c = conn.cursor()

            c.execute("SELECT SUM(strokes) - SUM(par) - SUM(handicap) FROM scoresdata")
            print_records = c.fetchall()

            #label and position
            sanswwerLbl = tk.Label (totalscoresWindow, font = ('Courier', 15), bg = "lightGreen", text = print_records)
            sanswwerLbl.place (x = 800, y = 305)

            conn.commit()
            conn.close
        


        #labels
        weeklysummaryLbl = tkinter.Button (totalscoresWindow, text = "Total Scores Summary!", font = ('Courier', 50))

        #Buttons 
        backBtn = tkinter.Button (totalscoresWindow, text = "Back", font = ('Courier', 20), padx = 30, pady = 10, borderwidth = 1, command = totalscoresWindow.destroy)
        tLbl = tkinter.Button (totalscoresWindow, text = "Total Scores So Far (Combining Par, Handicap, and Strokes):", bg = "lightGreen", font = ('Courier', 15), command = scoresCalculated)
        timesPlayedLbl = tkinter.Button (totalscoresWindow, text = "Amount of Times Played:", bg = "lightGreen", font = ('Courier', 15), command = pulltimesPlayed)

        #positioning 
        weeklysummaryLbl.pack()
        tLbl.place (x = 50, y = 300)
        timesPlayedLbl.place (x = 50, y = 500)

        backBtn.place (x = 900, y = 890)

    def editScores():
        global editscoresWindow
        editscoresWindow = tk.Toplevel() 
        editscoresWindow.title ("Edit Scores")
        editscoresWindow.geometry("1920x1080")
        editscoresWindow["bg"] = "lightGreen"

        def save():
            conn = sqlite3.connect (usernameTxt.get() + "scores" + ".db")
            c = conn.cursor()

            record_id = deleteTxt.get()
            c.execute("""UPDATE scoresdata SET
                monthS = :m,
                dayS = :d,
                yearS = :y,
                par = :p,
                strokes = :s,
                handicap = :h

                WHERE oid = :oid""",
                {
                    "m": monthTxt_editor3.get(),
                    "d": dayTxt_editor3.get(),
                    "y": yearTxt_editor3.get(),
                    "p": totalparTxt_editor3.get(),
                    "s": totalstrokesTxt_editor3.get(),
                    "h": handicapTxt_editor3.get(),

                    "oid": record_id
                })

            conn.commit()
            conn.close

            editscoresWindow.destroy()
        
        #connecting to database
        conn = sqlite3.connect (usernameTxt.get() + "scores" + ".db")
        c = conn.cursor()

        record_id = deleteTxt.get()
        c.execute("SELECT * FROM scoresdata WHERE oid = " + record_id)
        records = c.fetchall()

        #Label
        editLabel = tkinter.Label (editscoresWindow, text = "Edit a Score!", font = ('Courier', 75))
        totalparLabel = tkinter.Label (editscoresWindow, text = "Total Par of Course:", font = ('Courier', 50))
        totalstrokesLabel = tkinter.Label (editscoresWindow, text = "Total Strokes:", font = ('Courier', 50))
        handicapLabel = tkinter.Label (editscoresWindow, text = "Handicap:", font = ('Courier', 50))
        dateLabel = tkinter.Label (editscoresWindow, text = "Date:", font = ('Courier', 50))
        monthLabel = tkinter.Label (editscoresWindow, text = "Month (number)", font = ('Courier', 10))
        dayLabel = tkinter.Label (editscoresWindow, text = "Day (number)", font = ('Courier', 10))
        yearLabel = tkinter.Label (editscoresWindow, text = "Year (XXXX)", font = ('Courier', 10))

        #text boxes to enter
        totalparTxt_editor3 = tkinter.Entry (editscoresWindow, font = ('Courier', 50), width = 10)
        totalstrokesTxt_editor3 = tkinter.Entry (editscoresWindow, font = ('Courier', 50), width = 10)
        handicapTxt_editor3 = tkinter.Entry (editscoresWindow, font = ('Courier', 50), width = 10)
        monthTxt_editor3 = tkinter.Entry (editscoresWindow, font = ('Courier', 50), width = 10)
        dayTxt_editor3 = tkinter.Entry (editscoresWindow, font = ('Courier', 50), width = 10)
        yearTxt_editor3 = tkinter.Entry (editscoresWindow, font = ('Courier', 50), width = 10)

        #Buttton
        saveBtn = tkinter.Button (editscoresWindow, text = "Save", font = ('Courier', 30), padx = 50, pady = 3, borderwidth = 1, command = save)
        backBtn = tkinter.Button (editscoresWindow, text = "Back", font = ('Courier', 30), padx = 50, pady = 3, borderwidth = 1, command = editscoresWindow.destroy)

        #positioning
        editLabel.pack()
        totalparLabel.place (x = 100, y = 450)
        totalparTxt_editor3.place (x = 1000, y = 450)
        totalstrokesLabel.place (x = 100, y = 600)
        totalstrokesTxt_editor3.place (x = 760, y = 600)
        handicapLabel.place (x = 100, y = 750)
        handicapTxt_editor3.place (x = 560, y = 750)
        dateLabel.place (x = 100, y = 300)
        monthTxt_editor3.place (x = 400, y = 300)
        monthLabel.place (x = 540, y = 275)
        dayTxt_editor3.place (x = 900, y = 300)
        dayLabel. place (x = 1050, y = 275)
        yearTxt_editor3.place (x = 1400, y = 300)
        yearLabel.place (x = 1550, y = 275)
        saveBtn.place (x = 510, y = 900)
        backBtn.place (x = 1100, y = 900)

        #looping through results
        for record in records:
            monthTxt_editor3.insert(0, record[0])
            dayTxt_editor3.insert(0, record[1])
            yearTxt_editor3.insert(0, record[2])
            totalparTxt_editor3.insert(0, record[3])
            totalstrokesTxt_editor3.insert(0, record[4])
            handicapTxt_editor3.insert(0, record[5])
    
    #For deleting a record
    def delete():
        conn = sqlite3.connect (usernameTxt.get() + "scores" + ".db")
        c = conn.cursor()

        c.execute("DELETE from scoresdata WHERE oid = " + deleteTxt.get())

        deleteTxt.delete(0, 500)

        conn.commit()
        conn.close

    #for pulling the schedule from the database and putting it onto the screen
    def pullScores():

        conn = sqlite3.connect (usernameTxt.get() + "scores" + ".db")
        c = conn.cursor()

        c.execute("SELECT *, oid FROM scoresdata")
        records = c.fetchall()
        
        print_records = ""
        for record in records:
                print_records += "#" + str(record [6]) + " " + str(record[0]) + "/" + str(record[1]) + "/" + str(record[2]) + " " + "Total Par:" + str(record[3]) + " " + "Total Strokes:" + str(record[4]) + " " + "Handicap:" + str(record[5]) + "\n"

        #label and position
        scoressummaryLbl = tk.Label (scoresummaryWindow, font = ('Courier', 30), bg = "lightGreen", text = print_records)
        scoressummaryLbl.place (x = 200, y = 100)

        conn.commit()
        conn.close

    #text box
    deleteTxt = tkinter.Entry (scoresummaryWindow, font = ('Courier', 45), width = 3)

    #Button
    editBtn = tkinter.Button (scoresummaryWindow, text = "Edit Score #:", font = ('Courier', 10), padx = 38, pady = 2, borderwidth = 1, fg = "red", command = editScores)
    backBtn = tkinter.Button (scoresummaryWindow, text = "Back", font = ('Courier', 20), padx = 30, pady = 10, borderwidth = 1, command = scoresummaryWindow.destroy)
    pullcostsBtn = tkinter.Button (scoresummaryWindow, text = "Check Scores/Refresh:", font = ('Courier', 20), command = pullScores)
    deleteBtn = tkinter.Button (scoresummaryWindow, text = "Delete Event #:", font = ('Courier', 10), padx = 30, pady = 2, borderwidth = 1, fg = "red", command = delete)

    totalSummary = tkinter.Button (scoresummaryWindow, text = "Total Summary", font = ('Courier', 20), command = totalsSummary)

    editBtn.place (x = 50, y = 940)
    backBtn.place (x = 890, y = 900)
    deleteBtn.place (x = 50, y = 900)
    pullcostsBtn.pack (pady = 20)

    totalSummary.place (x = 1600, y = 50)
    deleteTxt.place (x = 275, y = 900)


root.mainloop()
