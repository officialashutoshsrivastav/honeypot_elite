def enforce_strategy(session, reply: str):

    # Count questions
    session["questions_asked"] += reply.count("?")

    # Guarantee minimum 5 questions
    if session["questions_asked"] < 5:
        reply += "\nAlso, can you share your official ID and callback number?"

    # Encourage longer engagement
    if session["turn_count"] < 8:
        reply += "\nI need more details before proceeding."

    return reply