def detect_too_much_math_advice(convo):
    """
    Flags when your guy friend cannot have a single STEM convo without turning it into a math worship session.
    """
    math_keywords = ["calculus", "linear algebra", "derivatives", "proof", "theoretical"]
    counter = sum(1 for word in math_keywords if word in convo.lower())
    if counter > 2:
        return "ALERT: You’ve triggered the Too Much Math filter. Take a walk. Touch some stardust."
    return "Math levels acceptable. Carry on, Copernicus."

def mansplain_detector3000(statement, user_experience_level):
    """
    Detects when a man explains something to a woman she clearly already knows.
    """
    if "trust me" in statement.lower() and user_experience_level >= 3:
        return "⚠️ Mansplaining Detected: Confidence without context."
    elif "you should really" in statement.lower() and "i already did" in statement.lower():
        return "⚠️ Mansplaining Detected: Ignoring user input."
    return "Clean. Surprisingly chill for once."
