import os
def get_noise_files(path="noise"):
    datalist={}
    data=os.listdir(path)
    data=list(filter(lambda i:i.endswith('.mp3'),data))
    for item in data:
        datalist.update({item: os.path.join(path,item)})
    return datalist

if __name__ == "__main__":
    print(get_noise_files())