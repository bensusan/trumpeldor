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
        
        private const double DESIRED_DISTANCE = 600;
        private const double DESIRED_SECONDS = 5;

        //Point p = new Point(31.262566, 34.796832); (latitude -> x, longtitude -> y)
        //Point p = new Point(31.262566, 34.796832);
        trumpeldor.SheredClasses.Point p;

        Pin previous = null;
        private static bool firstListInit = true;
        private static List<Position> traveledPins;
        //current point
        public double currLat = 0, currLong = 0;
        public GameController gc;
        public Attraction nextAttraction;
        public MapPage(trumpeldor.SheredClasses.Point p)
        {
            InitializeComponent();
            gc = GameController.getInstance();
            nextAttraction = gc.currentTrip.GetCurrentAttraction();
            if (firstListInit)
            {
                traveledPins = new List<Position>();
                firstListInit = false;
            }
            //-------------------------------------------------------------------
            var map = new CustomMap
            {
                MapType = MapType.Street,
                WidthRequest = 100,
                HeightRequest = 960,
                VerticalOptions = LayoutOptions.FillAndExpand
            };
            map.MoveToRegion(MapSpan.FromCenterAndRadius(new Position(31.262820, 34.802352), Distance.FromKilometers(3)).WithZoom(10));
            //List<SheredClasses.Attraction> visitedTrackPoints = ((App)(Application.Current)).getGameController().GetVisitedAttractions();
            AddCurrlocationToMap(map);
            AddPointToMap(map, p);
            
            Content = map;
        }

        public MapPage()
        {
            InitializeComponent();
            gc = GameController.getInstance();
            nextAttraction = gc.currentTrip.GetCurrentAttraction();
            p = new trumpeldor.SheredClasses.Point(nextAttraction.x, nextAttraction.y);
            //-------------------------------------------------------------------
            var map = new CustomMap
            {
                MapType = MapType.Street,
                WidthRequest = 100,
                HeightRequest = 960,
                VerticalOptions = LayoutOptions.FillAndExpand
            };
            //-------------------------------------------------------------------
            //gc.currentTrip.GetCurrentAttraction().x
            map.MoveToRegion(MapSpan.FromCenterAndRadius(new Position(31.262820, 34.802352), Distance.FromKilometers(3)).WithZoom(10));
            List<SheredClasses.Attraction> visitedTrackPoints = gc.GetVisitedAttractions();
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
            DrawPastPath(map);
            map.MoveToRegion(MapSpan.FromCenterAndRadius(new Position(37.79752, -122.40183), Distance.FromMiles(1.0)));

            TimerCheck(map);
            //return FromLocA.GetDistanceTo(ToLocB);
            
        }

        private void TimerCheck(CustomMap map)
        {
            Device.StartTimer(TimeSpan.FromSeconds(DESIRED_SECONDS), () =>
            {
                try
                {
                    OnLocationCheck(map);
                    if(traveledPins != null)
                        traveledPins.Add(new Position(currLat, currLong));
                    if (DistanceBetween(currLat, currLong, p.x, p.y) > DESIRED_DISTANCE)
                    {
                        //DisplayAlert(AppResources.not_arrived, DistanceBetween(currLat, currLong, p.x, p.y).ToString()+"curr lat: "+ currLat.ToString() +"curr long: "+ currLong.ToString() +"x: "+p.x + "y: " + p.y+" point info: "+nextAttraction.name, AppResources.close);
                        return true;
                    }
                    else
                    {
                        gc.EditScore(GameController.SCORE_VALUE.Attraction_Arrive);
                        //DisplayAlert(AppResources.arrived, AppResources.arrived+"!  " + DistanceBetween(currLat, currLong, p.x, p.y).ToString(), AppResources.close);
                        Application.Current.MainPage = new AttractionPage();
                        return false;
                    }
                    // True = Repeat again, False = Stop the timer
                }
                catch (Exception e)
                {
                    return false;
                }
            });
        }


        private void AddCurrlocationToMap (Map map)
        {
            //var locator = CrossGeolocator.Current;
            //Plugin.Geolocator.Abstractions.Position position =await locator.GetPositionAsync();
            trumpeldor.SheredClasses.Point p = gc.GetUserLocation();
            Pin currLocationPin = new Pin
            {
                Type = PinType.Place,
                Position = new Position(p.x, p.y),
                Label = "current location"
            };
            previous = currLocationPin;
            currLat = p.x;
            currLong = p.y;
            map.Pins.Add(currLocationPin); 
        }



        private void AddPointToMap(Map map, trumpeldor.SheredClasses.Point p)
        {
            Pin toAdd = new Pin
            {
                Type = PinType.Place,
                Position = new Position(p.x, p.y),
                Label = "the attraction"
                
               
            };
            map.Pins.Add(toAdd);
        }


        private void OnLocationCheck(Map map)
        {
            //remove from map the previous current location
            //draw on map the current location
            //chec if current location is around the fixed point:
            //if yes-show message to go to the point page and stop check location
            //if no-continue check location
            //var locator = CrossGeolocator.Current;
            //Plugin.Geolocator.Abstractions.Position position = await locator.GetPositionAsync();
            SheredClasses.Point p = gc.GetUserLocation();
            Pin newCurrLocationPin = new Pin
            {
                Type = PinType.Place,
                Position = new Position(p.x, p.y),
                Label = "current new location"
            };
            currLat = p.x;
            currLong = p.y;
            map.Pins.Remove(previous);
            map.Pins.Add(newCurrLocationPin);
            previous = newCurrLocationPin;
        }
        public static double DistanceBetween(double lat1, double lon1, double lat2, double lon2)//distance in meters
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

        public static double deg2rad(double deg)
        {
            return deg * (Math.PI / 180);
        }

        private void DrawPastPath(CustomMap map)
        {
            map.RouteCoordinates.Clear();
            foreach(Position pos in traveledPins)
                map.RouteCoordinates.Add(pos);
        }


    }
}