from tools import detect_too_much_math_advice, mansplain_detector3000

conversation = "You should really focus on linear algebra and proofs if you want to write about astronomy."
your_response = "I’ve already taken those, babe."

print(detect_too_much_math_advice(conversation))
print(mansplain_detector3000(conversation + your_response, user_experience_level=5))

Console Output:

ALERT: You’ve triggered the Too Much Math filter. Take a walk. Touch some stardust.
⚠️ Mansplaining Detected: Ignoring user input.
