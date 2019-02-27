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
			InitializeComponent ();
            gc = GameController.getInstance();
            titleLabel.Text = AppResources.congrdulation_you_finish_the_track_with + " " + ((App)Application.Current).getGameController().GetScore() + " " + AppResources.points+ " .";
            continueButton.IsVisible = isSubTrack;
        }

        private void Continiue_Button_Clicked(object sender, EventArgs e)
        {
            //((App)Application.Current).getGameController().ContinueToLongerTrack();
            //((App)Application.Current).getGameController().SelectNextAttraction();

            //var existingPages = Navigation.NavigationStack.ToList();
            //foreach (var page in existingPages)
            //{
            //    Navigation.RemovePage(page);
            //}
            //Application.Current.MainPage = new NavigationPage(); 
        }
        private void Share_Button_Clicked(object sender, EventArgs e)
        {

        }
        private void Leading_Table_Button_Clicked(object sender, EventArgs e)
        {

        }
        private async void feedback_Button_Clicked(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(new FeedbackPage());
        }
        private async void information_Button_Clicked(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(new informationPage());
        }
    }
}