using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Xamarin.Forms;
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
        //        gc.currentTrip.GetCurrentAttraction();//-for the hint
        public Attraction nextAttraction;
        public /*static*/ int hintsIndex = 0;
        //trumpeldor.SheredClasses.Point p;
        public GameController gc = ((App)Application.Current).getGameController();
        public LocationController lc;
        trumpeldor.SheredClasses.Point p;
        public double currLat = 0, currLong = 0;
        MapPage myMap = null;
        public NavigationPage ()
		{
			InitializeComponent ();
            nextAttraction = gc.currentTrip.GetCurrentAttraction();
            mapImage.Text = AppResources.map;
            myMap = new MapPage();
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
            //disable all other dynamic buttons
            try {
                Button clicked = (Button)sender;
                clicked.IsEnabled = false;
                DynamicButtonsEnable(false);
            }
            catch { }

            ContentPage temp = this;
            if (nextAttraction.IsThisLastHint(hintsIndex))
            {
                bool dialogAnswer = await DisplayAlert(
                    AppResources.Last_Hint_Alert_Title,
                    AppResources.Last_Hint_Alert_Message,
                    AppResources.Yes,
                    AppResources.No);
                if (!dialogAnswer)
                    return;
                //temp = new MapPage(new SheredClasses.Point(nextAttraction.x, nextAttraction.y));
                myMap.AddPointToMap(myMap.map, new SheredClasses.Point(nextAttraction.x, nextAttraction.y));
                temp = myMap;
                Button hintBtn = (Button)FindByName("hintBtn");
                if (hintBtn != null)
                    hintBtn.IsEnabled = false;
            }
            else
            {
                temp = new HintPage(nextAttraction.hints[hintsIndex]);
            }
            
            hintsIndex++;
            if (hintsIndex >= 3)
                scoreLabel.Text = AppResources.score + ": " + gc.EditScore(GameController.SCORE_VALUE.Hints_More_Than_Three);
            if(temp != this)
                await Navigation.PushModalAsync(temp);
            addToLayout(hintsLayout);

            //enable all other dynamic buttons
            try {
                Button clicked = (Button)sender;
                clicked.IsEnabled = true;
                DynamicButtonsEnable(true);
            }
            catch { }
        }

        private void Next_Destination_Button_Clicked(object sender, EventArgs e)
        {
            Device.BeginInvokeOnMainThread(async () => await DisplayAlert(AppResources.success, AppResources.You_have_Reached_Your_Destionation, AppResources.ok));
            var existingPages = Navigation.NavigationStack.ToList();
            foreach (var page in existingPages)
            {
                Navigation.RemovePage(page);
            }
            Application.Current.MainPage = new AttractionPage();
        }

        private async void mapImage_Clicked(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(myMap);
        }

        private async void DynamicBtn_Clicked(object sender, EventArgs e)
        {
            //disable all other dynamic buttons
            try { DynamicButtonsEnable(false); }
            catch { }

            Button clicked = (Button)sender;
            string strIdx = clicked.Text.Substring(5, clicked.Text.Length - 5);
            int currIdx = Int32.Parse(strIdx) -1;
            if (nextAttraction.IsThisLastHint(currIdx))//hint map
            {
                //await Navigation.PushModalAsync(new MapPage(new SheredClasses.Point(nextAttraction.x, nextAttraction.y)));
                await Navigation.PushModalAsync(myMap);
            }
            else
            {
                await Navigation.PushModalAsync(new HintPage(nextAttraction.hints[currIdx]));
            }

            //enable all other dynamic buttons
            try { DynamicButtonsEnable(true); }
            catch { }
        }
        
        private void DynamicButtonsEnable(bool toEnable)
        {
            foreach (Button btn in hintsLayout.Children)
            {
                btn.IsEnabled = toEnable;
            }
        }

        private void addToLayout(StackLayout layout)
        {
            Button btn = new Button();
            string strIndex = (hintsIndex).ToString();
            btn.Text = "Hint " + strIndex;
            btn.AutomationId = "savedHint" + strIndex;
            btn.Clicked += DynamicBtn_Clicked;
            layout.Children.Add(btn);
        }


        public async Task TimerCheck()
        {
            Device.StartTimer(TimeSpan.FromSeconds(DESIRED_SECONDS), () =>
            {
                try
                {
                    LocationCheck();
                    lc.AddToPositionsHistory(new Plugin.Geolocator.Abstractions.Position(currLat, currLong));
                    if (lc.DistanceBetween(currLat, currLong, p.x, p.y) > DESIRED_DISTANCE)
                    {
                        DisplayAlert(AppResources.not_arrived, lc.DistanceBetween(currLat, currLong, p.x, p.y).ToString() + "curr lat: " + currLat.ToString() + "curr long: " + currLong.ToString() + "x: " + p.x + "y: " + p.y + " point info: " + nextAttraction.name, AppResources.close);
                        return true;
                    }
                    else
                    {
                        gc.EditScore(GameController.SCORE_VALUE.Attraction_Arrive);
                        DisplayAlert(AppResources.arrived, AppResources.arrived + "!  " + lc.DistanceBetween(currLat, currLong, p.x, p.y).ToString(), AppResources.close);
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

        private async Task LocationCheck()
        {
            var locator = CrossGeolocator.Current;
            Plugin.Geolocator.Abstractions.Position position = await locator.GetPositionAsync(TimeSpan.FromSeconds(5));
            currLat = position.Latitude;
            currLong = position.Longitude;
        }
    }
}