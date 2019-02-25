using Plugin.Geolocator;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Timers;
using System.Threading.Tasks;
using trumpeldor.SheredClasses;

using Xamarin.Forms;
using Xamarin.Forms.Maps;
using Xamarin.Forms.Xaml;

namespace trumpeldor.Views
{
    [XamlCompilation(XamlCompilationOptions.Compile)]
    public partial class MapPage : ContentPage
    {
        
        private const double DESIRED_DISTANCE = 30;
        private const double DESIRED_SECONDS = 10;
        //Point p = new Point(31.262566, 34.796832); (latitude -> x, longtitude -> y)
        Point p = new Point();
        Pin previous = null;
        //current point
        double currLat = 0, currLong = 0;
        public GameController gc = ((App)Application.Current).getGameController();
        public Attraction nextAttraction;
        public MapPage(Point p)
        {
            InitializeComponent();
            nextAttraction = gc.currentTrip.GetCurrentAttraction();
            p.X = nextAttraction.x;
            p.Y = nextAttraction.y;
            Map map = new Map()
            {
                HeightRequest = 100,
                WidthRequest = 960,
                VerticalOptions = LayoutOptions.FillAndExpand
            };
            map.MoveToRegion(MapSpan.FromCenterAndRadius(new Position(31.262820, 34.802352), Distance.FromKilometers(3)).WithZoom(10));
            List<SheredClasses.Attraction> visitedTrackPoints = ((App)(Application.Current)).getGameController().GetVisitedAttractions();
            AddCurrlocationToMap(map);
            AddPointToMap(map, p);
            Content = map;
        }

        public MapPage()
        {
            InitializeComponent();
            nextAttraction = gc.currentTrip.GetCurrentAttraction();
            p.X = nextAttraction.x;
            p.Y = nextAttraction.y;
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
            Device.StartTimer(TimeSpan.FromSeconds(DESIRED_SECONDS), () =>
            {
                try
                {
                    OnLocationCheck(map);

                    //!((_&&_)||(_&&_))-->!(_&&_) && !(_&&_)
                    if (DistanceBetween(currLat, currLong, p.X, p.Y) > DESIRED_DISTANCE)
                    {
                        DisplayAlert(AppResources.not_arrived, DistanceBetween(currLat, currLong, p.X, p.Y).ToString()+"x: "+p.X + "y: " + p.Y+" point info: "+nextAttraction.name, AppResources.close);
                        return true;
                    }
                    else
                    {
                        DisplayAlert(AppResources.arrived, AppResources.arrived+"!  " + DistanceBetween(currLat, currLong, p.X, p.Y).ToString(), AppResources.close);
                        Application.Current.MainPage = new AttractionPage();
                        return false;
                    }
                    // True = Repeat again, False = Stop the timer
                }
                catch (Exception e)
                {
                    Console.WriteLine(AppResources.error+": "+e.Message);
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


        private void AddPointToMap(Map map, Point p)
        {
            Pin toAdd = new Pin
            {
                Type = PinType.Place,
                Position = new Position(p.X, p.Y),
                Label = "the attraction"
            };
            map.Pins.Add(toAdd);
        }


        private async void OnLocationCheck(Map map)
        {
            //remove from map the previous current location
            //draw on map the current location
            //chec if current location is around the fixed point:
            //if yes-show message to go to the point page and stop check location
            //if no-continue check location
            var locator = CrossGeolocator.Current;
            Plugin.Geolocator.Abstractions.Position position = await locator.GetPositionAsync();
            Pin newCurrLocationPin = new Pin
            {
                Type = PinType.Place,
                Position = new Position(position.Latitude, position.Longitude),
                Label = "current new location"
            };
            currLat = position.Latitude;
            currLong = position.Longitude;
            map.Pins.Remove(previous);
            map.Pins.Add(newCurrLocationPin);
            previous = newCurrLocationPin;
        }
        public double DistanceBetween(double lat1, double lon1, double lat2, double lon2)//distance in meters
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
            double d = R * c ; 
            return d;
        }

        public double deg2rad(double deg)
        {
            return deg * (Math.PI / 180);
        }




    }
}