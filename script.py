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

    # Display results in the console
    print("Not Following Me Back:")
    for user in not_followed_back:
        print(user)

    print("\nI'm Not Following Back:")
    for user in not_following_back:
        print(user)

    # Ask user if they want to save the results as CSV
    save_option = input("\nDo you want to save the results as a CSV file? (yes/no): ").strip().lower()

    if save_option == "yes":
        # Save results to CSV
        with open("instagram_follow_analysis.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Not Following Me Back"])
            writer.writerows([[user] for user in not_followed_back])
            writer.writerow([])  # Blank row
            writer.writerow(["I'm Not Following Back"])
            writer.writerows([[user] for user in not_following_back])
        
        print("Results saved in 'instagram_follow_analysis.csv'.")
    else:
        print("Results not saved.")

if __name__ == "__main__":
    main()
