import argparse
from . import api
import os
from .files import write

ap = argparse.ArgumentParser(description="Download all of your devRant account data")
ap.add_argument("username", help="The (valid) username of your account")
ap.add_argument("output", help="An (empty) directory to dump your data into")
ap.add_argument("--rants-only", help="Only download rants", default=False)
ap.add_argument("-c", "--compress-output", help="Should the output directory be compressed once finished?",  default=False)
args = ap.parse_args()

# Type conversion
args.rants_only = bool(args.rants_only)
args.compress_output = bool(args.compress_output)

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