from geopy.geocoders import Nominatim
import time
import folium

def locationByCoordinate(latitude, longitude) :
    """
    This Function returns the location in the format of {City}, {State}, {PinCode}(In Few Cases), {Country}
    !!! Important Note : You need internet connection to access the result.
    ??? If you get a error its most likely because you have a network issue, not having the (geopy) module or not given proper details
    """
    geoLoc = Nominatim(user_agent="GetLoc")
    coordinateString = f"{latitude}, {longitude}"
    locationCoordinates = geoLoc.reverse(coordinateString)
    return locationCoordinates.address

def openMap() : 
    ...
    maplocation = folium.Map(location = [latitude_input, longitude_input], zoom_start = 10)
    folium.Marker(
        location=[latitude_input, longitude_input],
        popup="Location",
    ).add_to(maplocation)
    maplocation.save("location.html")


if __name__ == '__main__':
    try :
        latitude_input = input("Enter Latitude :\t")
        longitude_input = input("Enter Longitude : \t")
        print(locationByCoordinate(latitude= latitude_input, longitude= longitude_input))
        openMap()
        
    except Exception as e: 
        print("Error !!!")
        

