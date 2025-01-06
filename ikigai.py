import streamlit as st

# Simulated database for skill and passion recommendations
passion_database = {
    "travel": ["Travel Blogger", "Tour Guide", "Travel Photographer", "Travel Consultant", "Adventure Guide", "Travel Vlogger", "Cruise Director"],
    "technology": ["Software Developer", "AI Researcher", "Tech Blogger", "Cybersecurity Specialist", "Web Developer", "Data Engineer", "Game Developer", "Robotics Engineer"],
    "sports": ["Athlete", "Coach", "Sports Analyst", "Fitness Trainer", "Sports Journalist", "Physical Therapist", "Referee", "Esports Player"],
    "arts": ["Painter", "Graphic Designer", "Musician", "Writer", "Art Teacher", "Animator", "Sculptor", "Theater Director"],
    "education": ["Teacher", "Education Consultant", "Curriculum Developer", "EdTech Specialist", "Librarian", "Academic Researcher", "Tutor", "Instructional Designer"],
    "health": ["Doctor", "Nurse", "Nutritionist", "Personal Trainer", "Therapist", "Dentist", "Pharmacist", "Healthcare Administrator"],
    "business": ["Entrepreneur", "Business Analyst", "Marketing Specialist", "Financial Advisor", "HR Manager", "Operations Manager", "Sales Executive", "Product Manager"],
    "science": ["Research Scientist", "Data Analyst", "Astronomer", "Biotechnologist", "Environmental Scientist", "Chemist", "Physicist", "Marine Biologist"],
    "food": ["Chef", "Food Blogger", "Nutritionist", "Restaurant Manager", "Food Photographer", "Pastry Chef", "Sommelier", "Culinary Instructor"],
    "environment": ["Conservationist", "Environmental Scientist", "Wildlife Photographer", "Sustainability Consultant", "Park Ranger", "Ecologist", "Urban Planner", "Climate Policy Advocate"],
    "fashion": ["Fashion Designer", "Stylist", "Fashion Blogger", "Model", "Textile Designer", "Retail Buyer", "Costume Designer", "Trend Forecaster"],
    "entertainment": ["Actor", "Director", "Screenwriter", "Producer", "Comedian", "Voice Actor", "Film Critic", "Cinematographer"],
    "finance": ["Accountant", "Investment Banker", "Stock Analyst", "Risk Manager", "Auditor", "Tax Consultant", "Wealth Manager", "Actuary"],
    "writing": ["Author", "Copywriter", "Editor", "Journalist", "Technical Writer", "Content Strategist", "Poet", "Blogger"],
    "gaming": ["Game Developer", "Game Tester", "Esports Player", "Streamer", "Game Designer", "Level Designer", "Gaming Journalist", "Virtual Reality Developer"],
    "psychology": ["Psychologist", "Therapist", "Counselor", "Social Worker", "Behavioral Analyst", "Clinical Psychologist", "School Counselor", "Organizational Psychologist"],
    "social services": ["Social Worker", "Community Organizer", "Case Manager", "Substance Abuse Counselor", "Youth Worker", "Nonprofit Manager", "Crisis Intervention Specialist"],
    "legal": ["Lawyer", "Paralegal", "Judge", "Legal Consultant", "Mediator", "Corporate Counsel", "Public Defender", "Legal Analyst"],
    "engineering": ["Mechanical Engineer", "Civil Engineer", "Electrical Engineer", "Software Engineer", "Chemical Engineer", "Aerospace Engineer", "Biomedical Engineer", "Industrial Engineer"],
    "agriculture": ["Farmer", "Agricultural Scientist", "Horticulturist", "Agribusiness Manager", "Soil Scientist", "Crop Consultant", "Irrigation Specialist", "Agroecologist"],
    "media": ["Journalist", "News Anchor", "Photographer", "Videographer", "Public Relations Specialist", "Content Creator", "Media Planner", "Broadcast Technician"],
    "trades": ["Carpenter", "Electrician", "Plumber", "Welder", "Mechanic", "Construction Worker", "HVAC Technician", "Machinist"],
    "transport": ["Pilot", "Truck Driver", "Logistics Manager", "Freight Broker", "Ship Captain", "Railway Engineer", "Cab Driver", "Aviation Mechanic"],
    "hospitality": ["Hotel Manager", "Event Planner", "Tour Guide", "Concierge", "Bartender", "Housekeeping Manager", "Catering Manager", "Travel Agent"]
}

# Function to recommend passions
def recommend_passion(answers):
    for keyword, passions in passion_database.items():
        if keyword in " ".join(answers).lower():
            return passions
    return ["Couldn't identify a clear passion. Explore general areas like arts, tech, or sports!"]

# Streamlit UI
st.title("Discover Your Passion for Free!")
questions = [
    "What do you enjoy doing in your free time?",
    "What topics do you find yourself reading or learning about?",
    "If money wasn’t a concern, what would you pursue?",
    "What activities make you lose track of time?",
    "What is one skill you wish to master?",
    "What do people often come to you for help with?",
    "If you could change one thing in the world, what would it be?"
]

answers = [st.text_input(question) for question in questions]

if st.button("Find My Passion"):
    suggestions = recommend_passion(answers)
    st.write("Here are some possible passions for you:")
    for suggestion in suggestions:
        st.write(f"- {suggestion}")
