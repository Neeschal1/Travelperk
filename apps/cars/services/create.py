from apps.cars.models.entities import Car

def create_new_car_data(validated_data, owner):
    carname = validated_data['Car_Name']
    model = validated_data['Car_Model']
    total_seats = validated_data['Car_Seats']
    color = validated_data['Car_Color']
    
    car = Car.objects.create(
        Car_Name = carname,
        Car_Owner = owner,
        Car_Model = model,
        Car_Seats = total_seats,
        Car_Color = color
    )
    
    return car
