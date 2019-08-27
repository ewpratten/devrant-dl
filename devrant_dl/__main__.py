import argparse
from . import api
import os
from .files import write

ap = argparse.ArgumentParser(description="Download all of your devRant account data")
ap.add_argument("username", help="The (valid) username of your account")
ap.add_argument("output", help="An (empty) directory to dump your data into")
ap.add_argument("--rants-only", help="Only download rants", default=False)
# ap.add_argument("-c", "--compress-output", help="Should the output directory be compressed once finished?",  default=False)
args = ap.parse_args()

# Type conversion
args.rants_only = bool(args.rants_only)
# args.compress_output = bool(args.compress_output)

# Make sure this user is valid
if not api.isValidUser(args.username):
    print(f"{args.username} does not seem to be a valid username.. Try again?")
    exit(1)

print(f"Hello {args.username}! I'm currently getting things set up for you..")

# Check if output dir needs to be created
if not os.path.exists(args.output):
    print("Creating output directory")
    os.mkdir(args.output)

# Load profile
upo, uid = api.fetchProfile(args.username)
user_profile = api.profile2Profile(upo, uid)
print("Loaded profile")

# Write the basic profile
write(user_profile, args.output, "profile")
print("Wrote profile data")

# Load all rants
user_rants = []
for i in range(user_profile.rant_count):
    if i % 30 != 0:
        continue
    
    rant_page = api.getRantPage(uid, i)
    user_rants += rant_page
    print(f"Loaded page {i / 30} / {str(user_profile.rant_count / 30).split('.')[0]}")

print("Loaded rants")


# Write rants
for i, rant in enumerate(user_rants):
    write(rant, args.output + "/rants", f"Rant-{rant.date}", txt="/text/", js="/json/")

    if i % 30 == 0:
        print(f"Wrote page {i / 30}")
print("Wrote rants")

# Check if that is all the user requested
if args.rants_only:
    print("Your data is ready")
    exit(1)

print("Downloading comments and upvotes has not yet been implemented. Feel free to open a PR over at:")
print("https://github.com/Ewpratten/devrant-dl")
exit(0)