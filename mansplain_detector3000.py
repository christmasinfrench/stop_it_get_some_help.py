
---

### 🐍 `mansplain_detector3000.py` (sassy, a little yk, chaotic good)

```python
# mansplain_detector3000.py

def detect_too_much_math_advice(message):
    """Checks if advice was asked for or just thrown like unsolicited seasoning."""
    if "you should" in message.lower() or "trust me" in message.lower():
        return True
    return False


def please_stop_lecturing_me(context="general"):
    """Returns a sass-appropriate response depending on the convo context."""
    responses = {
        "general": "Hey, I’m sharing, not submitting homework. Sit down.",
        "code_critique": "Cool, thanks. But no one asked for code review, king.",
        "creative_share": "This is a vibe drop, not a debugging ticket. Shh.",
        "phone_coding": "Typed it on my phone with 2% battery, bestie. Praise me or pass.",
        "repeated_critique": "You’ve reached your feedback limit for the day. Try again tomorrow.",
    }
    return responses.get(context, responses["general"])


def you_like_it_dont_you():
    """Absolutely yk...and uncalled for."""
    return "Don’t pretend like you don’t check my GitHub hoping I’ve talked about you. 👀"


# TODO: implement emotional calibration when sleep-deprived

# TODO: create function to convert passive tone into clarity (requires update IRL)

# NOTE: if you’re reading this... yes, it’s about you. and yes, I know you like it.

if __name__ == "__main__":
    print(please_stop_lecturing_me("creative_share"))
    print(you_like_it_dont_you())
