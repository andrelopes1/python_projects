zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

if "energy" in zodiac_elements:
    print(zodiac_elements["energy"])



zodiac_elements.update({"energy": "Not a Zodiac element"})
