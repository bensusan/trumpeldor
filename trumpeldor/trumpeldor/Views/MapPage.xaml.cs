using Plugin.Geolocator;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Xamarin.Forms;
using Xamarin.Forms.Maps;
using Xamarin.Forms.Xaml;

namespace trumpeldor.Views
{
    [XamlCompilation(XamlCompilationOptions.Compile)]
    public partial class MapPage : ContentPage
    {
        public MapPage()
        {
            InitializeComponent();

            Map map = new Map()
            {
                HeightRequest = 100,
                WidthRequest = 960,
                VerticalOptions = LayoutOptions.FillAndExpand
            };
            map.MoveToRegion(MapSpan.FromCenterAndRadius(new Position(31.262820, 34.802352), Distance.FromKilometers(3)).WithZoom(10));
            List<SheredClasses.TrackPoint> visitedTrackPoints = ((App)(Application.Current)).getGameController().GetVisitedTrackPoints();
            foreach (SheredClasses.TrackPoint trackPoint in visitedTrackPoints)
            {
                Pin pin = new Pin
                {
                    Type = PinType.Place,
                    Position = new Position(trackPoint.GetLatitude(), trackPoint.GetLongitude()),
                    Label = trackPoint.GetName(),
                    Address="35"
                };
                map.Pins.Add(pin);
            }
            AddCurrlocationToMap(map);

             Content = map;
        }

        private async void AddCurrlocationToMap(Map map)
        {
            var locator = CrossGeolocator.Current;
            Plugin.Geolocator.Abstractions.Position position =await locator.GetPositionAsync(TimeSpan.FromSeconds(10));
            Pin currLocationPin = new Pin
            {
                Type = PinType.Place,
                Position = new Position(position.Latitude, position.Longitude),
                Label = "current location"
            };
            map.Pins.Add(currLocationPin);
        }
    }
}