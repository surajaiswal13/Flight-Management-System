class User(models.Model):

    name = models.CharField(max_length=20)
    passport_no = models.CharField(max_length=20)
    phone_no = models.CharField(max_length=10)
    location = models.CharField(max_length=100)
    aadhar_no = models.CharField(max_length=15)
    profile_photo = models.CharField(max_length=20)

class Flights(models.Model):

    flight_name = models.CharField(max_length=20)
    flight_start_time = models.DateTimeField()
    flight_end_time = models.DateTimeField()
    route = model.CharField(max_length=50)

class Seats(models.Model):

    seat_no = models.CharField(max_length=5)
    seat_side = models.CharField(max_length=10)
    seat_availibilty = models.CharField(max_length=10)
    flights = models.ForeignKey("Flights")
    user_id = models.ForeignKey("User")

def reserver(user, flight, seat_no):


