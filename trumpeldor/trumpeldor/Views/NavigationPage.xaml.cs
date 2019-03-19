using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Xamarin.Forms;
using Xamarin.Forms.Xaml;
using trumpeldor.SheredClasses;
using trumpeldor;
namespace trumpeldor.Views
{
	[XamlCompilation(XamlCompilationOptions.Compile)]
	public partial class NavigationPage : ContentPage
	{
        //        gc.currentTrip.GetCurrentAttraction();//-for the hint
        public Attraction nextAttraction;
        public static int hintsIndex = 0;
        //trumpeldor.SheredClasses.Point p;
        public GameController gc = ((App)Application.Current).getGameController();
        public NavigationPage ()
		{
			InitializeComponent ();
            nextAttraction = gc.currentTrip.GetCurrentAttraction();
            mapImage.Text = AppResources.map;
        }

        protected override void OnAppearing()
        {
            base.OnAppearing();
            scoreLabel.Text = AppResources.score + ": " + gc.currentTrip.score;
        }

        private async void Get_Hint_Button_Clicked(object sender, EventArgs e)
        {
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
                temp = new MapPage(new SheredClasses.Point(nextAttraction.x, nextAttraction.y));
                Button hintBtn = (Button)FindByName("hintBtn");
                if (hintBtn != null)
                    hintBtn.IsEnabled = false;
            }
            else
            {
                temp = new HintPage(nextAttraction.hints[hintsIndex]);
            }
            addToLayout(hintsLayout);
            hintsIndex++;
            if (hintsIndex >= 3)
                scoreLabel.Text = AppResources.score + ": " + gc.EditScore(GameController.SCORE_VALUE.Hints_More_Than_Three);
            if(temp != this)
                await Navigation.PushModalAsync(temp);
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
            await Navigation.PushModalAsync(new MapPage());
        }

        private async void DynamicBtn_Clicked(object sender, EventArgs e)
        {
            Button clicked = (Button)sender;
            string strIdx = clicked.Text.Substring(5, clicked.Text.Length - 5);
            int currIdx = Int32.Parse(strIdx) -1;
            if (nextAttraction.IsThisLastHint(hintsIndex))//hint map
            {
                await Navigation.PushModalAsync(new MapPage(new SheredClasses.Point(nextAttraction.x, nextAttraction.y)));
            }
            else
            {
                await Navigation.PushModalAsync(new HintPage(nextAttraction.hints[currIdx]));
            }
        }
        

        private void addToLayout(StackLayout layout)
        {
            Button btn = new Button();
            string strIndex = (hintsIndex + 1).ToString();
            btn.Text = "Hint " + strIndex;
            btn.AutomationId = "savedHint" + strIndex;
            btn.Clicked += DynamicBtn_Clicked;
            layout.Children.Add(btn);
        }
    }
}