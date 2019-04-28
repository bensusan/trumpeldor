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

namespace trumpeldor.Views
{
	[XamlCompilation(XamlCompilationOptions.Compile)]
	public partial class NavigationPage : ContentPage
	{
        private const double DESIRED_DISTANCE = 20;
        private const double DESIRED_SECONDS = 10;
        public static bool isFirst = true;
        public Attraction nextAttraction;
        public static int hintsIndex = 1, currIndex = 0;
        public GameController gc;
        public LocationController lc;
        trumpeldor.SheredClasses.Point p, currLoc;
        MapPage mapInstance = null;

        public NavigationPage ()
		{
			InitializeComponent ();
            gc = GameController.getInstance();
            leftArrow.Source = ServerConection.URL_MEDIA + "leftArrow.png";
            rightArrow.Source = ServerConection.URL_MEDIA + "rightArrow.png";
            temperature.Source = ServerConection.URL_MEDIA + "temperature.png";
            v.Source = ServerConection.URL_MEDIA + "v.png";
            nextAttraction = gc.currentTrip.GetCurrentAttraction();
            mapInstance = new MapPage();
            mapBtn = mapInstance.map;
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
                hintBtn.IsVisible = false;
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

        private void AttachHint(int hintIndex)
        {
            if (nextAttraction.IsThisLastHint(hintIndex))
            {
                //TODO change when shahar will finish
                mapInstance = new MapPage(new SheredClasses.Point(nextAttraction.x, nextAttraction.y));
                hintWebView.IsVisible = false;
                hintText.IsVisible = false;
                hintMap = mapInstance.map;
                hintMap.IsVisible = true;
            }
            else
            {
                hintMap.IsVisible = false;
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
            Device.BeginInvokeOnMainThread(async () => await DisplayAlert(AppResources.success, AppResources.You_have_Reached_Your_Destionation, AppResources.ok));
            var existingPages = Navigation.NavigationStack.ToList();
            foreach (var page in existingPages)
            {
                Navigation.RemovePage(page);
            }
            Application.Current.MainPage = new AttractionPage();
        }

        //private async void mapImage_Clicked(object sender, EventArgs e)
        //{
        //    await Navigation.PushModalAsync(new MapPage());
        //}

        private void LeftArrow_Clicked(object sender, EventArgs e)
        {
            currIndex--;
            AttachHint(currIndex);
            if (currIndex == 0)
                leftArrow.IsEnabled = false;
            rightArrow.IsEnabled = true;
        }

        private async void Map_Focused(object sender, FocusEventArgs e)
        {
            await Navigation.PushModalAsync(mapInstance);
        }

        private void RightArrow_Clicked(object sender, EventArgs e)
        {
            currIndex++;
            AttachHint(currIndex);
            if (currIndex == hintsIndex - 1)
                rightArrow.IsEnabled = false;
            leftArrow.IsEnabled = true;
        }

        //private async void DynamicBtn_Clicked(object sender, EventArgs e)
        //{
        //    Button clicked = (Button)sender;
        //    string strIdx = clicked.Text.Substring(5, clicked.Text.Length - 5);
        //    int currIdx = Int32.Parse(strIdx) -1;
        //    if (nextAttraction.IsThisLastHint(hintsIndex))//hint map
        //    {
        //        await Navigation.PushModalAsync(new MapPage(new SheredClasses.Point(nextAttraction.x, nextAttraction.y)));
        //    }
        //    else
        //    {
        //        await Navigation.PushModalAsync(new HintPage(nextAttraction.hints[currIdx]));
        //    }
        //}


        //private void addToLayout(StackLayout layout)
        //{
        //    Button btn = new Button();
        //    string strIndex = (hintsIndex + 1).ToString();
        //    btn.Text = "Hint " + strIndex;
        //    btn.AutomationId = "savedHint" + strIndex;
        //    btn.Clicked += DynamicBtn_Clicked;
        //    layout.Children.Add(btn);
        //}


        public async Task TimerCheck()
        {
            Device.StartTimer(TimeSpan.FromSeconds(DESIRED_SECONDS), () =>
            {
                //LocationCheck();
                currLoc = gc.GetUserLocation();
                lc.AddToPositionsHistory(new Plugin.Geolocator.Abstractions.Position(currLoc.x, currLoc.y));
                if (lc.DistanceBetween(currLoc.x, currLoc.y, p.x, p.y) > DESIRED_DISTANCE){
                    if(ServerConection.DEBUG == 1)
                        DisplayAlert(AppResources.not_arrived, lc.DistanceBetween(currLoc.x, currLoc.y, p.x, p.y).ToString() + "curr lat: " + currLoc.x + "curr long: " + currLoc.y + "x: " + p.x + "y: " + p.y + " point info: " + nextAttraction.name, AppResources.close);
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