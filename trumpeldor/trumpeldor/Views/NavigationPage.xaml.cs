using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Xamarin.Forms;
using Xamarin.Forms.Maps;
using Xamarin.Forms.Xaml;
using trumpeldor.SheredClasses;
using trumpeldor;
using Plugin.Geolocator;
using System.Timers;

namespace trumpeldor.Views
{
	[XamlCompilation(XamlCompilationOptions.Compile)]
	public partial class NavigationPage : ContentPage
	{
        private const double DESIRED_DISTANCE = 20;
        private const double DESIRED_SECONDS = 10;
        public static bool isFirst = true;
        public static bool firstTimeLocationUpdate = true;
        public Attraction nextAttraction;
        public int hintsIndex = 1, currIndex = 0;
        public GameController gc;
        public LocationController lc;
        trumpeldor.SheredClasses.Point attractionLoc, currLoc;
        public double currLat = 0, currLong = 0;
        MapPage myMap = null;
        private bool firstAttachOfHintMap = true;
        private double startDistanceToDestination;
        //private bool stopDestinationCheck = false;
        private bool done = false;

        public NavigationPage ()
		{
			InitializeComponent ();
            gc = GameController.getInstance();
            leftArrow.Source = ServerConection.URL_MEDIA + "leftArrow.png";
            rightArrow.Source = ServerConection.URL_MEDIA + "rightArrow.png";
            temperature.Source = ServerConection.URL_MEDIA + "temperature.png";
            v.Source = ServerConection.URL_MEDIA + "v.png";
            odometer.Maximum = 1;
            odometer.Minimum = 0;
            odometer.MinimumTrackColor = Color.FromHex("#0066ff");
            odometer.MaximumTrackColor = Color.FromHex("#0066ff");
            odometer.Value = 0;
            nextAttraction = gc.currentTrip.GetCurrentAttraction();
            myMap = new MapPage();
            mapBtn.Source = ServerConection.URL_MEDIA + "googleMaps.png";
            //mapBtn = myMap.map;
            AttachHint(0);
            
            lc = LocationController.GetInstance();
            attractionLoc = new trumpeldor.SheredClasses.Point(nextAttraction.x, nextAttraction.y);
            if (isFirst)
            {
                isFirst = false;
                //Task.Run(() => TimerCheck()).ConfigureAwait(false);
                TimerCheck();
            }
        }

        protected override void OnAppearing()
        {
            base.OnAppearing();
            scoreLabel.Text = AppResources.score + ": " + gc.currentTrip.score;
        }

        private async void Get_Hint_Button_Clicked(object sender, EventArgs e)
        {
            ContentPage temp = this;
            bool dialogAnswer = false;
            if (nextAttraction.IsThisLastHint(hintsIndex)){
                dialogAnswer = await DisplayAlert(
                    AppResources.Last_Hint_Alert_Title,
                    AppResources.Last_Hint_Alert_Message,
                    AppResources.Yes,
                    AppResources.No);
                if (!dialogAnswer)
                    return;
                hintBtn.IsEnabled = false;
            }
            //else
            AttachHint(hintsIndex);
            rightArrow.IsEnabled = false;
            leftArrow.IsEnabled = true;
            currIndex = hintsIndex;
            hintsIndex++;
            if (hintsIndex >= 3)
                scoreLabel.Text = AppResources.score + ": " + gc.EditScore(GameController.SCORE_VALUE.Hints_More_Than_Three);
        }

        private async void AttachHint(int hintIndex)
        {
            if (nextAttraction.IsThisLastHint(hintIndex))
            {
                //TODO change when shahar will finish
                // mapInstance = new MapPage(new SheredClasses.Point(nextAttraction.x, nextAttraction.y));
                if(firstAttachOfHintMap)
                    myMap.AddPointToMap(myMap.map, new SheredClasses.Point(nextAttraction.x, nextAttraction.y));
                hintWebView.IsVisible = false;
                hintText.IsVisible = false;
                await Navigation.PushModalAsync(myMap);
                firstAttachOfHintMap = false;
                //hintMap = myMap.map;
                //hintMap.IsVisible = true;
            }
            else
            {
                //hintMap.IsVisible = false;
                Hint currentHint = nextAttraction.hints[hintIndex];
                if (currentHint.GetKindHint() == Hint.Kinds.HintPicture || currentHint.GetKindHint() == Hint.Kinds.HintVideo){
                    hintText.IsVisible = false;
                    hintWebView.IsVisible = true;
                    hintWebView.Source = currentHint.data;
                }
                else //case text
                {
                    hintWebView.IsVisible = false;
                    hintText.IsVisible = true;
                    hintText.Text = currentHint.data;
                }
            }
        }

