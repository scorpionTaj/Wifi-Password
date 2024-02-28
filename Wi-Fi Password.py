import subprocess

# Function to export profiles to a text file
def export_to_txt(profiles, keys):
    with open('wifi_profiles.txt', 'w') as file:
        for profile, key in zip(profiles, keys):
            file.write(f"{profile:<30}|  {key}\n")
    print("Wi-Fi profiles have been exported to wifi_profiles.txt")

# Retrieve WiFi profiles and keys
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

keys = []
for profile in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8').split('\n')
    key = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    if key:
        keys.append(key[0])
    else:
        keys.append("")

# Print profiles and keys
for profile, key in zip(profiles, keys):
    print(f"{profile:<30}|  {key}")

# Prompt the user to export to a text file
export_choice = input("Do you want to export the Wi-Fi profiles to a text file? (yes/no): ")
if export_choice.lower() == 'yes':
    export_to_txt(profiles, keys)
else:
    print("Wi-Fi profiles have not been exported.")

# Wait for a key press to continue
input("Press Enter to continue...")
