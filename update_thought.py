import datetime
import random

thoughts = [
    "Happiness is as exclusive as a butterfly, and you must never pursue it. If you stay very still, it may come and settle on your hand. But only briefly. - Ruskin Bond",
    "To be able to laugh and to be merciful are the only things that make man better than the beast. - Ruskin Bond",
    "Childhood means simplicity. Look at the world with the child's eye - it is very beautiful. - Kailash Satyarthi",
    "If not now, then when? If not you, then who? - Kailash Satyarthi",
    "I want people to remember me as a Good Person, Not as a Good Cricketer. - M.S. Dhoni",
    "The process is more important than the results. And if you take care of the process, you will get the results. - M.S. Dhoni",
    "Self-belief and hard work will always earn you success. - Virat Kohli",
    "Pressure is something you feel when you don't know what you're doing. - Virat Kohli",
    "It is our choices... that show what we truly are, far more than our abilities. - J.K. Rowling",
    "Happiness can be found, even in the darkest of times, if one only remembers to turn on the light. - J.K. Rowling",
    "To be, or not to be, that is the question. - William Shakespeare",
    "Love all, trust a few, do wrong to none. - William Shakespeare",
    "Language is courage: the ability to conceive a thought, to speak it, and by doing so to make it true. - Salman Rushdie",
    "What is freedom of expression? Without the freedom to offend, it ceases to exist. - Salman Rushdie",
    "Always do right; this will gratify some people and astonish the rest. - Mark Twain",
    "If you tell the truth you don't have to remember anything. - Mark Twain",
    "Arise, awake, and stop not till the goal is reached. - Swami Vivekananda",
    "If you want to shine like a sun, first burn like a sun. - A. P. J. Abdul Kalam",
    "We are what our thoughts have made us; so take care about what you think. - Swami Vivekananda",
    "No legacy is so rich as honesty. - William Shakespeare",
    "The mind is everything. What you think you become. - Buddha",
    "Thousands of candles can be lighted from a single candle, and the life of the candle will not be shortened. Happiness never decreases by being shared. - Buddha",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "Strive not to be a success, but rather to be of value. - Albert Einstein",
    "Imagination is more important than knowledge. - Albert Einstein",
    "The unexamined life is not worth living. - Socrates",
    "Cowards die many times before their deaths; the valiant never taste of death but once. - William Shakespeare",
    "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment. - Ralph Waldo Emerson",
    "What lies behind us and what lies before us are tiny matters compared to what lies within us. - Ralph Waldo Emerson",
    "It is never too late to be what you might have been. - George Eliot",
    "Success consists of going from failure to failure without loss of enthusiasm. - Winston Churchill",
    "The only thing we have to fear is fear itself. - Franklin D. Roosevelt",
    "Ask not what your country can do for you – ask what you can do for your country. - John F. Kennedy",
    "Genius is one percent inspiration and ninety-nine percent perspiration. - Thomas Edison",
    "You miss 100 percent of the shots you never take. - Wayne Gretzky",
    "The way to get started is to quit talking and begin doing. - Walt Disney",
    "Your most unhappy customers are your greatest source of learning. - Bill Gates",
    "Someone is sitting in the shade today because someone planted a tree a long time ago. - Warren Buffett",
    "Remembering that you are going to die is the best way I know to avoid the trap of thinking you have something to lose. - Steve Jobs",
    "Do your little bit of good where you are; it's those little bits of good put together that overwhelm the world. - Desmond Tutu",
    "The best and most beautiful things in the world cannot be seen or even touched - they must be felt with the heart. - Helen Keller",
    "Try to be a rainbow in someone's cloud. - Maya Angelou",
    "No matter what people tell you, words and ideas can change the world. - Robin Williams",
    "Don't judge each day by the harvest you reap but by the seeds that you plant. - Robert Louis Stevenson",
    "We are such stuff as dreams are made on, and our little life is rounded with a sleep. - William Shakespeare",
    "Nothing in life is to be feared, it is only to be understood. Now is the time to understand more, so that we may fear less. - Marie Curie",
    "Have no fear of perfection; you'll never reach it. - Marie Curie",
    "It is the function of science to discover the existence of a general reign of order in nature and to find the causes governing this order. - Dmitri Mendeleev",
    "We must trust to nothing but facts: These are presented to us by Nature, and cannot deceive. - Antoine Lavoisier",
    "In nature, nothing is created, nothing is lost, everything changes. - Antoine Lavoisier",
    "Every aspect of the world today – even politics and international relations – is affected by chemistry. - Linus Pauling",
    "Science is the search for truth, that is the effort to understand the world: it involves the rejection of bias, of dogma, of revelation, but not the rejection of morality. - Linus Pauling",
    "Atoms cannot be seen, but we infer their existence and properties from the ways in which substances behave. - John Dalton",
    "Science knows no country, because knowledge belongs to humanity, and is the torch which illuminates the world. - Louis Pasteur",
    "In the fields of observation chance favors only the prepared mind. - Louis Pasteur",
    "Science and everyday life cannot and should not be separated. - Rosalind Franklin",
    "The more I study science, the more I believe in God. - Max Planck",
    "All science is either physics or stamp collecting. - Ernest Rutherford",
    "I have measured the heavens, now I shall measure the shadows of Earth. - Johannes Kepler",
    "Science is the poetry of reality. - Richard Dawkins",
    "We are all connected; to each other, biologically. To the Earth, chemically. To the rest of the universe, atomically. - Neil deGrasse Tyson",
    "Look up at the stars and not down at your feet. Try to make sense of what you see, and wonder about what makes the universe exist. Be curious. - Stephen Hawking",
]

# Randomly shuffle the thoughts list
random.shuffle(thoughts)

def get_random_thought():
    return random.choice(thoughts)

def update_readme():
    current_date = datetime.date.today().strftime("%Y-%m-%d")
    thought_of_the_day = get_random_thought()

    # Split the thought into the quote text and author for placing the heart
    quote_parts = thought_of_the_day.rsplit(' - ', 1)
    quote_text = quote_parts[0]
    author_name = quote_parts[1] if len(quote_parts) > 1 else "Unknown Author"

    # --- START OF MODIFIED CONTENT (for README styling) ---
    new_content = ""
    new_content += "# ✨ Daily Dose of Inspiration ✨\n\n"
    new_content += "--- \n\n"

    new_content += "_Your daily spark of wisdom!_\n\n"

    new_content += f"## 🗓️ Date: **{current_date}**\n\n"
    new_content += f"### 💬 Today's Insight:\n"
    new_content += "```\n"
    # The quote with the red heart before the author's name
    new_content += f"> #### {quote_text} ❤️ - {author_name}\n"
    new_content += "```\n\n"

    new_content += "--- \n\n"
    new_content += "**Thank You for Visiting!** 🙏\n"
    new_content += "**Have a Wonderful Day!** ☀️\n"
    # --- END OF MODIFIED CONTENT ---

    with open("README.md", "w") as f:
        f.write(new_content)

if __name__ == "__main__":
    update_readme()
    print("README.md updated with new thought!")