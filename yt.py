from pytube import YouTube

link=input("Please enter a link to download")
youtube1=YouTube(link)

# print(youtube1.title)
videos=youtube1.streams.all()
vid=list(enumerate(videos))
for i in vid:
    print(i)
strm=int(input("enter number of video"))
videos[strm].download()
print("Done")
