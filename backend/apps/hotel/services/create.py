from apps.hotel.models.entities import Hotel

def create_new_hotel_data_record(validated_data, user):
    name = validated_data['Hotel_Name']
    category = validated_data['Hotel_Category_In_Stars']
    location = validated_data['Hotel_Location']
    number_of_rooms = validated_data['Total_Rooms_Available']
    description = validated_data['Room_Description']
    price_of_room = validated_data['Room_Rent_Per_Day_In_Nepali_Rupees']
    
    hotel_detail = Hotel.objects.create(
        Hotel_Owner_Username = user,
        Hotel_Name = name,
        Hotel_Category_In_Stars = category,
        Hotel_Location = location,
        Room_Description = description,
        Total_Rooms_Available = number_of_rooms,
        Room_Rent_Per_Day_In_Nepali_Rupees = price_of_room,
    )
    
    return hotel_detail
