using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace trumpeldor.Views
{
	[XamlCompilation(XamlCompilationOptions.Compile)]
	public partial class FinishTrackPage : ContentPage
	{
        GameController gc;
		public FinishTrackPage (bool isSubTrack)
		{
			InitializeComponent();
            gc = GameController.getInstance();
            continueButton.IsVisible = isSubTrack;
        }

        protected override void OnAppearing()
        {
            base.OnAppearing();
            scoreLabel.Text = AppResources.score + ": " + gc.GetScore();
        }

        private async Task<bool> GetFeedback()
        {
            int answer = 0;
            bool ans = await DisplayAlert(AppResources.Done_Trip_Title, AppResources.Done_Trip_Message, AppResources.Yes, AppResources.No);
            if (ans)
                answer = 1;
            else
                answer = 2;
            if (answer == 1)
            {
                Application.Current.MainPage = new FeedbackPage();
                return true;
            }
            return false;
            //await Navigation.PushModalAsync();
        }

        private void Continiue_Button_Clicked(object sender, EventArgs e)
        {
            gc.ContinueToLongerTrack();
            var existingPages = Navigation.NavigationStack.ToList();
            foreach (var page in existingPages)
            {
                Navigation.RemovePage(page);
            }
            Application.Current.MainPage = new NavigationPage();
        }

        private async void Share_Button_Clicked(object sender, EventArgs e)
        {
            int answer = 0;
            bool ans = await DisplayAlert(AppResources.Share_Title, AppResources.Share_First_Part_Message + gc.currentUser.socialNetwork + "?\n" + AppResources.Share_Second_Part_Message, AppResources.Option_1, AppResources.Option_2);
            if (ans)
                answer = 1;
            else
                answer = 2;
            if (answer == 1)
                ShareInExistingSocialNetwork();
            await Navigation.PushModalAsync(new SharePageChoice());
        }

        private void ShareInExistingSocialNetwork()
        {

        }

        private async void Leading_Table_Button_Clicked(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(new LeadingTablePage());
        }

        private async void Done_Button_Clicked(object sender, EventArgs e)
        {
            if (!await GetFeedback())
            {
                var existingPages = Navigation.NavigationStack.ToList();
                foreach (var page in existingPages)
                {
                    Navigation.RemovePage(page);
                }
                gc.UpdateTrip();
                Application.Current.MainPage = new FirstPage();
            }
        }

    }
}