def space_border(func):
    def wrapper(message):
        border = "🚀" * (len(message) + 8)
        result = func(message)
        return f"{border}\n🚀  {result}  🚀\n{border}"
    return wrapper

def galaxy_effect(func):
    def wrapper(message):
        result = func(message)
        return f"🌌✨ {result} ✨🌌"
    return wrapper