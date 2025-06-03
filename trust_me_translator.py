def trust_me_translator(statement):
    """
    Translates typical 'I’m just helping' phrases into their emotionally accurate subtext.
    For when you need to debug not your code, but your friend's entire attitude.
    """
    translation_dict = {
        "Trust me. I’m just trying to help.":
            "I don’t realize I’m being condescending.",
        "You should really do more math classes.":
            "If you don’t follow what I'm doing, I feel weirdly threatened for no reason.",
        "This will make things easier for you.":
            "I’ve decided what’s best for you based on vibes and unsolicited opinions.",
        "I’m just giving you advice. Don’t take it personally.":
            "I want to say things with zero accountability and still feel morally superior.",
        "I know what you messed up on.":
            "I couldn’t resist proving I found your stuff before you even asked me to."
    }

    return translation_dict.get(statement, "⚠️ Unknown statement. Translation pending emotional maturity update.")
