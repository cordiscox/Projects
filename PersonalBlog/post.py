from datetime import date
import json
import os

class Post:

    def __init__(self):
        self.posts = os.listdir("posts")
        self.last_id = self.get_lastid()

    def getAllPost(self):
        posts = []
        try:
            for post in self.posts:
                with open(f"posts/{post}", "r") as file:
                    posts.append(json.load(file))
        except Exception as e:
            print(e)
        
        return posts

    
    def getPost(self, id):
        
        for post in self.posts:
            with open(f"posts/{post}", "r") as file:
                post = json.load(file)
                if post["id"] == id:
                    return post
        return("ERROR 404")
        


    def deletePost(self, title):
        pass

    def addPost(self, title, date, content):
        to_add = {
            "id": self.last_id + 1,
            "title": title,
            "content": content,
            "createdAt": date #date.today().isoformat()
        }
        # this need to create always a new json file.
        try:
            with open(f"posts/{title}.json", "w") as file:
                json.dump(to_add, file, indent=4)
        except FileExistsError as e:
            print(f"The file with title {title} already exists")
        except Exception as e:
            print(e)

        #update posts property and last_id
        self.posts.append(f"{title}.json")
        self.last_id = to_add["id"]


    def updatePost(self, idPost, data):
        try:
            for post in self.posts:
                with open(f"posts/{post}", "r+") as file:
                    existing_data = json.load(file)
                    if idPost == existing_data["id"]:
                        existing_data["title"] = data["title"]
                        existing_data["content"] = data["content"]
                        existing_data["createdAt"] = data["createdAt"]
                        file.seek(0)
                        json.dump(existing_data, file, indent=4)
                        file.truncate()
                        print("Data updated correctly")
                        return
            print("Data no update")
        except Exception as e:
            print("error",e)


    def get_lastid(self):
        ids = []
        try:
            for post in self.posts:
                with open(f"posts/{post}", "r") as file:
                    ids.append(json.load(file)["id"])
        except Exception:
            return 0

        return max(ids)

            
                
