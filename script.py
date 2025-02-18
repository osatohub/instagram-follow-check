import json
import csv

# Load Followers List
def load_followers():
    with open("followers_1.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return set(user["string_list_data"][0]["value"] for user in data["followers"])  # Extract usernames

# Load Following List
def load_following():
    with open("following.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return set(user["string_list_data"][0]["value"] for user in data["relationships_following"])  # Extract usernames

def main():
    followers = load_followers()
    following = load_following()
    
    not_following_back = following - followers
    not_followed_back = followers - following
    
    with open("instagram_follow_analysis.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Not Following Me Back"])
        writer.writerows([[user] for user in not_following_back])
        writer.writerow([])
        writer.writerow(["I’m Not Following Back"])
        writer.writerows([[user] for user in not_followed_back])
    
    print("Done! Results saved in 'instagram_follow_analysis.csv'")

if __name__ == "__main__":
    main()
