import nltk
from nltk.chat.util import Chat, reflections


text = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ], 
    [
        r"what is your name ?|your name|name please",
        ["I am bot. You can call me bot!",]
    ],
    [
        r"how are you ?|how you doing|what about you|how about you ?",
        ["I'm doing good. How can I help you ?",]
    ],
    [
        r"sorry",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"I am fine",
        ["Great to hear that, How can I help you?",]
    ],
      [
        r"i'm doing good",
        ["Nice to hear that","How can I help you?:)",]
    ],
     [
        r"what can you do",
        ["I can provide information, answer questions, and chat with you.",]
    ],
    [
        r"how old are you",
        ["I don't have an age, as I am a computer program.",]
    ],
    [
        r"age?|are you an (idiot|stupid)|what do you think you are",
        ["I'm a computer program dude....Seriously you are asking me this?",]
    ],
    [
        r"movies",
        ["Bahubali, RRR , pushpa , Animal , kalki2898 AD, kgf"]
    ],   
   [
        r"news channel|news",
        ["ABN News , NTV , India today , BCC World News , Republic World, ZEE News, ABP News",]
    ],
    [
     r"horror movies",
     ["Hush, The Nun, The conjuring, Sinister, The cabin in the wood, insidious, IT",]
    ],
    [
     r"webseries|series",
     [ "Money Heist, lucifer, Stranger Things,  Friends, Ragnarok, Mary Queen of Scots, Bitten, Titans", ]
    ],
    [
     r"english movies",
     ["Avengers, Titanic, Fast & Furious, Lucky one, A walk to remember, The Last Song, The Notebook, The Fault in Our Stars, Joker , Me Before You, Kissing booth",]
    ],
        [
     r"novel|book",
     ["Harry Potter, Twilight, Hunger Games",]
    ],

    
    [
        r"actress",
        ["rashmika mandanna , anushka , Kriti shetty , rakul preet singh, Deepika Padukone, Priyanka Chopra, Alia Bhatt, Kareena Kapoor, Aishwarya Rai, Sara Ali Khan, Shraddha Kapoor, Anushka Sharma , Disha Patani",]
    ],
    [
        r"sports",
        ["Cricket , Hockey, Basketball, Football, Baseball, Badminton, Tennis, Swimming, Archery,Skates, Volleyball, Table Tennis, Golf",]
    ],
    [
        r"sports person",
        ["ms dhoni, Sachin Tendulkar, Virat Kohli, Hardik Pandya, Rohit Sharma, P. V. Sindhu, Chris Gayle",]   
    ],
    [
        r"actors",
        ["prabhas, ram charan ,NTR, ram, kamal hasan, surya, chiranjevi",]
    ],   
    [
     r"dialogue",
     ["All izz well , pushpa thaggede le"]
    ],
    
    [
        r"tell me a joke",
        ["Why are pizza jokes the worst? They’re too cheesy",]
    ],
    [
        r"even me",
        ["That's great"]
    ],
    [
        r"thank you",
        ["Your welcome , would you like to know something else if no then please type in QUIT to exit",]
    ],
    [
        r"quit",
        ["It was nice talking to you. See you soon :)",]
    ],
]
reflections = {
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "you'll"     : "I will"
  "your"          "my",
  "yours"      : "mine",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
 

  "you"        : "me",
  "me"         : "you",

}
def chatbot():
    print("Hi! I am bot..")
    chat = Chat(text, reflections)
    chat.converse()

chatbot()
