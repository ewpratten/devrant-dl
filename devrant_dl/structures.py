
class Rant(object):
    author_name: str
    body: str
    score: int
    comment_count: int
    comments: list
    date: int

    def getComments(self):
        output = ""

        for comment in self.comments:
            output += str(comment) + "\n-----\n\n"

        return output

    def __str__(self):
        return f"""
:: Rant Info ::
Rant by: {self.author_name}
Score: {self.score}
Number of comments: {self.comment_count}

:: Rant Body ::
{self.body}

:: Comments ::
{self.getComments()}
        """

    def dict(self):
        return {
            "Metadata": {
                "author": self.author_name,
                "score": self.score,
                "timestamp": self.date
            },
            "body": self.body,
            "comments": [comment.dict() for comment in self.comments]
        }


class Comment(object):
    author_name: str
    score: int
    body: str
    date: int

    def __str__(self):
        return (f"""
:: Comment Info ::
Commment By: {self.author_name}
Score: {self.score}

:: Comment Body ::
{self.body}
        """)

    def dict(self):
        return {
            "Metadata": {
                "author": self.author_name,
                "score": self.score,
                "timestamp": self.date
            },
            "body": self.body
        }


class Profile(object):
    username: str
    user_id: str
    score: int
    profile_pic_gen: str
    profile_pic_uri: str
    bio: str
    skills: str
    location: str
    website: str
    github: str
    creation_date: int

    rant_count: int
    comment_count: int
    upvote_count: int
    fav_count: int

    rants: list
    comments: list
    upvoted: list
    favs: list

    def __str__(self):
        return (f"""
:: Profile Report ::
Username: {self.username} ({self.user_id})
Score: {self.score}

Bio: {self.bio}
Skills: {[skill.strip() for skill in self.skills.split(",")]}
Location: {self.location}
Website: {self.website}
GitHub Account: {self.github}

:: Profile Photo ::
Photo URL: {self.profile_pic_gen}
Photo URI: {self.profile_pic_uri}

:: Metrics ::
Created on: {self.creation_date}
Rant count: {self.rant_count}
Comment count: {self.comment_count}
Upvote count: {self.upvote_count}
        """)

    def dict(self):
        return {
            "profile": {
                "username": self.username,
                "user_id": self.user_id,
                "score": self.score,
                "bio": self.bio,
                "skills": [skill.strip() for skill in self.skills.split(",")],
                "location": self.location,
                "website": self.website,
                "github": self.github
            },
            "profile_pic": {
                "url": self.profile_pic_gen,
                "uri": self.profile_pic_uri
            },
            "metrics": {
                "timestamp": self.creation_date,
                "rant_count": self.rant_count,
                "comment_count": self.comment_count,
                "upvote_count": self.upvote_count
            }
        }
