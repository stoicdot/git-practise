import time
import random
import sys
topic=["Python is a high-level, interpreted programming language created by Guido van Rossum and released in 1991.Python stands out as a highly versatile, multi-paradigm tool that supports object-oriented, structured, and functional programming methodologies.", "Python is Known for its exceptional code readability, simplicity, and ease of writing, it utilizes a clean syntax that heavily features English keywords and relies on mandatory whitespace indentation to define code structure rather than curly braces or semicolons.","This distinct emphasis on clean design reduces the cost of program maintenance and enables developers to write programs using fewer lines of code compared to more rigid languages like C or Java. Because of its steep learning curve and beginner-friendly nature, it has become one of the most widely taught and adopted foundational languages in software education."]
text=random.choice(topic)
def main():
    print("\n===TYPING SPEED TEST===\n")
    print("PRESS ENTER TO START...")
    input()
    print(f"\nTHE TEXT YOU'LL WRITE = '{text}'\n")
    input("PRESS ENTER TO START TYPING TEST...")
    for _ in range(4):
        sys.stdout.write("\033[A\033[2K\r")
    sys.stdout.write("\r")
    sys.stdout.flush()
    start_time = time.perf_counter()
    print(text)
    user_text=input("TYPE :").strip()
    end_time=time.perf_counter()
    time_taken = end_time - start_time
    time_taken=round(time_taken)
    value=(result(user_text,text,time_taken)) 
    print("-"*40)
    amt_of_time=(f"=> Time Taken : {time_taken}second")
    Accurcy=(f"=> Accuracy : {value["Accuracy"]} %")
    Sped=(f"=> Speed : {value["Speed"]} wpm")
    data=["player-1",amt_of_time,Accurcy,Sped]
    print(f"""
    {amt_of_time}\n,
    {Accurcy}\n,
    {Sped}
    """)
    
def result(x:str,y:str,sec:int)->dict:
    X=x.split()
    Y=y.split()
    accuracy=0
    for i,e in zip(X,Y) :
        if i==e:
            accuracy+=1
    speed=len(X)/(sec/60)
    value={
        "Accuracy":accuracy,
        "Speed":f"{speed:.2f}"
    }
    return value

if __name__=="__main__":
    main()