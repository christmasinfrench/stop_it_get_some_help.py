def please_stop_lecturing_me(context="general"):
    """
    Politely but firmly tells the ‘bro lecture mode’ to take a chill pill.
    Because sometimes friendship isn’t a masterclass and unsolicited critiques can GTFO.
    """

    messages = {
        "general": "Hey, I’m sharing vibes, not inviting a lecture. Take a seat, sip some tea, and enjoy the playlist.",
        "code_critique": "Love that you care, but this isn’t a code review session. Save it for the repo where I actually ask, cool?",
        "creative_share": "Creative shares come with zero tolerance for critique mode. Let’s just vibe, not grade, okay?",
        "phone_coding": "Typed this on my phone, so if it’s not perfect, congrats, you caught me in human mode. No rewrites needed.",
        "repeated_critique": "You’ve hit peak unsolicited feedback. This is your sign to take a break from your inner critic and come back with kindness.",
    }

    return messages.get(context, messages["general"])

print(please_stop_lecturing_me())  # General vibe check
print(please_stop_lecturing_me("code_critique"))  # When he turns every share into a code lecture
print(please_stop_lecturing_me("creative_share"))  # For artsy stuff he’s trying to nitpick
print(please_stop_lecturing_me("phone_coding"))  # When you remind him you’re human
print(please_stop_lecturing_me("repeated_critique"))  # When he just won’t let up

Hey, I’m sharing vibes, not inviting a lecture. Take a seat, sip some tea, and enjoy the playlist.
Love that you care, but this isn’t a code review session. Save it for the repo where I actually ask, cool?
Creative shares come with zero tolerance for critique mode. Let’s just vibe, not grade, okay?
Typed this on my phone, so if it’s not perfect, congrats, you caught me in human mode. No rewrites needed.
You’ve hit peak unsolicited feedback. This is your sign to take a break from your inner critic and come back with kindness.
