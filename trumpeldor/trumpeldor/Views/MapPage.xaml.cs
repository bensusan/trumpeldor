using Plugin.Geolocator;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Timers;
using System.Threading.Tasks;

using Xamarin.Forms;
using Xamarin.Forms.Maps;
using Xamarin.Forms.Xaml;

namespace trumpeldor.Views
{
    [XamlCompilation(XamlCompilationOptions.Compile)]
    public partial class MapPage : ContentPage
    {
        //fixed point
        private GameController gc = ((App)(Application.Current)).getGameController();
        private const double DESIRED_DISTANCE = 100;
        Point p = new Point(31.262566, 34.796832);
        Pin previous = new Pin();
        //current point
        double currLat = 0, currLong = 0;

        public MapPage()
        {
            InitializeComponent();

            //gc.currentTrip.GetCurrentAttraction().x
            Map map = new Map()
            {
                HeightRequest = 100,
                WidthRequest = 960,
                VerticalOptions = LayoutOptions.FillAndExpand
            };
            map.MoveToRegion(MapSpan.FromCenterAndRadius(new Position(31.262820, 34.802352), Distance.FromKilometers(3)).WithZoom(10));
            List<SheredClasses.Attraction> visitedTrackPoints = ((App)(Application.Current)).getGameController().GetVisitedAttractions();
            foreach (SheredClasses.Attraction attraction in visitedTrackPoints)
            {
                Pin pin = new Pin
                {
                    Type = PinType.Place,
                    Position = new Position(attraction.x, attraction.y),
                    Label = attraction.name,
                    Address="35"
                };
                map.Pins.Add(pin);
            }
            AddCurrlocationToMap(map);

             Content = map;
            
            //return FromLocA.GetDistanceTo(ToLocB);
            Device.StartTimer(TimeSpan.FromSeconds(1), () =>
            {
                try
                {
                    OnLocationCheck(previous, map);

                    //!((_&&_)||(_&&_))-->!(_&&_) && !(_&&_)
                    if (DistanceBetween(currLong, currLat, p.X, p.Y) > 100)
                    {

                        return true;
                    }
                    else
                    {
                        DisplayAlert("Signed in!", "arrived!", "Close");
                        return false;
                    }
                    // True = Repeat again, False = Stop the timer
                }
                catch (Exception e)
                {
                    Console.WriteLine("ERROR: "+e.Message);
                    return false;
                }
            });
        }

        private async void AddCurrlocationToMap (Map map)
        {
            var locator = CrossGeolocator.Current;
            Plugin.Geolocator.Abstractions.Position position =await locator.GetPositionAsync();
            Pin currLocationPin = new Pin
            {
                Type = PinType.Place,
                Position = new Position(position.Latitude, position.Longitude),
                Label = "current location"
            };
            previous = currLocationPin;
            currLat = position.Latitude;
            currLong = position.Longitude;
            map.Pins.Add(currLocationPin); 
        }

        private async void OnLocationCheck(Pin prev, Map map)
        {
            //remove from map the previous current location
            //draw on map the current location
            //chec if current location is around the fixed point:
            //if yes-show message to go to the point page and stop check location
            //if no-continue check location
            var locator = CrossGeolocator.Current;
            Plugin.Geolocator.Abstractions.Position position = await locator.GetPositionAsync();
            Pin currLocationPin = new Pin
            {
                Type = PinType.Place,
                Position = new Position(position.Latitude, position.Longitude),
                Label = "current location"
            };
            currLat = position.Latitude;
            currLong = position.Longitude;
            previous = currLocationPin;
            map.Pins.Remove(prev);
            map.Pins.Add(currLocationPin);
        }
        private double DistanceBetween(double lat1, double lon1, double lat2, double lon2)//distance in meters
        {
            double R = 6371000; // Radius of the earth in meters
            double dLat = deg2rad(lat2 - lat1);  // deg2rad below
            double dLon = deg2rad(lon2 - lon1);
            double a =
              Math.Sin(dLat / 2) * Math.Sin(dLat / 2) +
              Math.Cos(deg2rad(lat1)) * Math.Cos(deg2rad(lat2)) *
              Math.Sin(dLon / 2) * Math.Sin(dLon / 2)
              ;
            double c = 2 * Math.Atan2(Math.Sqrt(a), Math.Sqrt(1 - a));
            double d = R * c; // Distance in km
            return d;
        }

        private double deg2rad(double deg)
        {
            return deg * (Math.PI / 180);
        }




    }
}