        private void Next_Destination_Button_Clicked(object sender, EventArgs e)
        {
            Arrived();
        }

        private void Arrived()
        {
            done = true;
            gc.EditScore(GameController.SCORE_VALUE.Attraction_Arrive);
            var existingPages = Navigation.NavigationStack.ToList();
            foreach (var page in existingPages)
                Navigation.RemovePage(page);
            Application.Current.MainPage = new AttractionPage();
        }

        private void LeftArrow_Clicked(object sender, EventArgs e)
        {
            currIndex--;
            AttachHint(currIndex);
            if (currIndex == 0)
                leftArrow.IsEnabled = false;
            rightArrow.IsEnabled = true;
        }

        private async void Map_Clicked(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(myMap);
        }

        private void RightArrow_Clicked(object sender, EventArgs e)
        {
            currIndex++;
            AttachHint(currIndex);
            if (currIndex == hintsIndex - 1)
                rightArrow.IsEnabled = false;
            leftArrow.IsEnabled = true;
        }

        public void TimerCheck()
        {
            Timer arrivedTimer = new Timer();
            arrivedTimer.Interval = DESIRED_SECONDS * 1000;
            arrivedTimer.Elapsed += (o, e) =>
            {
                if (done)
                    arrivedTimer.Stop();
                currLoc = gc.GetUserLocation();
                if (firstTimeLocationUpdate)
                {
                    firstTimeLocationUpdate = false;
                    startDistanceToDestination = lc.DistanceBetween(currLoc.x, currLoc.y, attractionLoc.x, attractionLoc.y);
                }
                lc.AddToPositionsHistory(new Plugin.Geolocator.Abstractions.Position(currLoc.x, currLoc.y));
                double currentDistanceToDestination = lc.DistanceBetween(currLoc.x, currLoc.y, attractionLoc.x, attractionLoc.y);
                if (currentDistanceToDestination > DESIRED_DISTANCE){
                    if (ServerConection.DEBUG == 1)
                        Device.BeginInvokeOnMainThread (() => {
                            DisplayAlert("Must come closer", lc.DistanceBetween(currLoc.x, currLoc.y, attractionLoc.x, attractionLoc.y).ToString() + "\ncurr lat: " + currLoc.x + "\ncurr long: " + currLoc.y + "\nattractionLoc x: " + attractionLoc.x + "\nattractionLoc y: " + attractionLoc.y + "\npoint info: " + nextAttraction.name, "close");
                        });
                    double percentApproachingTarget = Math.Max(0, Math.Min(1, (1 - (currentDistanceToDestination / startDistanceToDestination))));
                    odometer.Value = percentApproachingTarget;
                    if (percentApproachingTarget < 0.3){
                        odometer.MinimumTrackColor = Color.FromHex("#0066ff");
                        odometer.MaximumTrackColor = Color.FromHex("#0066ff");
                    }
                    else{
                        if (percentApproachingTarget < 0.7){
                            odometer.MinimumTrackColor = Color.FromHex("#b21f4c");
                            odometer.MaximumTrackColor = Color.FromHex("#b21f4c");
                        }
                        else{
                            odometer.MinimumTrackColor = Color.FromHex("#ff0000");
                            odometer.MaximumTrackColor = Color.FromHex("#ff0000");
                        }
                    }
                }
                else
                    Device.BeginInvokeOnMainThread(() => Arrived());
            };
            arrivedTimer.Start();
        }

        //private async Task LocationCheck()
        //{
        //    var locator = CrossGeolocator.Current;
        //    Plugin.Geolocator.Abstractions.Position position = await locator.GetPositionAsync(TimeSpan.FromSeconds(5));
        //    currLat = position.Latitude;
        //    currLong = position.Longitude;
        //}
    }
}