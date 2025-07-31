# news application - displayes the latest news articles from this platfrom - https://newsapi.org/
# uses NewsAPI to fetch articles and Tkinter for the user interface
# project by Malibongwe Makhubo

import requests                                                             # to make http requests to the API
import tkinter as tk                                                        # for making the GUI

def loadNews():
    api_key = "942ba8aa3c194428a179fe2fb27dde59"                                                    # api key for authentications
    url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey="+api_key       # the route from which we retreive the information from
    news =  requests.get(url).json()                                                                # make http request and convert to json
    
    articles = news["articles"]                                                                     # extract articles from API response
    
    my_articles = []                                                                                
    my_news = ""
    
    for x in articles:
        my_articles.append(x["title"])
        
    for m in range(10):                                                                             # display the first 10 articles as a numbered list
        my_news = my_news +str(m+1)+ ". " + my_articles[m] + "\n"
    
    label.config(text = my_news)                                            
    
    
    
canvas = tk.Tk()                                                            # setting up canvas, the main window for the results to be displayed
canvas.geometry("900x350")                                                  # setting up the width and height of the box/canvas
canvas.title("Latest News")

label = tk.Label(canvas, font=18, justify="left")
label.pack(pady=20)

loadNews()

canvas.mainloop()                                                           # keeps the window open and responsive
