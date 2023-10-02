#!/usr/bin/env python3
from myapp import db,app
from myapp.models import Hero,Power,HeroPower

def populate_database():
    with app.app_context():
# seed Powers
        powers_data = [
            { "name": "super strength", "description": "gives the wielder super-human strengths" },
            { "name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed" },
            { "name": "super human senses", "description": "allows the wielder to use her senses at a super-human level" },
            { "name": "elasticity", "description": "can stretch the human body to extreme lengths" }
        ]

        for power_data in powers_data:
            power = Power(**power_data)
            db.session.add(power)

        # seed Heros
        heros_data =[
        { "name": "Kamala Khan", "super_name": "Ms. Marvel" },
        { "name": "Doreen Green", "super_name": "Squirrel Girl" },
        { "name": "Gwen Stacy", "super_name": "Spider-Gwen" },
        { "name": "Janet Van Dyne", "super_name": "The Wasp" },
        { "name": "Wanda Maximoff", "super_name": "Scarlet Witch" },
        { "name": "Carol Danvers", "super_name": "Captain Marvel" },
        { "name": "Jean Grey", "super_name": "Dark Phoenix" },
        { "name": "Ororo Munroe", "super_name": "Storm" },
        { "name": "Kitty Pryde", "super_name": "Shadowcat" },
        { "name": "Elektra Natchios", "super_name": "Elektra" }

        ]
        for hero_data in heros_data:
            hero = Hero(**hero_data)
            db.session.add(hero)

        # commit changes
            db.session.commit()

        # Add powers to heros with random strengths
        import random

        strengths = ['Strong', 'Weak', 'Average']
        heroes =Hero.query.all()

        for hero in heroes:
            random_powers = random.sample(Power.query.all(), random.randint(1, 3))
            for power in random_powers:
                hero_power = HeroPower(hero=hero, power=power, strength=random.choice(strengths))
                db.session.add(hero_power)
                db.session.commit()

        print("🦸‍♀️ Done seeding!")

if __name__ == '__main__':
    populate_database()