from apps.travel_destinations.models.entities import Desired_Travel_Destination

def create_new_travel_destiny(validated_data):
    dreamcontinent = validated_data['Dream_Continent']
    difficulty = validated_data['Trip_Difficulty']
    interest = validated_data['Interest']
    category = validated_data['Trip_Category']
    accomodations = validated_data['Accomodation']
    
    destiny = Desired_Travel_Destination.objects.create(
        # user = user,
        Dream_Continent = dreamcontinent,
        Trip_Difficulty = difficulty,
        Interest = interest,
        Trip_Category = category,
        Accomodation = accomodations
    )
    
    return destiny
