import instaloader

test = instaloader.Instaloader()

acc = input("Enter the account usename :")

test.download_profile(acc, profile_pic_only=True)
