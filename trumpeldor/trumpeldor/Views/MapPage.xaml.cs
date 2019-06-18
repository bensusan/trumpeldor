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
        public CustomMap map;
        private const double DESIRED_DISTANCE = 10;
        private const double DESIRED_SECONDS = 10;

        //Point p = new Point(31.262566, 34.796832); (latitude -> x, longtitude -> y)
        //Point p = new Point(31.262566, 34.796832);
        trumpeldor.SheredClasses.Point p;

        Pin previous = null;
        private static bool firstListInit = true;
        private static List<Position> traveledPins;
        //current point
        public double currLat = 0, currLong = 0;
        public GameController gc;
        public LocationController lc;
        public Attraction nextAttraction;
        private static MapPage instance = null;
        List<SheredClasses.Attraction> visitedTrackPoints = null;
        Attraction hintedAttraction = null;
        Pin hintedPin = null;

        public MapPage()
        {
            InitializeComponent();
            gc = GameController.getInstance();
            lc = LocationController.GetInstance();
            nextAttraction = gc.currentTrip.GetCurrentAttraction();
            p = new trumpeldor.SheredClasses.Point(nextAttraction.x, nextAttraction.y);
            //-------------------------------------------------------------------
            map = new CustomMap
            {
                MapType = MapType.Street,
                WidthRequest = 100,
                HeightRequest = 960,
                VerticalOptions = LayoutOptions.FillAndExpand
            };
            Content = map;
            map.MoveToRegion(MapSpan.FromCenterAndRadius(new Position(31.262820, 34.802352), Distance.FromKilometers(3)).WithZoom(10));

            //-------------------------------------------------------------------

            /*
            List<SheredClasses.Attraction> visitedTrackPoints = gc.GetVisitedAttractions();
            foreach (SheredClasses.Attraction attraction in visitedTrackPoints)
            {
                Pin pin = new Pin
                {
                    Type = PinType.Place,
                    Position = new Position(attraction.x, attraction.y),
                    Label = gc.GetCurrentLanguageText(attraction.name),
                };
                map.Pins.Add(pin);
            }
            AddCurrlocationToMap(map);

           
            Content = map;
            DrawPastPath(map);
            map.MoveToRegion(MapSpan.FromCenterAndRadius(new Position(31.262820, 34.802352), Distance.FromKilometers(3)).WithZoom(10));
        */
        }


        public static MapPage GetInstance()
        {
            if (instance == null)
            {
                instance = new MapPage();
            }
            return instance;
        }
        

        public void DrawPastAttractions()
        {
            visitedTrackPoints = gc.GetVisitedAttractions();
            foreach (SheredClasses.Attraction attraction in visitedTrackPoints)
            {
                Pin pin = new Pin
                {
                    Type = PinType.Place,
                    Position = new Position(attraction.x, attraction.y),
                    Label = gc.GetCurrentLanguageText(attraction.name),
                };
                map.Pins.Add(pin);
            }
        }

        public async Task TimerCheck(CustomMap map)
        {
            Device.StartTimer(TimeSpan.FromSeconds(DESIRED_SECONDS), () =>
            {
                try
                {
                    OnLocationCheck(map);
                    lc.AddToPositionsHistory(new Plugin.Geolocator.Abstractions.Position(currLat, currLong));
                    if (DistanceBetween(currLat, currLong, p.x, p.y) > DESIRED_DISTANCE)
                    {
                        DisplayAlert(AppResources.not_arrived, DistanceBetween(currLat, currLong, p.x, p.y).ToString()+"curr lat: "+ currLat.ToString() +"curr long: "+ currLong.ToString() +"x: "+p.x + "y: " + p.y+" point info: "+nextAttraction.name, AppResources.close);
                        return true;
                    }
                    else
                    {
                        gc.EditScore(ScoreRule.Kinds.Attraction_Arrive);
                        DisplayAlert(AppResources.arrived, AppResources.arrived+"!  " + DistanceBetween(currLat, currLong, p.x, p.y).ToString(), AppResources.close);
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

        public void AddCurrlocationToMap (trumpeldor.SheredClasses.Point location)
        {
            //var locator = CrossGeolocator.Current;
            //Plugin.Geolocator.Abstractions.Position position =await locator.GetPositionAsync();

            //trumpeldor.SheredClasses.Point p = gc.GetUserLocation();
            Pin currLocationPin = new Pin
            {
                Type = PinType.Place,
                Position = new Position(location.x, location.y),
                Label = "current location"
            };
            previous = currLocationPin;
            currLat = location.x;
            currLong = location.y;
            map.Pins.Add(currLocationPin); 
        }

        public void AddToHistory(Plugin.Geolocator.Abstractions.Position p)
        {
            lc.AddToPositionsHistory(p);
        }

        public void AddPointToMap(trumpeldor.SheredClasses.Point p, Attraction attraction)
        {
            Pin toAdd = new Pin
            {
                Type = PinType.Place,
                Position = new Position(p.x, p.y),
                Label=gc.GetCurrentLanguageText(attraction.name)
            };
            hintedAttraction = attraction;
            hintedPin = toAdd;
            map.Pins.Add(toAdd);
        }



        private async Task OnLocationCheck(Map map)
        {
            var locator = CrossGeolocator.Current;
            Plugin.Geolocator.Abstractions.Position position = await locator.GetPositionAsync(TimeSpan.FromSeconds(5));
            //SheredClasses.Point p = gc.GetUserLocation();
            Pin newCurrLocationPin = new Pin
            {
                Type = PinType.Place,
                Position = new Position(position.Latitude, position.Longitude),
                Label = "current new location"
            };
            currLat = position.Latitude;
            currLong = position.Longitude;
            if (previous != null)
            {
                previous.Label = "8888";
                map.Pins.Remove(previous);
            }
            map.Pins.Add(newCurrLocationPin);
            previous = newCurrLocationPin;
        }


        public void OnTimerCheck(Plugin.Geolocator.Abstractions.Position position)
        {
            //map.Pins.Clear();
            DrawPastAttractions();
            Pin newCurrLocationPin = new Pin
            {
                Type = PinType.Place,
                Position = new Position(position.Latitude, position.Longitude),
                Label = "current new location"
            };
            currLat = position.Latitude;
            currLong = position.Longitude;
            if (previous != null)
            {
                map.Pins.Remove(previous);
                //lc.RemoveFromHistory(new Plugin.Geolocator.Abstractions.Position(previous.Position.Latitude, previous.Position.Longitude));
            }
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

        public void DrawPastPath()
        {
            map.RouteCoordinates.Clear();
            List<Plugin.Geolocator.Abstractions.Position> lst = lc.GetStoredPositions();
            if (lst != null)
            {
                foreach (Plugin.Geolocator.Abstractions.Position pos in lst)
                {
                    if (pos != null && pos.Latitude != 0 && pos.Longitude != 0)
                    {
                        map.RouteCoordinates.Add(new Xamarin.Forms.Maps.Position(pos.Latitude, pos.Longitude));
                    }
                }
            }
        }

        public void ClearPastPath()
        {
            map.RouteCoordinates.Clear();
        }




    }
}