import os
import re
import pandas as pd

if __name__ == '__main__':
    dir_path = 'C:\\Users\\cg398\\Desktop\\DFC\\MISC400'
    files = os.listdir(dir_path)
    p = re.compile("Action\d+.csv")

    likers = dict()
    dislikers = dict()

    for file in files:
        if(p.match(file) != None):
            file = os.path.join(dir_path, file)
            print(file)
            df = pd.read_csv(file, names=['Comment_ID', 'ID', 'URL', 'CLK_DT', 'Action'], 
                dtype={'Comment_ID' : str, 'ID' : str, 'URL' : str, 'CLK_DT' : str, 'Action' : str})
            
            for i in df.index:
                if(i % 1000000 == 0):
                    print("index : ", i)
                action = df.at[i, 'Action']
                id = df.at[i, 'ID'] 
                if(action == 'like'):        # Action 열의 값이 like인 경우
                    if(id in likers) :
                        likers[id] += 1      # 키가 이미 있는 경우 값을 증가
                    else:
                        likers[id] = 1       # 키가 없는 경우 값을 1로 저장
                elif(action == 'dislike'):   # Action 열의 값이 like인 경우
                    if(id in dislikers) :
                        dislikers[id] += 1   # 키가 이미 있는 경우 값을 증가
                    else:
                        dislikers[id] = 1    # 키가 없는 경우 값을 1로 저장

    print("likers---------------------")
    likers_df = pd.DataFrame(likers.items(), columns=['ID', 'Count'])
    likers_df = likers_df.sort_values(['Count'], ascending = False)
    likers_df = likers_df.reset_index(drop=True)
    print(likers_df.iloc[:30])
   

    print("\ndislikers----------------------")
    dislikers_df = pd.DataFrame(dislikers.items(), columns=['ID', 'Count'])
    dislikers_df = dislikers_df.sort_values(['Count'], ascending = False)
    dislikers_df = dislikers_df.reset_index(drop=True)
    print(dislikers_df.iloc[:30])