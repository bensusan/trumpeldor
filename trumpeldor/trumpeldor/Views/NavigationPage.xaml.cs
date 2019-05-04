﻿using System;
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
        trumpeldor.SheredClasses.Point p, currLoc;
        public double currLat = 0, currLong = 0;
        MapPage myMap = null;
<<<<<<< HEAD
        private bool firstAttachOfHintMap = true;
=======
        private double startDistanceToDestination;
>>>>>>> odometer2

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
            p = new trumpeldor.SheredClasses.Point(nextAttraction.x, nextAttraction.y);
            if (isFirst)
            {
                isFirst = false;
                Task.Run(async () =>
                {
                    await TimerCheck();
                }).ConfigureAwait(false);
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
            //Device.BeginInvokeOnMainThread(async () => await DisplayAlert(AppResources.success, AppResources.You_have_Reached_Your_Destionation, AppResources.ok));
            var existingPages = Navigation.NavigationStack.ToList();
            foreach (var page in existingPages)
            {
                Navigation.RemovePage(page);
            }
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

        public async Task TimerCheck()
        {
            Device.StartTimer(TimeSpan.FromSeconds(DESIRED_SECONDS), () =>
            {
                //LocationCheck();
                currLoc = gc.GetUserLocation();
                if (firstTimeLocationUpdate)
                {
                    firstTimeLocationUpdate = false;
                    startDistanceToDestination = lc.DistanceBetween(currLoc.x, currLoc.y, p.x, p.y);
                }
                lc.AddToPositionsHistory(new Plugin.Geolocator.Abstractions.Position(currLoc.x, currLoc.y));
                double currentDistanceToDestination = lc.DistanceBetween(currLoc.x, currLoc.y, p.x, p.y);
                if (currentDistanceToDestination > DESIRED_DISTANCE){
                    if(ServerConection.DEBUG == 1)
                        DisplayAlert(AppResources.not_arrived, lc.DistanceBetween(currLoc.x, currLoc.y, p.x, p.y).ToString() + "curr lat: " + currLoc.x + "curr long: " + currLoc.y + "x: " + p.x + "y: " + p.y + " point info: " + nextAttraction.name, AppResources.close);
                    double percentApproachingTarget = Math.Max(0, Math.Min(1, (1 - (currentDistanceToDestination / startDistanceToDestination))));
                    odometer.Value = percentApproachingTarget;
                    if (percentApproachingTarget < 0.3)
                    {
                        odometer.MinimumTrackColor = Color.FromHex("#0066ff");
                        odometer.MaximumTrackColor = Color.FromHex("#0066ff");
                    }
                    else
                    {
                        if (percentApproachingTarget < 0.7)
                        {
                            odometer.MinimumTrackColor = Color.FromHex("#b21f4c");
                            odometer.MaximumTrackColor = Color.FromHex("#b21f4c");
                        }
                        else
                        {
                            odometer.MinimumTrackColor = Color.FromHex("#ff0000");
                            odometer.MaximumTrackColor = Color.FromHex("#ff0000");
                        }
                    }
                    return true;
                }
                else{
                    gc.EditScore(GameController.SCORE_VALUE.Attraction_Arrive);
                    if (ServerConection.DEBUG == 1)
                        DisplayAlert(AppResources.arrived, AppResources.arrived + "! " + lc.DistanceBetween(currLoc.x, currLoc.y, p.x, p.y).ToString(), AppResources.close);
                    Application.Current.MainPage = new AttractionPage();
                    return false;
                }
            });
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