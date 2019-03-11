using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Xamarin.Forms;
using Xamarin.Forms.Xaml;
using trumpeldor.SheredClasses;
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
            //p = new trumpeldor.SheredClasses.Point(nextAttraction.x, nextAttraction.y);
            //nextAttraction = gc.currentTrip.GetCurrentAttraction();
            //mapImage.Source = ImageSource.FromResource("trumpeldor.Resources.MapIcon.png");
            mapImage.Text = AppResources.map;
            //SheredClasses.Clue nextClue = gc.GetFisrtHint();
            //nextClue.addToLayout(hintsLayout);
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
            }
            else
            {
                //Hint nextHint = nextAttraction.hints[hintsIndex];
                //if (nextHint.kind.Equals("HM"))//hint map
                //{
                //    await Navigation.PushModalAsync(new MapPage(gc.GetUserLocation()));
                //}
                //else
                //{
                //await Navigation.PushModalAsync(new HintPage(nextHint));
                //}
                temp = new HintPage(nextAttraction.hints[hintsIndex]);
            }
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

        private void addToLayout(StackLayout layout)
        {
            Button btn = new Button();
            string strIndex = (hintsIndex + 1).ToString();
            btn.Text = "Hint " + strIndex;
            layout.Children.Add(btn);
        }
    }
}